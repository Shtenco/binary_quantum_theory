# BQG repository audit — 2026-10-22

## Scope and reproducibility boundary

Repository: https://github.com/Shtenco/binary_quantum_theory
Default branch: main
Audited main HEAD: `1b88780157ed602c1954528cc685241384d25deb` (2026-10-19).
Recursive tree response: 611 tracked files, 20 directories; truncated=false.

This is a remote evidence audit, not a claim that every script was executed locally. GitHub Actions results are historical CI evidence. The current chat runtime did not check out the repository and execute the full test suite. No numerical result is upgraded from a historical log to a fresh reproduction.

## Inventory of files on main

Extensions: md: 192; py: 181; pkl: 77; json: 68; log: 43; yml: 31; zip: 8; txt: 6; npz: 2; [без расширения]: 1; tsv: 1; cpp: 1.

Top-level path counts: [корень]: 185; scripts: 160; docs: 142; research: 91; .github: 28; proof_tools: 2; tests: 2; tools: 1.

Tracked artifacts include 181 Python files, 192 Markdown documents, 68 JSON ledgers, 77 pickle files, 43 logs, 8 ZIP files, 2 NPZ files, 31 workflow YAMLs, 2 tests, and one C++ source. Pickle files must be loaded only from a trusted checkout.

## All branch refs and HEAD commits

Count returned by GitHub API pagination: 139.

