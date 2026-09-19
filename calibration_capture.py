from __future__ import annotations
from hashlib import sha256
from pathlib import Path
import json, numpy as np

def hf_module_to_gguf_weight(module_name: str) -> str | None:
    if module_name == "lm_head":
        return "output.weight"
    prefixes=("model.layers.","transformer.layers.")
    prefix=next((p for p in prefixes if module_name.startswith(p)),None)
    if prefix is None:return None
    rest=module_name[len(prefix):]
    parts=rest.split(".",1)
    if len(parts)!=2 or not parts[0].isdigit():return None
    block=int(parts[0]); tail=parts[1]
    mapping={
      "self_attn.q_proj":"attn_q","self_attn.k_proj":"attn_k","self_attn.v_proj":"attn_v",
      "self_attn.o_proj":"attn_output","mlp.gate_proj":"ffn_gate","mlp.up_proj":"ffn_up","mlp.down_proj":"ffn_down"}
    role=mapping.get(tail)
    return None if role is None else f"blk.{block}.{role}.weight"

def main():
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    model_id="Qwen/Qwen2.5-0.5B-Instruct"
    corpus=Path("calibration_corpus.txt")
    output=Path("activation.npz")
    text=corpus.read_text(encoding="utf-8")
    tok=AutoTokenizer.from_pretrained(model_id)
    ids=tok(text,add_special_tokens=False,return_attention_mask=False)["input_ids"]
    model=AutoModelForCausalLM.from_pretrained(model_id,torch_dtype="auto")
    model.eval().to("cpu")
    sums={}; counts={}; handles=[]
    def mk(name):
      def hook(_m,args):
        if not args:return
        x=args[0]
        if not hasattr(x,"shape") or x.shape[-1]<=0:return
        d=x.detach().to(dtype=torch.float32)
        dims=tuple(range(d.ndim-1))
        ss=d.square().sum(dim=dims).cpu().numpy().astype(np.float64,copy=False)
        n=int(d.numel()//d.shape[-1])
        if name not in sums:
          sums[name]=np.array(ss,dtype=np.float64,copy=True); counts[name]=n
        else:
          sums[name]+=ss; counts[name]+=n
      return hook
    mapped=[]
    for module_name,module in model.named_modules():
      gguf_name=hf_module_to_gguf_weight(module_name)
      if gguf_name is None:continue
      handles.append(module.register_forward_pre_hook(mk(gguf_name))); mapped.append((module_name,gguf_name))
    samples=0
    try:
      with torch.no_grad():
        for start in range(0,len(ids),192):
          if samples>=8:break
          chunk=ids[start:start+192]
          if len(chunk)<2:continue
          x=torch.tensor([chunk],dtype=torch.long)
          model(input_ids=x,use_cache=False)
          samples+=1
    finally:
      for h in handles:h.remove()
    stats={name:np.maximum(v/max(counts[name],1),1e-12).astype(np.float32) for name,v in sums.items()}
    np.savez_compressed(output,**stats)
    meta={"model_id":model_id,"samples_run":samples,"captured_tensors":sorted(stats),"vector_counts":counts,"mapped_modules":mapped,
          "corpus_sha256":sha256(corpus.read_bytes()).hexdigest()}
    Path("activation.npz.json").write_text(json.dumps(meta,indent=2),encoding="utf-8")
    print(json.dumps({"samples":samples,"tensors":len(stats),"size":output.stat().st_size},indent=2))
if __name__=="__main__":main()
