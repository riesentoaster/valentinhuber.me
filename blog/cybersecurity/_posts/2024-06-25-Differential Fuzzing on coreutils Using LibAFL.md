---
tags: fuzzing, coreutils, LibAFL
title: "Differential Fuzzing on coreutils Using LibAFL"
---

After [reading about fuzzing]({% post_url blog/cybersecurity/2023-12-15-Challenges and Mitigation Strategies in Symbolic Execution Based Fuzzing Through the Lens of Survey Papers %}) and [testing a fuzzer]({% post_url blog/cybersecurity/2024-02-13-Running KLEE on GNU coreutils %}), I wanted to delve deeper into the inner workings. In discussions with my advisor, we found that there is a lot of work on some parts of fuzzers, such as advanced scheduling algorithms, but the oracle of what constitutes an illegal state has received comparably little attention.

Since I've previously worked with coreutils, I found that there are multiple implementations available, including some that claim to be complete drop-in replacements. I therefore decided to build a differential fuzzer to not only find crashes based on memory violations in the projects, but more subtle logic bugs.

I based my fuzzer on LibAFL, a framework to build fuzzers, which included basic support for differential fuzzing. During the project, I had to create a novel approach to transferring coverage information from a child process back to the fuzzer. Additionally, I experimented with custom input types and mutations on them, starting the process of making these more flexible in the upstream project. 

During the project I've already started contributing to LibAFL in five pull requests containing more than 500 lines of code. And while the improvements on mutators for custom inputs could not be completed during the project (and thus limits the evaluation performed to a small subset of coreutils' features), work on that has already started, and will be finished in the upcoming months.

The fuzzer's source code is available under an open-source license [here](https://github.com/riesentoaster/coreutils-differential-fuzzing/), the report can be found [here](https://github.com/riesentoaster/coreutils-differential-fuzzing/blob/main/report/out/index.pdf).