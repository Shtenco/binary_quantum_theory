# NEXUS 70B DIRECT evidence

## NEXUS_70B_MODEL_DIRECT.json
```json
{
  "repo": "mradermacher/Llama-3.3-70B-Instruct-i1-GGUF",
  "files": [
    "Llama-3.3-70B-Instruct.i1-IQ1_S.gguf"
  ],
  "bytes": 15343488384
}
```

## NEXUS_70B_STORAGE_DIRECT.json
```json
{
  "model_bytes": 15343488384,
  "mean_ratio": 1.2226598072125294,
  "rows": [
    {
      "offset": 0,
      "raw": 8388608,
      "compressed": 3050390,
      "ratio": 2.7500116378561428
    },
    {
      "offset": 2190728539,
      "raw": 8388608,
      "compressed": 8228368,
      "ratio": 1.0194740925539547
    },
    {
      "offset": 4381457078,
      "raw": 8388608,
      "compressed": 8300838,
      "ratio": 1.0105736312406048
    },
    {
      "offset": 6572185618,
      "raw": 8388608,
      "compressed": 8368452,
      "ratio": 1.0024085697091887
    },
    {
      "offset": 8762914157,
      "raw": 8388608,
      "compressed": 8391143,
      "ratio": 0.9996978957455498
    },
    {
      "offset": 10953642697,
      "raw": 8388608,
      "compressed": 8391155,
      "ratio": 0.9996964661003164
    },
    {
      "offset": 13144371236,
      "raw": 8388608,
      "compressed": 8391164,
      "ratio": 0.9996953938690747
    },
    {
      "offset": 15335099776,
      "raw": 8388608,
      "compressed": 8390951,
      "ratio": 0.9997207706254034
    }
  ]
}
```

## NEXUS_70B_BENCH_DIRECT.txt
```text
load_backend: loaded RPC backend from /tmp/llama-bin/llama-b10809/libggml-rpc.so
load_backend: loaded CPU backend from /tmp/llama-bin/llama-b10809/libggml-cpu-haswell.so
| model                          |       size |     params | backend    | threads |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | ------: | --------------: | -------------------: |
| llama 70B IQ1_S - 1.5625 bpw   |  14.28 GiB |    70.55 B | CPU        |       4 |            pp32 |          1.30 ± 0.00 |
| llama 70B IQ1_S - 1.5625 bpw   |  14.28 GiB |    70.55 B | CPU        |       4 |             tg4 |          0.39 ± 0.00 |

build: 5266f24da (10809)
	Command being timed: "llama-bench -m models/Llama-3.3-70B-Instruct.i1-IQ1_S.gguf -p 32 -n 4 -r 1 -t 4"
	User time (seconds): 249.80
	System time (seconds): 1.22
	Percent of CPU this job got: 251%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 1:39.70
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 15463120
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 8302
	Minor (reclaiming a frame) page faults: 402595
	Voluntary context switches: 51430
	Involuntary context switches: 40176
	Swaps: 0
	File system inputs: 29896592
	File system outputs: 0
	Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0

```

## NEXUS_70B_SERVER_DIRECT.log
```text
0.00.028.537 I cmn  common_param: common_params_print_info: verbosity = 3 (adjust with the `-lv N` CLI arg)
0.00.030.258 W srv  llama_server: -----------------
0.00.030.267 W srv  llama_server: CORS is set to allow all origins ('*') and no API key is set
0.00.030.268 W srv  llama_server: this can be a security risk (cross-origin attacks)
0.00.030.268 W srv  llama_server: more info: https://github.com/ggml-org/llama.cpp/pull/25655
0.00.030.268 W srv  llama_server: -----------------
0.00.032.019 I srv    load_model: loading model 'models/Llama-3.3-70B-Instruct.i1-IQ1_S.gguf'
0.02.349.088 I cmn          init: llama threadpool init, n_threads = 4
0.13.105.055 I srv    load_model: initializing, n_slots = 4, n_ctx_slot = 256, kv_unified = 'true'
0.13.128.055 I srv  llama_server: model loaded
0.13.128.068 I srv  llama_server: listening on http://127.0.0.1:8080
0.13.128.069 W srv  llama_server: NOTICE: server default port will be changed to :9931 in a future release
0.13.128.070 W srv  llama_server:         ref: https://github.com/ggml-org/llama.cpp/pull/26508
0.14.193.402 I slot get_availabl: id  3 | task -1 | selected slot by LRU, t_last = -1
parse: error parsing grammar: expecting newline or end at \"A\" | \"B\" | \"C\" | \"D\"

root ::= \"A\" | \"B\" | \"C\" | \"D\"
0.14.195.467 E failed to parse grammar
0.14.196.251 E srv    send_error: task id = 0, error: Failed to initialize samplers: failed to parse grammar
0.14.196.270 E srv  process_sing: failed to launch slot with task, id_task = 0
0.14.196.441 W srv          stop: cancel task, id_task = 0

```
