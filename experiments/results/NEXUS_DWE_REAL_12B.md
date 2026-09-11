# NEXUS DWE real Mistral-Nemo 12B

Model: `mistralai/Mistral-Nemo-Base-2407` @ `2045759120154383da48ee84ce4bf2f90cc6ec1f`

Elapsed: 43.1s

## Whole-model structural arithmetic

|K|centroid bits|norm bits|size MiB|ratio vs BF16|effective bpw|
|---:|---:|---:|---:|---:|---:|
|16|2|4|9.552|2445.6x|0.00654|
|16|2|8|10.536|2217.2x|0.00722|
|16|16|4|56.857|410.9x|0.03894|
|32|2|4|16.556|1411.0x|0.01134|
|32|2|8|17.540|1331.8x|0.01201|
|32|16|4|111.165|210.1x|0.07614|
|64|2|4|30.318|770.5x|0.02076|
|64|2|8|31.302|746.3x|0.02144|
|64|16|4|219.536|106.4x|0.15036|
|128|2|4|57.595|405.6x|0.03945|
|128|2|8|58.579|398.8x|0.04012|
|128|16|4|436.032|53.6x|0.29864|

## Real-weight distortion — symmetric 2-bit centroids, 4-bit norms

|tensor|K|cos mean|cos p05|NMSE|activation rel L2|index H|std lossless|
|---|---:|---:|---:|---:|---:|---:|---:|
|`model.embed_tokens.weight`|16|0.1856|0.0911|2.5563|1.8149|2.497|1.79x lzma9|
|`model.embed_tokens.weight`|32|0.2514|0.1192|2.5103|1.6045|3.686|1.85x lzma9|
|`model.embed_tokens.weight`|64|0.3266|0.0909|2.5444|1.4269|3.855|1.88x lzma9|
|`model.embed_tokens.weight`|128|0.4861|0.1093|2.5365|1.9389|5.385|1.90x lzma9|
|`model.layers.0.self_attn.q_proj.weight`|16|0.3656|0.2018|5.8731|2.2934|3.886|1.79x lzma9|
|`model.layers.0.self_attn.q_proj.weight`|32|0.4105|0.2573|11.8911|3.8941|4.779|1.86x lzma9|
|`model.layers.0.self_attn.q_proj.weight`|64|0.4691|0.3217|17.6963|4.3117|5.735|1.89x lzma9|
|`model.layers.0.self_attn.q_proj.weight`|128|0.5244|0.4155|36.8776|6.6973|6.689|1.91x lzma9|
|`model.layers.0.mlp.gate_proj.weight`|16|0.1925|0.0743|1.8316|1.1722|3.236|1.80x lzma9|
|`model.layers.0.mlp.gate_proj.weight`|32|0.2563|0.1190|30.8247|4.7356|4.172|1.86x lzma9|
|`model.layers.0.mlp.gate_proj.weight`|64|0.2968|0.0421|4.6784|1.9283|3.371|1.89x lzma9|
|`model.layers.0.mlp.gate_proj.weight`|128|0.4900|0.0837|3.6972|1.8666|5.621|1.90x lzma9|
|`model.layers.10.mlp.down_proj.weight`|16|0.1632|0.0859|4.5274|2.0577|2.975|1.88x lzma9|
|`model.layers.10.mlp.down_proj.weight`|32|0.2135|0.0714|7.9649|2.4577|3.354|1.90x lzma9|
|`model.layers.10.mlp.down_proj.weight`|64|0.2763|0.0752|7.3445|2.4803|3.594|1.91x lzma9|
|`model.layers.10.mlp.down_proj.weight`|128|0.4425|0.0631|17.6432|3.7360|4.834|1.91x lzma9|
|`model.layers.20.self_attn.o_proj.weight`|16|0.1732|0.0657|2.0227|1.3634|3.095|1.76x lzma9|
|`model.layers.20.self_attn.o_proj.weight`|32|0.2258|0.0578|2.6941|1.6437|3.486|1.83x lzma9|
|`model.layers.20.self_attn.o_proj.weight`|64|0.3237|0.0940|6.3597|2.1854|4.624|1.87x lzma9|
|`model.layers.20.self_attn.o_proj.weight`|128|0.4910|0.1326|8.7726|2.7336|5.961|1.90x lzma9|
|`model.layers.20.mlp.up_proj.weight`|16|0.1271|0.0425|4.4085|2.0210|1.658|1.80x lzma9|
|`model.layers.20.mlp.up_proj.weight`|32|0.2113|0.0497|2.6581|1.3776|3.054|1.85x lzma9|
|`model.layers.20.mlp.up_proj.weight`|64|0.3251|0.0828|3.9141|1.8170|4.589|1.89x lzma9|
|`model.layers.20.mlp.up_proj.weight`|128|0.4718|0.0782|8.7033|2.9748|5.492|1.91x lzma9|
|`model.layers.39.self_attn.q_proj.weight`|16|0.2262|0.0959|2.1963|1.4030|3.596|1.77x lzma9|
|`model.layers.39.self_attn.q_proj.weight`|32|0.2499|0.0394|4.7159|2.0666|3.378|1.86x lzma9|
|`model.layers.39.self_attn.q_proj.weight`|64|0.3606|0.0812|6.0246|2.2859|4.713|1.89x lzma9|
|`model.layers.39.self_attn.q_proj.weight`|128|0.5233|0.0983|7.0912|2.7867|5.986|1.91x lzma9|
|`model.layers.39.mlp.down_proj.weight`|16|0.1595|0.0767|5.7739|2.9512|2.897|1.88x lzma9|
|`model.layers.39.mlp.down_proj.weight`|32|0.2024|0.0692|169.3170|12.2947|3.167|1.90x lzma9|
|`model.layers.39.mlp.down_proj.weight`|64|0.3052|0.0951|166.5266|11.0738|4.385|1.91x lzma9|
|`model.layers.39.mlp.down_proj.weight`|128|0.4538|0.0762|19.6579|4.2533|5.324|1.92x lzma9|
|`lm_head.weight`|16|0.3084|0.0939|4.8818|2.1564|2.034|1.84x lzma9|
|`lm_head.weight`|32|0.3425|0.1113|6.8710|2.1780|2.029|1.87x lzma9|
|`lm_head.weight`|64|0.4225|0.1743|13.5040|3.0230|2.534|1.89x lzma9|
|`lm_head.weight`|128|0.5634|0.2269|6.5446|3.4356|4.639|1.91x lzma9|

