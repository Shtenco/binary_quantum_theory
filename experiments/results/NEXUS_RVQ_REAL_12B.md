# NEXUS block PQ / residual VQ on real Mistral-Nemo 12B

Elapsed: 21.5s

## Whole-model size arithmetic

|config|block|stages|MiB|GiB|effective bpw|ratio vs BF16|
|---|---:|---:|---:|---:|---:|---:|
|PQ8x1|8|1|2191.5|2.140|1.501|10.7x|
|PQ16x1|16|1|1097.1|1.071|0.751|21.3x|
|RVQ16x2|16|2|2193.3|2.142|1.502|10.7x|
|RVQ32x2|32|2|1100.5|1.075|0.754|21.2x|
|RVQ64x2|64|2|557.5|0.544|0.382|41.9x|

## Real-weight local quality

|tensor|config|cos mean|cos p05|NMSE|activation rel L2|index entropy/stage|lossless|
|---|---|---:|---:|---:|---:|---|---|
|`model.embed_tokens.weight`|PQ8x1|0.8469|0.8437|0.2828|0.5602|7.99|1.08x lzma9|
|`model.embed_tokens.weight`|PQ16x1|0.6691|0.6634|0.5524|0.7225|7.99|1.09x lzma9|
|`model.embed_tokens.weight`|RVQ16x2|0.8334|0.8299|0.3054|0.5364|7.99,7.99|1.10x lzma9|
|`model.embed_tokens.weight`|RVQ32x2|0.6847|0.6782|0.5311|0.6944|7.94,7.97|1.12x lzma9|
|`model.embed_tokens.weight`|RVQ64x2|0.5587|0.5426|0.6879|0.8318|7.60,7.59|1.11x lzma9|
|`model.layers.0.self_attn.q_proj.weight`|PQ8x1|0.9106|0.8997|0.1684|0.4265|7.76|1.16x lzma9|
|`model.layers.0.self_attn.q_proj.weight`|PQ16x1|0.7682|0.7432|0.4052|0.6249|7.91|1.14x lzma9|
|`model.layers.0.self_attn.q_proj.weight`|RVQ16x2|0.8953|0.8818|0.1957|0.5086|7.89,7.93|1.10x lzma9|
|`model.layers.0.self_attn.q_proj.weight`|RVQ32x2|0.7744|0.7399|0.3945|0.6799|7.74,7.89|1.15x lzma9|
|`model.layers.0.self_attn.q_proj.weight`|RVQ64x2|0.6857|0.6016|0.5184|0.7246|7.74,7.72|1.22x lzma9|
|`model.layers.0.mlp.gate_proj.weight`|PQ8x1|0.8475|0.8440|0.2818|0.5344|7.99|1.06x zlib9|
|`model.layers.0.mlp.gate_proj.weight`|PQ16x1|0.6701|0.6625|0.5511|0.7410|7.99|1.05x zlib9|
|`model.layers.0.mlp.gate_proj.weight`|RVQ16x2|0.8340|0.8301|0.3045|0.5728|7.99,7.99|1.05x lzma9|
|`model.layers.0.mlp.gate_proj.weight`|RVQ32x2|0.6867|0.6798|0.5284|0.7692|7.97,7.97|1.06x lzma9|
|`model.layers.0.mlp.gate_proj.weight`|RVQ64x2|0.5587|0.5441|0.6877|0.8303|7.58,7.62|1.09x lzma9|
|`model.layers.20.mlp.up_proj.weight`|PQ8x1|0.8473|0.8441|0.2822|0.5188|7.99|1.06x lzma9|
|`model.layers.20.mlp.up_proj.weight`|PQ16x1|0.6691|0.6634|0.5524|0.7673|7.99|1.05x zlib9|
|`model.layers.20.mlp.up_proj.weight`|RVQ16x2|0.8338|0.8299|0.3047|0.5325|7.99,7.99|1.05x zlib9|
|`model.layers.20.mlp.up_proj.weight`|RVQ32x2|0.6852|0.6781|0.5305|0.7409|7.96,7.96|1.05x lzma9|
|`model.layers.20.mlp.up_proj.weight`|RVQ64x2|0.5583|0.5439|0.6881|0.8332|7.65,7.59|1.09x lzma9|
|`model.layers.39.mlp.down_proj.weight`|PQ8x1|0.8459|0.8441|0.2849|0.5200|7.99|1.07x lzma9|
|`model.layers.39.mlp.down_proj.weight`|PQ16x1|0.6626|0.6585|0.5606|0.7294|7.99|1.08x lzma9|
|`model.layers.39.mlp.down_proj.weight`|RVQ16x2|0.8270|0.8245|0.3161|0.5850|7.99,7.99|1.07x lzma9|
|`model.layers.39.mlp.down_proj.weight`|RVQ32x2|0.6620|0.6575|0.5616|0.7350|7.99,7.98|1.09x lzma9|
|`model.layers.39.mlp.down_proj.weight`|RVQ64x2|0.5180|0.5113|0.7315|0.8611|7.76,7.76|1.09x lzma9|