| Branch | HEAD SHA |
|---|---|
| `audit/active-habitat-master-v1` | `43f8d00ea237e2123ec07d88c1aa2d3d91f683e2` |
| `audit/active-habitat-master-v2-preregistered` | `9ae7c06d4660061a62bfde4fd5136010dcff9fd5` |
| `audit/active-habitat-master-v2` | `4f3c9ccc67c14e892744b30a9f2736f2fc4576aa` |
| `audit/bell-chsh-gate` | `de0b56710f3892f566ece0e6ea31030a50c2dfaf` |
| `audit/current-status-2026-10-10` | `ac1a07a27c2acc9231d2d42ffcbbed9799afb426` |
| `audit/k5-s5-carrier-symmetry` | `5a4685d2f73453790f554cf3f5cd75275c6458bb` |
| `audit/k5-s5-hamiltonian-covariance-v1` | `f683df8f9d80c6654dab8e99c3c8946c586c7401` |
| `audit/loc-2026-09-15` | `4fc5634ebed3b5e29318bef90f23e5006a50bb31` |
| `audit/physicalization-truth-v3` | `e5ae681bbaed3bdb53d82a7f9d6b51cf3707da9b` |
| `audit/q4-k5-local-carrier-bridge` | `d9683ce796b3e05dc9c1c83d16790db7ec6f946c` |
| `audit/q4-s4-background-obstruction` | `14d9088c5674d320801979f24af72e45375c5851` |
| `audit/spectral-history-closure-2026-09-06` | `c19de5df420e84ae7125b67cea4bef5a9dc37536` |
| `bqg/depth6-32-canonical-recovery` | `de4391fa616883fc2576636adcc6aaae98da80d0` |
| `ci-sinergy-messenger-v02-native-build` | `4a6bdf75b1403333b27600d4af9bc510b7bbadd0` |
| `ci-sinergy-messenger-v030` | `6c4fd254530fea3b70d2c7fec15711ccb1caedc3` |
| `ci-sinergy-messenger-v033-diagnostic` | `931faff5906ea13ce2b2ada9b269f2c10ca18a94` |
| `ci-sinergy-messenger-v033-functional-final` | `412517dc6a6fecf2b58ba6203972df2c62d5f007` |
| `cleanup/gr-qm-bit-continuum` | `91f4dbf7cd61d851426198db4d38afc743db4c98` |
| `codex` | `486036ab8fdaa0901c5461ec8bda8418df34ab09` |
| `codex-3g4lb0` | `344659a4976b77c9cd85d84e8fa1f10f03769cfc` |
| `codex-4bua2u` | `11012b7abe75ba881125a793885327f03a1e9b59` |
| `codex-4ni6ut` | `ba7e6cedc3bd7b356e3f353227fef5795c336027` |
| `codex-5uocfq` | `de7d0be18ebc49349738b8191e8976b05809edc3` |
| `codex-89btph` | `fd4f13017d698b5ac92517c6c08b9f5726cfe34e` |
| `codex-bwhfkc` | `2b861a419623dd46c91b06b4a58eb104c4fd5366` |
| `codex-e0ee6e` | `6c0badce8a9d407d9f3244351866913ec5486dfc` |
| `codex-hobdxi` | `be5d5fba10868e4e1b613813494e19943354059c` |
| `codex-kpnzg2` | `770d156d5985a1c5d355ae62708fb231c24318a0` |
| `codex-lppw5h` | `b46883f229c5870135720a485c161bf30ae87e9c` |
| `codex-qgjhgi` | `a0b2b9b7b9a961a92abeea9e90868ef13737fa30` |
| `codex-ro2602` | `f6155c3abe030a2564e0402306baad1f5b9f253a` |
| `codex-sjothi` | `a29288ede4363534124c9ef1630b5b06648c912d` |
| `codex-va54l6` | `616d4e7f240b8cc184041ac7497852f03ae4c683` |
| `codex-vbnn2h` | `2bece049421c96e5e4e1aefef6a45b57ea5a190d` |
| `codex-yn178z` | `1c0138c6309531c31984beab5e3565fdb2ef60fe` |
| `exp/iq1s70b-vs-qwen3-14b-20260923` | `326b53733b688c079ae983f7f4936102f82b112b` |
| `exp/nexus-70b-runtime` | `326b53733b688c079ae983f7f4936102f82b112b` |
| `exp/nexus-dwe-real-12b` | `32e28947dc586c44652bec0d68f98605a62a6a52` |
| `exp/plain-llama-portable` | `120f596f652fb5a70e28a10605f0884af59134f2` |
| `exp/qwen15-local-courier` | `42c71612967fdaf3409ac5ddfd390ec7b0189589` |
| `exp/qwen15b-q8-courier` | `ecd0b20ca7affc5e424e7f113a5b273ba73c6c3a` |
| `exp/qwen-activation-calibration` | `213c7a6e6443625f57cb8c727500aaaeddbdd4a5` |
| `exp/qwen-chunks` | `952b6524633773d6c4dfd674036c044f3d0f2d8b` |
| `exp/qwen-f16-courier` | `ae1025b29150293d0b98ce9d970346883bfede52` |
| `exp/qwen-local-courier` | `b59f4bb4031338f9f6d7d5c97c5123deb77da984` |
| `federation-v3-domain-expansion` | `101be6105e1bee9c3e6d662b451d72af2350e827` |
| `final-squash-base` | `c40b091513cd3c73b14bbcaaa80bc12d861da7f3` |
| `hodge-spectral-dimension-notation-fix` | `7f01e41120f001b51a933d4d6aae27010e908e05` |
| `main` | `1b88780157ed602c1954528cc685241384d25deb` |
| `migration/synergy-723-2026-09` | `63ee28fb16dc303344928b5a75fcae2a068055be` |
| `nexus-r74-phi-fix-run` | `cfe01691b8541b3963fe220cea254fef5cae4a32` |
| `nexus-r74-public-run-20260818` | `9e660e61d55d316d09508f900adce0807936b34c` |
| `nexus-r74-qwen-instruct-run` | `39585d2b152790579e6e8b9a608939c9e3acc8dc` |
| `nexus-r74-structured-five-run` | `52ec9e5161024119f276f79c96162012f796ba8d` |
| `physical-tt-kernel-leading-ir` | `e3118e1a710b83d23622af57d9c41ed66d7da2c4` |
| `recovery/bqg-physical-spectral-history-2026-09-06` | `4cb8ae20b72768d556973361820edb1e3137ae05` |
| `release/canonical-theory-package-v1` | `934ead3ebdcdc93b4adbc11bca08ca46f6325570` |
| `research/bcqg-core-candidate-v1` | `2b2c9f623544f5d38f7ffd7f37617f91f4dae306` |
| `research/bqg-2t-algebra` | `b03bf253a43a92e0adda6c18ee3def5fe534b7da` |
| `research/bqg-2t-algebra2` | `b03bf253a43a92e0adda6c18ee3def5fe534b7da` |
| `research/bqg-2t-gate` | `b03bf253a43a92e0adda6c18ee3def5fe534b7da` |
| `research/bqg-2t-gate-final` | `b03bf253a43a92e0adda6c18ee3def5fe534b7da` |
| `research/bqg-2t-gate-final2` | `b03bf253a43a92e0adda6c18ee3def5fe534b7da` |
| `research/bqg-2t-gate-v2` | `b03bf253a43a92e0adda6c18ee3def5fe534b7da` |
| `research/bqg-2t-gate-v3` | `b03bf253a43a92e0adda6c18ee3def5fe534b7da` |
| `research/bqg-2t-gate-v4` | `b03bf253a43a92e0adda6c18ee3def5fe534b7da` |
| `research/bqg-2t-gate-v5` | `b03bf253a43a92e0adda6c18ee3def5fe534b7da` |
| `research/bqg-2t-gate-work` | `b03bf253a43a92e0adda6c18ee3def5fe534b7da` |
| `research/bqg-bell-volume-20261012` | `80d519240f9f4e68df77a7a28742e1a943b37f15` |
| `research/bqg-hda-minimal-no-go-20261012` | `ae74e72035fd97c01b1f3399365bfd865ce95617` |
| `research/canonical-frontier-v2` | `73287ef611096c01c1673ac894ff44ffb1a38066` |
| `research/canonical-ledger-2026-08-15` | `1f754a7060653746e13da05cc8c76261665379f9` |
| `research/canonical-lorentzian-frontier` | `4c51657a7cdc2a758b67a44f0b5c641a10350d50` |
| `research/canonical-prefactor-audit` | `e68a226bfa4638d82e169e4b2a7dbb4645dda349` |
| `research/depth6-s4sign-proof` | `887e76fba5210524650002da0b54653d2c5b37fd` |
| `research/first-q2-scalar-effective-action` | `6c63f0d8734d7bc67d1ca6e462e1ba05956b8db5` |
| `research/hl-sine-dag` | `299e3d896a7845688ca6f3e7cb6c4b379c6a73f1` |
| `research/k5-covariance-hda` | `af16606ecb1358a246574ba3a1406e15f9b5c8fa` |
| `research/logical-s4-sign-twirl` | `e40011f66d9779eda82bca2584229128ab3a76f2` |
| `research/lorentzian-composition-fast` | `7abcaba66567fd09ec533c0c2a170b7d560e2b9a` |
| `research/lorentzian-ordered-triple-fast` | `5cdf421c8f662db620b762328bec6d9228c7d7b4` |
| `research/micro-hda-joint-prediction` | `c5aade6763fdd1bd41717f93037231fcba2de99c` |
| `research/mirror-anisotropy-audit-v2` | `11a0775ce11fddc5cf28680bb24d1f4cc609774d` |
| `research/mirror-orientation-eta` | `7710fc5f2b2b93eebfc2ff72552ff853398a88f4` |
| `research/modular-complex-arithmetic-bridge` | `6dad7a4fb05ed8b80540fa610c884d05e1af5563` |
| `research/operator-micro-dynamics` | `ad37059d0f478ff9bfda57a157d538399f39318a` |
| `research/physical-cosmology-interference-lensing` | `185bee58de27b053497e2a28eaf45c66b1470540` |
| `research/physical-pole-universality` | `b46dbad39e4c9b3de08a45742604d0a9cb973fec` |
| `research/physical-scalar-kernel-dynamics` | `ab24171a4bb327d190551bdf68957bd10a819c1d` |
| `research/physicalization-l1-depth2-metric` | `f06b18f3a9af995d0e7987b323359631945a9394` |
| `research/physicalization-scale-observable-prediction` | `c2a3ee8e30ab449ef23b0cd60fac3db1a0285631` |
| `research/post-hda-physicalization-v2` | `6d3f23860fc134ec0f10259fa17adb2c32588739` |
| `research/pw-lorentzian-24-collector` | `f7f28882d02339b9ed3703c02634ad526c2d1f1b` |
| `research/pw-lorentzian-24-mitm` | `4d72abf7fd0f88c3d9113138eca0b06d264ef2c3` |
| `research/pw-lorentzian-component-fast` | `4d7676a0e153145d34e35b215356528eb8629f04` |
| `research/pw-lorentzian-component-mitm` | `fe117390f4b3b567241084ed945fcb7d3166751e` |
| `research/pw-lorentzian-envtrace` | `7a44506a3b17a341381a720ac27eae78b81e27b0` |
| `research/pw-lorentzian-envtrace-orbit` | `ed0949bee6f7e21658f3ef054b9f23d6f167c611` |
| `research/pw-lorentzian-logical-projection` | `651dd9003cb15b8fd57d4b7c31f7c3a70d9bb49b` |
| `research/pw-lorentzian-lowcut-scout` | `0559c1122070a8eb72885fa8214bf2ba7f1be320` |
| `research/pw-lorentzian-mitm` | `2d05ca59f920d78d926a7f78020a69f6c1326e81` |
| `research/pw-lorentzian-parity` | `cf968d788c2b7aac93d468516cd81695a2feff1b` |
| `research/pw-lorentzian-single-mitm` | `71e807cfedcd38085ebd1801293428ba5701f098` |
| `research/pw-lorentzian-single-probe` | `8d4d697d613a05334f2f346dedd68771e0460318` |
| `research/pw-lorentzian-ultralow-scout` | `e0322ee01558510b0aaf922936a93520488b5360` |
| `research/pw-master-32` | `87aee1e6005fa33d1aa2a1361207218088ed0d1c` |
| `research/pw-spin-parity-master` | `3462cb5ee7c802b45d83577ef875877bc5964231` |
| `research/q2-face-incidence-bridge` | `6a32a784dfbdc47ffa20248232713a92fd9b90ee` |
| `research/q2-gravity-gyc-amplitude` | `ae748aa16c3569d0fe16351150ee33de6bb63ab4` |
| `research/q2-gravity-gyc-sign-twirl` | `494fd514d2d46ee89b487e9b3d506579a9539831` |
| `research/q2-history-directed-laplacian-factorization` | `69d30ce243b79e89151a48888d02342f8897f0b9` |
| `research/q2-history-fourier-complex-structure` | `1a580b434391da0c884d640930ed1b67971c4613` |
| `research/q2-history-gravity-orientation-current` | `5ba4bc24230c3d0a1e47bf309453a692601ee49d` |
| `research/q2-history-phase-refinement-winding` | `d52496c73c76b8fec0e7b4021ef9a852503bc690` |
| `research/q2-orientation-intrinsic-metric-nogo` | `115d308433254b3b32440e3497df259533930b9d` |
| `research/q2-oriented-flux-history-observable` | `ce33520f0c1bdd9985661bb9be086a463de87e9f` |
| `research/q2-relational-history-projector` | `fbdf2ef66d3f28be9ee9c03c0cd479af4459e5c3` |
| `research/q2-relational-metric-source` | `4c5053a002d4acd380a5911413cc4a76697fa87c` |
| `research/q2-unified-complex-structure` | `83f45dfc19cdef884e5290f111bf46dc0e10d1e7` |
| `research/scalar-adm-physical-response` | `4833af3f878a18c2179cdb560fa9b22d9ad941c8` |
| `research/sine-kkv-next` | `9066d572b456f139939d180b7e3cbc2a5a64b514` |
| `research/v12-gauge-dressed-nucleation-20261015` | `d1a4648187d063c464d8fd51558b45afbfff39dc` |
| `research/v13-k5-leakage-safe-master-20261015` | `2cd4813005356302d8d66f8767b264b908b99d4e` |
| `research/v14-k5-first-real-columns-20261015` | `ce43cabf260d3bb937f4de0bf03d685247c83d41` |
| `research/v15-k5-32input-rank-audit-20261015` | `bc172ff2b4b823d2f33af61ab11be6da37221267` |
| `research/v16-full-initial-k5-and-first-shell-20261015` | `95fa4040df6ac71566f111adf89eebb3ab5b74e5` |
| `research/v17-k5-parity-shell-selection-20261015` | `330236f88c9e5734d67b123330190088c4dfecdd` |
| `research/v18-k5-parity-feshbach-20261015` | `2c59b1e03fd7404685db29547fd6b9da3ede575a` |
| `research/v19-canonical-k5-replay-20261015` | `1a715e22d10bb27b2d7c7b6529ac53c59092a851` |
| `research/v20-160-canonical-k5-20261015` | `1a715e22d10bb27b2d7c7b6529ac53c59092a851` |
| `research/v20-complete-160-canonical-20261015` | `f3ce62cfd9199201dd3ff1025846600cfb75c72d` |
| `research/v21-first-shell-checkpoints-20261015` | `085e7b8aa152191a2323803fceecb8565a353880` |
| `research/v22-k5-kernel-ritz-cutoff-20261016` | `35056f1b7eebc89840606529164dfd083e1e5f1e` |
| `research/v23-unified-proof-bridge-20261016` | `c0df55a10937d6545616a44593a6e060cb21d513` |
| `research/v24-crossscale-multiplicity-obstruction-20261016` | `e3eb71e898f4b638d32cdc19b2c3e5ba2f97db52` |
| `research/v25-ancilla-crossscale-k5-20261016` | `45d7ba89facf7c0ad17ddb2359c26bb00f6e6eb5` |
| `research/v26-graph-sector-output-obstruction-20261016` | `456aa7c477c022b87ba1a09d1d0397c67506645c` |
| `research/zeroaware-volume-migration` | `042baa6e87b2a0340511cf083c974042c89b848b` |
| `spectral-history-closure` | `306eaccf4f6416438271eb69eeb72ff2ea6959ae` |

