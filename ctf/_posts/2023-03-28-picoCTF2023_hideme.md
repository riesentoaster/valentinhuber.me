---
title: picoCTF 2023 – hideme
tags: forensics steg binwalk
---

## Challenge

> Every file gets a flag. The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](/assets/ctf/picoCTF2023/hideme.png).

## Solution

{%raw%}
```bash
binwalk -e hideme.png
```
{%endraw%}

This extracts a few files including one called `secret/flag.png`. This in turn contains the flag:

![](/assets/ctf/picoCTF2023/hideme_flag.png)

