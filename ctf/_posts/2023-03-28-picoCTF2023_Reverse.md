---
title: picoCTF 2023 – Reverse
tags: rev strings grep
---

## Challenge

> Try reversing this file? Can ya?
> I forgot the password to this [file](/assets/ctf/picoCTF2023/Reverse). Please find it for me?

## Solution

The provided file seems to be a binary. First step is to check if the flag is in there as plain text:

```bash
strings Reverse | grep picoCTF
```

```txt
picoCTF{H
Password correct, please see flag: picoCTF{3lf_r3v3r5ing_succe55ful_1de05085}
```