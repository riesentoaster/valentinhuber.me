---
title: picoCTF 2023 – PcapPoisoning
tags: forensics pcap strings grep
---

## Challenge

> How about some hide and seek heh?
> Download this [file](/assets/ctf/picoCTF2023/PcapPoisoning.pcap) and find the flag.

## Solution

```bash
strings PcapPoisoning.pcap | grep pico
```

led to

```txt
picoCTF{P64P_4N4L7S1S_SU55355FUL_b1995216}
```

This is why you never underestimate the power of basic linux tools like strings and grep.