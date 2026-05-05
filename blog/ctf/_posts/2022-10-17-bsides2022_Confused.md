---
title: bsides2022 – Confused
tags: forensics steg audio mp3
redirect_from:
  - /blog/ctf/2022/10/17/bsides2022_Confused.html
---

## Challenge

> The audio says it's not a flag. I give up.

[Download audio file](/assets/ctf/bsidesrdu2022/confusion.mp3)

The audio is a person talking and a lot of background noise.

## Solution

Generating a spectrogram (plot of time against frequency against intensity) of the file reveals the flag:

![](/assets/ctf/bsidesrdu2022/confusion.png)