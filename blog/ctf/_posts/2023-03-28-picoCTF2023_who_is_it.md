---
title: picoCTF 2023 – who is it
tags: forensics email whois
redirect_from:
  - /blog/ctf/2023/03/28/picoCTF2023_who_is_it.html
---

## Challenge

> Someone just sent you an email claiming to be Google's co-founder Larry Page but you suspect a scam.
> Can you help us identify whose mail server the email actually originated from?
> Download the email file [here](/assets/ctf/picoCTF2023/who%20is%20it.eml). Flag: picoCTF{FirstnameLastname}


## Solution

The challenge title indicated a potential whois lookup, so I checked the email for an IP address and found `173.249.33.206`.

The [lookup](https://www.whois.com/whois/173.249.33.206) yielded `Wilhelm Zwalina` as the first and last name, so the flag is `picoCTF{WilhelmZwalina}`.