## Branch comparison sample against main

Comparisons below use GitHub compare API; ahead/behind are commit graph counts, and changed-file counts may be omitted by GitHub for large comparisons.

| Branch | Status | Ahead | Behind | Commits | Changed files returned |
|---|---:|---:|---:|---:|---:|
| `audit/physicalization-truth-v3` | behind | 0 | 232 | 0 | 0 |
| `bqg/depth6-32-canonical-recovery` | diverged | 92 | 149 | 92 | 55 |
| `physical-tt-kernel-leading-ir` | diverged | 26 | 228 | 26 | 9 |
| `research/v26-graph-sector-output-obstruction-20261016` | diverged | 4 | 1 | 4 | 4 |
| `research/v25-ancilla-crossscale-k5-20261016` | diverged | 2 | 1 | 2 | 2 |
| `research/v20-complete-160-canonical-20261015` | diverged | 20 | 1 | 20 | 19 |
| `research/canonical-frontier-v2` | behind | 0 | 270 | 0 | 0 |
| `release/canonical-theory-package-v1` | diverged | 25 | 262 | 25 | 52 |
| `cleanup/gr-qm-bit-continuum` | diverged | 77 | 269 | 77 | 73 |
| `research/pw-master-32` | diverged | 2 | 275 | 2 | 2 |

