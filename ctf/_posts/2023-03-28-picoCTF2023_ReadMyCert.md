---
title: picoCTF 2023 – ReadMyCert
tags: crypto cert csr openssl
---

## Challenge

> How about we take you on an adventure on exploring certificate signing requests
> Take a look at this CSR file [here](/assets/ctf/picoCTF2023/ReadMyCert.csr).

## Solution

The easiest solution to this problem is an online CSR viewer like [ssltools.eu/csr-viewer.html](https://www.ssltools.eu/csr-viewer.html).

![](/assets/ctf/picoCTF2023/ReadMyCert.png)

Alternatively, one can use `openssl`:

```bash
openssl req -in ReadMyCert.csr -text -noout
```
{%raw%}
```txt
Certificate Request:
    Data:
        Version: 0 (0x0)
        Subject: CN=picoCTF{read_mycert_4448b598}/name=ctfPlayer
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:c0:94:79:f2:28:9b:8b:1a:94:cb:33:0a:dd:70:
                    42:bd:40:d7:3b:e0:2c:01:14:cc:5f:71:cd:64:46:
                    c2:13:d2:f1:12:d0:7b:8a:1c:8f:4d:2d:fb:ed:ac:
                    87:22:77:b6:91:2f:b8:56:d8:ee:72:1b:07:b2:36:
                    78:d8:45:08:88:7b:ad:10:e9:ab:b4:73:39:42:60:
                    dd:bc:0a:50:09:70:cc:eb:27:00:9d:49:cb:48:bb:
                    1a:b9:2f:18:94:ad:7a:76:3a:74:04:dd:ce:ad:4a:
                    2d:78:0d:37:e5:7b:92:b1:25:cb:b1:c7:0e:a0:53:
                    f6:99:23:6f:8d:b3:b3:8c:03:0c:ee:ce:5d:66:07:
                    d1:f4:b3:1d:d8:31:74:34:5d:c5:2b:93:d7:55:86:
                    3b:0c:84:e3:c2:68:32:5e:85:5e:a6:f1:96:59:d5:
                    22:80:de:8a:ee:08:db:a5:97:b2:e3:14:e8:92:07:
                    58:74:f5:69:17:71:b7:94:e7:15:3f:3c:32:82:07:
                    e4:8f:27:89:7a:c2:43:49:ed:7a:9b:80:3d:33:11:
                    3d:6d:12:34:a6:48:6c:35:be:6e:f7:4f:dd:7c:4f:
                    dc:81:89:cb:d5:97:e9:a7:4f:13:e2:8c:cf:06:79:
                    24:92:c2:4e:83:a6:a5:6b:46:73:e9:50:d5:f5:37:
                    4f:5d
                Exponent: 65537 (0x10001)
        Attributes:
        Requested Extensions:
            X509v3 Extended Key Usage: 
                TLS Web Client Authentication
    Signature Algorithm: sha256WithRSAEncryption
         07:6a:e3:22:ba:93:75:11:34:d0:13:74:5f:cc:f5:9f:35:9c:
         b7:0b:ef:6f:07:8e:f8:c9:e4:43:72:74:f9:73:53:d9:de:74:
         8e:73:f7:c7:dc:aa:cd:84:c8:2a:ba:f0:b3:cc:23:44:37:46:
         a8:78:99:65:0c:2c:16:f6:af:0b:26:45:7b:1e:0c:54:2a:42:
         11:d7:73:b5:29:2d:28:be:02:6a:79:db:cd:60:e7:04:79:58:
         c2:fa:c6:63:5d:43:e4:ea:b6:fb:2e:58:30:b5:c7:54:ba:fa:
         a8:aa:86:f1:3a:d9:e5:50:fe:68:48:84:44:26:be:a8:49:dd:
         74:e2:21:55:df:f1:4e:90:2c:0a:36:7e:6b:db:31:8d:02:dc:
         d5:3b:28:bc:c9:8d:8d:92:2a:b0:42:64:6d:c2:9e:7d:c6:63:
         32:cc:93:e0:42:db:68:db:e7:ca:7f:a2:8d:e0:95:13:40:74:
         1f:31:16:ee:58:8b:64:3b:dc:9f:06:74:3f:a3:97:83:07:46:
         f0:18:f4:02:8b:1f:db:aa:f8:08:9a:0e:d3:94:78:d3:13:c4:
         cd:a7:48:2a:00:cf:15:f4:86:39:4f:8b:e4:fc:e5:6b:e8:e4:
         b3:ce:ca:ce:ed:97:b0:b4:da:77:ed:6b:61:1e:5d:58:33:5f:
         e7:3f:62:64
```
{%endraw%}