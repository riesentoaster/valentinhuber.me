---
title: picoCTF 2023 – rotation
tags: crypto rot13 cyberchef
---

## Challenge

> You will find the flag after decrypting this file
> Download the encrypted flag [here](/assets/ctf/picoCTF2023/rotation.txt).

File content:

```txt
xqkwKBN{z0bib1wv_l3kzgxb3l_429in00n}
```

## Solution

The challenge title indicates some form of rotation cipher, so I put the encoded text into [cyberchef](https://icyberchef.com) and used the `ROT13 Brute Force` module to rotate the text. A quick text search on the output showed that the encoding is a rotation by 18 chars and the flag is `picoCTF{r0tat1on_d3crypt3d_429af00f}`.