Important limitation: full branch inventory and HEAD capture are complete for the refs returned by the two API pages, but per-branch file diffs have not yet been queried for all 138 non-main branches. The ten comparisons above are a priority sample, not a substitute for the remaining comparisons.

## Recent CI evidence

Workflow API reported 2756 historical workflow runs; first page returned 100. These are records, not fresh runs.

| Workflow | Branch | SHA | Date | Conclusion |
|---|---|---|---|---|
| numerical-continuation | `main` | `1b887801` | 2026-10-19T18:51:50Z | success |
| core-regression | `main` | `1b887801` | 2026-10-19T18:51:50Z | failure |
| core-regression | `research/v26-graph-sector-output-obstruction-20261016` | `456aa7c4` | 2026-10-16T15:16:12Z | failure |
| numerical-continuation | `research/v26-graph-sector-output-obstruction-20261016` | `456aa7c4` | 2026-10-16T15:16:12Z | success |
| numerical-continuation | `research/v25-ancilla-crossscale-k5-20261016` | `45d7ba89` | 2026-10-16T08:27:18Z | success |
| core-regression | `research/v25-ancilla-crossscale-k5-20261016` | `45d7ba89` | 2026-10-16T08:27:18Z | failure |
| core-regression | `research/v24-crossscale-multiplicity-obstruction-20261016` | `e3eb71e8` | 2026-10-16T07:09:03Z | failure |
| numerical-continuation | `research/v24-crossscale-multiplicity-obstruction-20261016` | `e3eb71e8` | 2026-10-16T07:09:03Z | success |
| core-regression | `research/v23-unified-proof-bridge-20261016` | `c0df55a1` | 2026-10-15T22:08:31Z | failure |
| numerical-continuation | `research/v23-unified-proof-bridge-20261016` | `c0df55a1` | 2026-10-15T22:08:31Z | success |
| numerical-continuation | `research/v22-k5-kernel-ritz-cutoff-20261016` | `35056f1b` | 2026-10-15T19:26:17Z | success |
| core-regression | `research/v22-k5-kernel-ritz-cutoff-20261016` | `35056f1b` | 2026-10-15T19:26:17Z | failure |
| core-regression | `research/v21-first-shell-checkpoints-20261015` | `085e7b8a` | 2026-10-15T19:07:03Z | failure |
| numerical-continuation | `research/v21-first-shell-checkpoints-20261015` | `085e7b8a` | 2026-10-15T19:07:03Z | success |
| numerical-continuation | `research/v20-complete-160-canonical-20261015` | `f3ce62cf` | 2026-10-15T16:57:58Z | success |
| core-regression | `research/v20-complete-160-canonical-20261015` | `f3ce62cf` | 2026-10-15T16:57:58Z | failure |
| core-regression | `research/v19-canonical-k5-replay-20261015` | `1a715e22` | 2026-10-15T16:43:48Z | failure |
| numerical-continuation | `research/v19-canonical-k5-replay-20261015` | `1a715e22` | 2026-10-15T16:43:48Z | success |
| numerical-continuation | `research/v18-k5-parity-feshbach-20261015` | `2c59b1e0` | 2026-10-15T16:23:25Z | success |
| core-regression | `research/v18-k5-parity-feshbach-20261015` | `2c59b1e0` | 2026-10-15T16:23:25Z | failure |
| core-regression | `research/v17-k5-parity-shell-selection-20261015` | `330236f8` | 2026-10-15T15:42:22Z | failure |
| numerical-continuation | `research/v17-k5-parity-shell-selection-20261015` | `330236f8` | 2026-10-15T15:42:22Z | success |
| numerical-continuation | `research/v16-full-initial-k5-and-first-shell-20261015` | `95fa4040` | 2026-10-15T15:26:25Z | success |
| core-regression | `research/v16-full-initial-k5-and-first-shell-20261015` | `95fa4040` | 2026-10-15T15:26:25Z | failure |
| numerical-continuation | `research/v15-k5-32input-rank-audit-20261015` | `bc172ff2` | 2026-10-15T14:46:21Z | success |
| core-regression | `research/v15-k5-32input-rank-audit-20261015` | `bc172ff2` | 2026-10-15T14:46:21Z | failure |
| core-regression | `research/v14-k5-first-real-columns-20261015` | `ce43cabf` | 2026-10-15T13:33:40Z | failure |
| numerical-continuation | `research/v14-k5-first-real-columns-20261015` | `ce43cabf` | 2026-10-15T13:33:40Z | success |
| core-regression | `research/v13-k5-leakage-safe-master-20261015` | `2cd48130` | 2026-10-15T12:26:46Z | failure |
| numerical-continuation | `research/v13-k5-leakage-safe-master-20261015` | `2cd48130` | 2026-10-15T12:26:46Z | success |

