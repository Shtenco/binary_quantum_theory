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

## NEXUS_70B_QUANTUM_DIRECT.json
```json
{
  "schema": "shtenco.nexus-70b-vqc/v2",
  "questions": 12,
  "train_questions": 6,
  "test_questions": 6,
  "baseline_train_accuracy": 0.8333333333333334,
  "baseline_test_accuracy": 0.6666666666666666,
  "vqc_train_accuracy": 0.8333333333333334,
  "vqc_test_accuracy": 0.6666666666666666,
  "theta": [
    -0.006261694441332526,
    -0.003388739775402952,
    0.8386342844091446
  ],
  "train_nll": 0.4505794248323163,
  "mean_model_query_seconds": 25.44825856441666,
  "median_model_query_seconds": 25.504672183000025,
  "simulated_2qubit_vqc_overhead_us": 58.9717579500018,
  "note": "Classically simulated 2-qubit post-logit unitary adapter on real A/B/C/D probabilities from a live 70B model; this is not a quantum speedup and not a hidden-state quantum layer.",
  "rows": [
    {
      "q": "2+3=?",
      "p": [
        9.999999999969996e-13,
        0.9999999999969997,
        9.999999999969996e-13,
        9.999999999969996e-13
      ],
      "gold": 1,
      "raw": "B",
      "latency_s": 26.150686098999984
    },
    {
      "q": "Capital of France?",
      "p": [
        9.999999999969998e-13,
        9.999999999969998e-13,
        0.999999999997,
        9.999999999969998e-13
      ],
      "gold": 2,
      "raw": "C",
      "latency_s": 22.502276534999964
    },
    {
      "q": "9*7=?",
      "p": [
        9.999999999969996e-13,
        0.9999999999969997,
        9.999999999969996e-13,
        9.999999999969996e-13
      ],
      "gold": 2,
      "raw": "B",
      "latency_s": 25.725863871
    },
    {
      "q": "Water formula?",
      "p": [
        0.9999999999969997,
        9.999999999969996e-13,
        9.999999999969996e-13,
        9.999999999969996e-13
      ],
      "gold": 0,
      "raw": "A",
      "latency_s": 24.709323047999987
    },
    {
      "q": "sqrt(144)=?",
      "p": [
        9.999999999969998e-13,
        9.999999999969998e-13,
        9.999999999969998e-13,
        0.999999999997
      ],
      "gold": 3,
      "raw": "D",
      "latency_s": 25.219864496000014
    },
    {
      "q": "Binary 1010 in decimal?",
      "p": [
        9.999999999969996e-13,
        0.9999999999969997,
        9.999999999969996e-13,
        9.999999999969996e-13
      ],
      "gold": 1,
      "raw": "B",
      "latency_s": 26.312222300999963
    },
    {
      "q": "Capital of Kazakhstan?",
      "p": [
        9.999999999969996e-13,
        0.9999999999969997,
        9.999999999969996e-13,
        9.999999999969996e-13
      ],
      "gold": 1,
      "raw": "B",
      "latency_s": 26.241826016999994
    },
    {
      "q": "d/dx x^2 = ?",
      "p": [
        9.999999999969996e-13,
        0.9999999999969997,
        9.999999999969996e-13,
        9.999999999969996e-13
      ],
      "gold": 1,
      "raw": "B",
      "latency_s": 27.91976934400003
    },
    {
      "q": "15% of 200?",
      "p": [
        9.999999999969996e-13,
        0.9999999999969997,
        9.999999999969996e-13,
        9.999999999969996e-13
      ],
      "gold": 2,
      "raw": "B",
      "latency_s": 26.12810535
    },
    {
      "q": "Which is prime?",
      "p": [
        9.999999999969998e-13,
        9.999999999969998e-13,
        9.999999999969998e-13,
        0.999999999997
      ],
      "gold": 2,
      "raw": "D",
      "latency_s": 24.616739537999933
    },
    {
      "q": "SI unit of electric current?",
      "p": [
        9.999999999969998e-13,
        9.999999999969998e-13,
        0.999999999997,
        9.999999999969998e-13
      ],
      "gold": 2,
      "raw": "C",
      "latency_s": 24.568945678999967
    },
    {
      "q": "Earth is the ___ planet from the Sun.",
      "p": [
        9.999999999969996e-13,
        0.9999999999969997,
        9.999999999969996e-13,
        9.999999999969996e-13
      ],
      "gold": 1,
      "raw": "B",
      "latency_s": 25.28348049500005
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
	User time (seconds): 247.36
	System time (seconds): 1.16
	Percent of CPU this job got: 250%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 1:39.07
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 15451184
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 9331
	Minor (reclaiming a frame) page faults: 406200
	Voluntary context switches: 56555
	Involuntary context switches: 38615
	Swaps: 0
	File system inputs: 30025864
	File system outputs: 0
	Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0

```

