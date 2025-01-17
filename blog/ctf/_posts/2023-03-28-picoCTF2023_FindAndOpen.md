---
title: picoCTF 2023 – FindAndOpen
tags: forensics pcap base64 zip cyberchef
---

## Challenge

> Someone might have hidden the password in the trace file.
> Find the key to unlock [this file](/assets/ctf/picoCTF2023/FindAndOpen.zip). [This tracefile](/assets/ctf/picoCTF2023/FindAndOpen.pcap) might be good to analyze.

## Solution

The ZIP file asks for a password. So we'll look at the tracefile to see if we can find anything.

Using `!mdns` as a filter (to remove packets by a chromecast), we are left with a few packets, most of which are duplicates. Here's a list:

| id  | Text (ASCII decoded)                                                     | Packet No.      |
| --- | ------------------------------------------------------------------------ | --------------- |
| 1   | `Flying on Ethernet secret: Is this the flag`                            | (Packets 1-9)   |
| 2   | `iBwaWNvQ1RGe1Could the flag have been splitted?`                        | (Packets 23-47) |
| 3   | `AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=` | (Packet 48)     |
| 4   | `PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS`                      | (Packets 49-57) |
| 5   | `PBwaWUvQ1RGe1Maybe try checking the other file`                         | (Packets 58-65) |

Packets with id `3` seems most interesting. If we remove the first few bytes (that are part of the Ethernet header), we are left with the string `VGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=`. The `=` sign at the end of string one gave me the idea that this might be base64 encoded. So I threw it into [cyberchef](https://icyberchef.com) and got `This is the secret: picoCTF{R34DING_LOKd_`.

`picoCTF{R34DING_LOKd_` was the password for the zip file, which contained a text file with the flag: `picoCTF{R34DING_LOKd_fil56_succ3ss_419835ef}`.
