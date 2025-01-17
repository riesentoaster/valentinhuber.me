---
title: picoCTF 2023 – repetitions
tags: base64 python
---

## Challenge

> Can you make sense of this file?
> Download the file [here](/assets/ctf/picoCTF2023/repetitions.txt).

File content:
```txt
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbFpSV0VKWVZGVmtNRTVHV2tWU2JYUlVDbUpXV25sVWJGcHZWbGRHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
```

## Solution

The `==` at the end of the data indicates base64, the title indicates a repeated application. So I wrote a short python script:

{%raw%}
```python
from base64 import b64decode
data = "VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVhRmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNkMlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVWVkpEVGxaYVdFMVhSbGhhTTBKWVZXeG9RMlZXV2tkWGJYUlVDbUY2VmtoWmEyaEhWMGRHZEdWRlZsaGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg=="
while "picoCTF" not in data:
    data = b64decode(data).decode().strip()

print(data)
```
{%endraw%}