## NEXUS_70B_RSS_DIRECT.txt
```text
VmHWM:	15501440 kB
VmRSS:	15386400 kB

```

## NEXUS_70B_SERVER_DIRECT.log
```text
s per second)
1.03.124.273 I slot print_timing: id  2 | task 2 |        eval time =       0.00 ms /     1 tokens (    0.00 ms per token,     0.00 tokens per second)
1.03.124.274 I slot print_timing: id  2 | task 2 |       total time =   22464.83 ms /    30 tokens
1.03.124.275 I slot print_timing: id  2 | task 2 |    graphs reused =          1
1.03.125.308 I slot      release: id  2 | task 2 | stop processing: n_tokens = 29, truncated = 0
1.03.128.943 I slot get_availabl: id  1 | task -1 | selected slot by LRU, t_last = -1
1.03.128.982 I slot launch_slot_: id  1 | task 4 | processing task, is_child = 0
1.28.850.804 I slot print_timing: id  1 | task 4 | prompt eval time =   25716.94 ms /    34 tokens (  756.38 ms per token,     1.32 tokens per second)
1.28.850.817 I slot print_timing: id  1 | task 4 |        eval time =       0.00 ms /     1 tokens (    0.00 ms per token,     0.00 tokens per second)
1.28.850.818 I slot print_timing: id  1 | task 4 |       total time =   25716.94 ms /    35 tokens
1.28.850.819 I slot print_timing: id  1 | task 4 |    graphs reused =          1
1.28.851.268 I slot      release: id  1 | task 4 | stop processing: n_tokens = 34, truncated = 0
1.28.859.753 I slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = -1
1.28.859.789 I slot launch_slot_: id  0 | task 6 | processing task, is_child = 0
1.53.559.932 I slot print_timing: id  0 | task 6 | prompt eval time =   24697.55 ms /    33 tokens (  748.41 ms per token,     1.34 tokens per second)
1.53.559.949 I slot print_timing: id  0 | task 6 |        eval time =       0.00 ms /     1 tokens (    0.00 ms per token,     0.00 tokens per second)
1.53.559.950 I slot print_timing: id  0 | task 6 |       total time =   24697.56 ms /    34 tokens
1.53.559.953 I slot print_timing: id  0 | task 6 |    graphs reused =          1
1.53.560.762 I slot      release: id  0 | task 6 | stop processing: n_tokens = 33, truncated = 0
1.53.566.795 I slot get_availabl: id  3 | task -1 | selected slot by LRU, t_last = 287030605
1.53.566.857 I slot launch_slot_: id  3 | task 8 | processing task, is_child = 0
2.18.779.857 I slot print_timing: id  3 | task 8 | prompt eval time =   25211.27 ms /    34 tokens (  741.51 ms per token,     1.35 tokens per second)
2.18.779.867 I slot print_timing: id  3 | task 8 |        eval time =       0.00 ms /     1 tokens (    0.00 ms per token,     0.00 tokens per second)
2.18.779.868 I slot print_timing: id  3 | task 8 |       total time =   25211.27 ms /    35 tokens
2.18.779.869 I slot print_timing: id  3 | task 8 |    graphs reused =          1
2.18.780.698 I slot      release: id  3 | task 8 | stop processing: n_tokens = 34, truncated = 0
2.18.784.959 I slot get_availabl: id  2 | task -1 | selected slot by LRU, t_last = 309535485
2.18.785.017 I slot launch_slot_: id  2 | task 10 | processing task, is_child = 0
2.45.092.506 I slot print_timing: id  2 | task 10 | prompt eval time =   26301.11 ms /    36 tokens (  730.59 ms per token,     1.37 tokens per second)
2.45.092.518 I slot print_timing: id  2 | task 10 |        eval time =       0.00 ms /     1 tokens (    0.00 ms per token,     0.00 tokens per second)
2.45.092.519 I slot print_timing: id  2 | task 10 |       total time =   26301.11 ms /    37 tokens
2.45.092.520 I slot print_timing: id  2 | task 10 |    graphs reused =          1
2.45.093.031 I slot      release: id  2 | task 10 | stop processing: n_tokens = 36, truncated = 0
2.45.117.174 I slot get_availabl: id  1 | task -1 | selected slot by LRU, t_last = 335261447
2.45.117.218 I slot launch_slot_: id  1 | task 12 | processing task, is_child = 0
3.11.333.554 I slot print_timing: id  1 | task 12 | prompt eval time =   26214.30 ms /    36 tokens (  728.17 ms per token,     1.37 tokens per second)
3.11.333.566 I slot print_timing: id  1 | task 12 |        eval time =       0.00 ms /     1 tokens (    0.00 ms per token,     0.00 tokens per second)
3.11.333.567 I slot print_timing: id  1 | task 12 |       total time =   26214.30 ms /    37 tokens
3.11.333.568 I slot print_timing: id  1 | task 12 |    graphs reused =          2
3.11.334.950 I slot      release: id  1 | task 12 | stop processing: n_tokens = 36, truncated = 0
3.11.340.979 I slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 359970943
3.11.341.018 I slot launch_slot_: id  0 | task 14 | processing task, is_child = 0
3.39.254.501 I slot print_timing: id  0 | task 14 | prompt eval time =   27912.18 ms /    38 tokens (  734.53 ms per token,     1.36 tokens per second)
3.39.254.513 I slot print_timing: id  0 | task 14 |        eval time =       0.00 ms /     1 tokens (    0.00 ms per token,     0.00 tokens per second)
3.39.254.514 I slot print_timing: id  0 | task 14 |       total time =   27912.18 ms /    39 tokens
3.39.254.515 I slot print_timing: id  0 | task 14 |    graphs reused =          2
3.39.254.756 I slot      release: id  0 | task 14 | stop processing: n_tokens = 38, truncated = 0
3.39.258.367 I slot get_availabl: id  3 | task -1 | selected slot by LRU, t_last = 385190877
3.39.258.405 I slot launch_slot_: id  3 | task 16 | processing task, is_child = 0
4.05.382.957 I slot print_timing: id  3 | task 16 | prompt eval time =   26119.78 ms /    35 tokens (  746.28 ms per token,     1.34 tokens per second)
4.05.382.967 I slot print_timing: id  3 | task 16 |        eval time =       0.00 ms /     1 tokens (    0.00 ms per token,     0.00 tokens per second)
4.05.382.968 I slot print_timing: id  3 | task 16 |       total time =   26119.79 ms /    36 tokens
4.05.382.969 I slot print_timing: id  3 | task 16 |    graphs reused =          2
4.05.383.267 I slot      release: id  3 | task 16 | stop processing: n_tokens = 35, truncated = 0
4.05.387.093 I slot get_availabl: id  2 | task -1 | selected slot by LRU, t_last = 411503208
4.05.387.133 I slot launch_slot_: id  2 | task 18 | processing task, is_child = 0
4.29.999.215 I slot print_timing: id  2 | task 18 | prompt eval time =   24610.49 ms /    33 tokens (  745.77 ms per token,     1.34 tokens per second)
4.29.999.224 I slot print_timing: id  2 | task 18 |        eval time =       0.00 ms /     1 tokens (    0.00 ms per token,     0.00 tokens per second)
4.29.999.225 I slot print_timing: id  2 | task 18 |       total time =   24610.49 ms /    34 tokens
4.29.999.226 I slot print_timing: id  2 | task 18 |    graphs reused =          2
4.29.999.822 I slot      release: id  2 | task 18 | stop processing: n_tokens = 33, truncated = 0
4.30.011.689 I slot get_availabl: id  1 | task -1 | selected slot by LRU, t_last = 437745130
4.30.011.735 I slot launch_slot_: id  1 | task 20 | processing task, is_child = 0
4.54.567.616 I slot print_timing: id  1 | task 20 | prompt eval time =   24554.16 ms /    33 tokens (  744.07 ms per token,     1.34 tokens per second)
4.54.567.625 I slot print_timing: id  1 | task 20 |        eval time =       0.00 ms /     1 tokens (    0.00 ms per token,     0.00 tokens per second)
4.54.567.626 I slot print_timing: id  1 | task 20 |       total time =   24554.16 ms /    34 tokens
4.54.567.627 I slot print_timing: id  1 | task 20 |    graphs reused =          3
4.54.568.952 I slot      release: id  1 | task 20 | stop processing: n_tokens = 33, truncated = 0
4.54.575.254 I slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = 465664933
4.54.575.293 I slot launch_slot_: id  0 | task 22 | processing task, is_child = 0
5.19.851.564 I slot print_timing: id  0 | task 22 | prompt eval time =   25274.10 ms /    34 tokens (  743.36 ms per token,     1.35 tokens per second)
5.19.851.573 I slot print_timing: id  0 | task 22 |        eval time =       0.00 ms /     1 tokens (    0.00 ms per token,     0.00 tokens per second)
5.19.851.574 I slot print_timing: id  0 | task 22 |       total time =   25274.11 ms /    35 tokens
5.19.851.575 I slot print_timing: id  0 | task 22 |    graphs reused =          3
5.19.852.364 I slot      release: id  0 | task 22 | stop processing: n_tokens = 34, truncated = 0

```
