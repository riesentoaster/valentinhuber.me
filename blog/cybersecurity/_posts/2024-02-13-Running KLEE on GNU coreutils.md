---
tags: fuzzing symbex KLEE coreutils
title: "Running KLEE on GNU coreutils"
---

While [I read a lot about symbolic execution in fuzzing for a seminar]({% post_url blog/cybersecurity/2023-12-15-Challenges and Mitigation Strategies in Symbolic Execution Based Fuzzing Through the Lens of Survey Papers %}), I wanted to actually do it. Since KLEE appeared to be one of the most influential fuzzing tool, I decided to attempt to reproduce the findings in their original paper. Additionally, I chose to compare different versions of GNU's coreutils to investigate the quality of software over time. 

The report is available [here](https://github.com/riesentoaster/klee-coreutils-experiments/releases/download/v1.0/Huber-Valentin-running-KLEE-on-coreutils-report.pdf), the orchestration code and resulting data can be found in the [project repository](https://github.com/riesentoaster/klee-coreutils-experiments).