Latest main run at the audited HEAD:
- `numerical-continuation`: success, run [39306094131](https://github.com/Shtenco/binary_quantum_theory/actions/runs/39306094131).
- `core-regression`: failure, run [39306094084](https://github.com/Shtenco/binary_quantum_theory/actions/runs/39306094084).
- In `canonical-core`, steps 1–40 succeeded, while `Registered canonical integration status` failed with exit code 2. Other jobs (`higher-shell`, `l1-q4-metric`, `directional-regge`) succeeded.
- Successful numerical continuation does not imply physical-limit closure.

## Depth-6 numerical frontier

Current `depth6_frontier.json` explicitly states `NUMERICAL_WITNESSES_PENDING`, `finite_depth6_theorem_status=NOT_YET_PROVED`, and leaves numerical witnesses pending for `[3,2]`, `[3,1,1]`, `[2,2,1]`.

| Sector | Dimension | Current status | Required action |
|---|---:|---|---|
| `[3,2]` | 130903 | `RECOVER_OR_FINISH` | Recover surviving Stage-A evidence and compute only missing master-map witnesses; do not recompute closed structural work. |
| `[3,1,1]` | 153455 | `PENDING_INDEPENDENT_NUMERICAL_WITNESS` | Produce an independent numerical witness. |
| `[2,2,1]` | 130503 | `PENDING_INDEPENDENT_NUMERICAL_WITNESS` | Produce an independent numerical witness. |

The 2026-10-02 recovery ledger reports 15 preserved shards, 7,749 columns (5.91965% of the `[3,2]` target). This is partial evidence, not full rank closure. The ledger explicitly prohibits recomputing shell enumeration, multiplicity, Jucys selectors, branch identity and structural matching already closed.

## Hamiltonian / physicalization gates

1. Finite positive master constraint identity is mathematically valid under its declared finite-dimensional assumptions; it does not prove a nontrivial continuum physical Hilbert space.
2. On the audited actual32 Euclidean H0 images, the recorded minimum master eigenvalue is about 3.97703148; finite spectral windows at zero disappear on that slice. This does not exclude a kernel outside the chosen code/habitat.
3. The two-hit Euclidean computation covers one original source column: 1,004 states per ordering, commutator norm 2.8794538147, and 96.34699% of squared norm outside the original 32D code. The other 31 columns, other node pairs and independent diffeomorphism constraint on the same habitat remain unverified.
4. The reduced TT propagator gives exact bare coefficients `eta2=-1/45`, `zeta4=-1/12` for its frozen lattice model. These are not yet physical IR predictions; the full constrained Peter–Weyl/history/RG TT kernel and common action normalization remain open.
5. `CONDITIONAL_PROOF.md` is explicitly conditional: physical projector/refinement, connected histories, Ward identities, TT positivity and suppression of higher-derivative/nonlocal terms are assumptions to prove, not already established BQG results.

## Reproducibility issues

- `requirements.txt` uses lower bounds rather than exact pins: numpy>=1.24, pandas>=2.0, scipy>=1.10, sympy>=1.12, networkx>=3.0, torch>=2.0. Historical reruns can drift across dependency releases.
- CI is configured for Python 3.11. Local reproduction should use the same interpreter and preserve BLAS thread settings where specified.
- Several numerical artifacts are large (multi-gigabyte shard archives); historical CI completion is not the same as a clean end-to-end recomputation from source.
- `.pkl` artifacts are executable-serialization risks; only load from the trusted repository and never treat them as inert data.
- Core regression is currently red at the registered canonical integration status even though numerical-continuation is green.

## Unified issue / obligation register

| ID | Severity | Finding / obligation | Exit criterion |
|---|---|---|---|
| AUD-001 | Critical | Core-regression fails at `Registered canonical integration status` (exit 2). | Capture exact gate mismatch; fix only if status is scientifically justified; CI green. |
| DEP-001 | High | Dependencies are unpinned. | Lock exact versions and hashes; rerun core and continuation CI. |
| BR-001 | High | 138 non-main refs exist; only 10 priority branches have detailed compare stats in this report. | Query compare API for every remaining branch and classify identical/ancestor/diverged/stale/unrelated. |
| D6-001 | Critical | `[3,2]` numerical master witness incomplete. | Recover trusted preserved shards; independent rank/conditioning certificate for all 130,903 columns. |
| D6-002 | Critical | `[3,1,1]` numerical witness pending. | Independent rank certificate for dimension 153,455. |
| D6-003 | Critical | `[2,2,1]` numerical witness pending. | Independent rank certificate for dimension 130,503. |
| H-001 | Critical | Finite actual32 Euclidean slice has no near-zero master eigenvalue. | Resolve habitat/constraint definition or retain the no-go for that slice; do not generalize beyond it. |
| H-002 | High | Two-hit dynamics largely leaks outside 32D code; only one source column checked. | Compute remaining columns and node pairs with independent D and controlled truncation bounds. |
| P-001 | Critical | Continuum physical projector / rigging map not established. | Refinement-compatible normalized physical matrix-element convergence and nonzero physical inner product. |
| P-002 | Critical | Full connected physical history and TT 1PI kernel not established. | Derive source-deformed history amplitude, Ward identities, positive massless TT pole and six Wilson coefficients. |
| P-003 | High | Bare lattice dispersion coefficients not promoted to physical IR observables. | Propagate full six-coefficient TT kernel through the constrained RG and freeze one scale before comparison. |
| EXP-001 | High | No independent replication / held-out observational validation. | Freeze commit, coefficients, scale and likelihood; run independent implementation and blind data comparison. |

## Reproduction commands declared by the repository

```bash
python scripts/verify_theory_gates.py
python scripts/verify_physicalization_gates.py
python scripts/verify_depth6_frontier.py
python scripts/bqg_ancilla_peter_weyl_refinement_gate.py
python research/audit_2026_10_10/replay_two_hit.py
python research/audit_2026_10_10/check_conditional_chain.py
```

These commands were read from repository audit documentation; they have not all been executed in this chat environment.

## Final verdict

Structural and finite numerical sub-results exist, and several regression controls pass. However, the full finite depth-6 numerical theorem is still explicitly not proved, the physical projector/history/TT continuum chain remains open, and the latest `core-regression` CI is failing. Do not label BQG as physically completed or as a verified derivation of GR.