## Literal pasted 2-bit quantizer control

|tensor|K|cos mean|NMSE|activation rel L2|
|---|---:|---:|---:|---:|
|`model.embed_tokens.weight`|16|0.0665|0.9882|0.9859|
|`model.embed_tokens.weight`|32|0.1124|0.9687|0.9874|
|`model.embed_tokens.weight`|64|0.1953|0.9212|0.9568|
|`model.embed_tokens.weight`|128|0.3310|0.8315|0.9025|
|`model.layers.0.self_attn.q_proj.weight`|16|0.3409|0.8980|0.9502|
|`model.layers.0.self_attn.q_proj.weight`|32|0.3167|0.9217|0.9638|
|`model.layers.0.self_attn.q_proj.weight`|64|0.3275|0.9237|0.9976|
|`model.layers.0.self_attn.q_proj.weight`|128|0.2668|0.9507|1.0086|
|`model.layers.0.mlp.gate_proj.weight`|16|0.0818|0.9877|0.9935|
|`model.layers.0.mlp.gate_proj.weight`|32|0.0107|0.9989|0.9997|
|`model.layers.0.mlp.gate_proj.weight`|64|0.1614|0.9400|0.9907|
|`model.layers.0.mlp.gate_proj.weight`|128|0.3120|0.8629|0.9244|
|`model.layers.10.mlp.down_proj.weight`|16|0.0267|0.9933|0.9918|
|`model.layers.10.mlp.down_proj.weight`|32|0.0485|0.9892|0.9936|
|`model.layers.10.mlp.down_proj.weight`|64|0.1226|0.9533|0.9724|
|`model.layers.10.mlp.down_proj.weight`|128|0.1428|0.9788|0.9985|
|`model.layers.20.self_attn.o_proj.weight`|16|0.0670|0.9888|0.9912|
|`model.layers.20.self_attn.o_proj.weight`|32|0.1017|0.9731|0.9697|
|`model.layers.20.self_attn.o_proj.weight`|64|0.1200|0.9600|0.9885|
|`model.layers.20.self_attn.o_proj.weight`|128|0.2129|0.9397|0.9731|
|`model.layers.20.mlp.up_proj.weight`|16|0.0364|0.9874|0.9966|
|`model.layers.20.mlp.up_proj.weight`|32|0.1011|0.9691|0.9853|
|`model.layers.20.mlp.up_proj.weight`|64|0.1502|0.9442|0.9804|
|`model.layers.20.mlp.up_proj.weight`|128|0.2158|0.9406|0.9592|
|`model.layers.39.self_attn.q_proj.weight`|16|0.0914|0.9895|0.9992|
|`model.layers.39.self_attn.q_proj.weight`|32|0.0877|0.9831|0.9942|
|`model.layers.39.self_attn.q_proj.weight`|64|0.1424|0.9574|0.9849|
|`model.layers.39.self_attn.q_proj.weight`|128|0.2471|0.9237|0.9671|
|`model.layers.39.mlp.down_proj.weight`|16|0.0216|0.9951|0.9942|
|`model.layers.39.mlp.down_proj.weight`|32|0.0024|0.9988|0.9972|
|`model.layers.39.mlp.down_proj.weight`|64|0.0061|0.9974|0.9967|
|`model.layers.39.mlp.down_proj.weight`|128|0.1338|0.9795|0.9799|
|`lm_head.weight`|16|0.0943|0.9874|0.9916|
|`lm_head.weight`|32|0.1162|0.9755|0.9695|
|`lm_head.weight`|64|0.1320|0.9835|1.0073|
|`lm_head.weight`|128|0.2907|0.9153|0.9685|
