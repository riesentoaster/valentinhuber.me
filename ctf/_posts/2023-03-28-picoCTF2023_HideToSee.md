---
title: picoCTF 2023 – HideToSee
tags: forensics crypto steg steghide python
---

## Challenge

> How about some hide and seek heh?
> Look at this image [here](/assets/ctf/picoCTF2023/HideToSee.jpg).

## Solution

The image seems to show a crypto system, but we don't have any encrypted data. So I checked if there was some data hidden using steganography:

```bash
steghide extract -sf HideToSee.jpg -p "" # no password since we don't have anything
```

Which returned the following: `krxlXGU{zgyzhs_xizxp_xz00558y}`. This seemed like an encrypted flag. I couldn't be bothered to manually decrypt it using the system in the picture, so I wrote a short python script to do it:

{%raw%}
```python3
import string
input = "krxlXGU{zgyzhs_xizxp_vx4zyz61}"

def swap(a:chr)->str:
    if a not in string.ascii_letters:
        return a
    elif ord(a) <= ord('_'):
        return chr(ord('Z')-ord(a)+ord('A'))
    else:
        return chr(ord('z')-ord(a)+ord('a'))
    
res = ''
for e in input:
    res += swap(e)
print(res)
```
{%endraw%}

Et voilà: `picoCTF{atbash_crack_ec4aba61}`.
