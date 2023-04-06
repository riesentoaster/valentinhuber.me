---
title: picoCTF 2023 – findme
tags: web curl base64 cyberchef
---

## Challenge

> Help us test the form by submiting the username as `test` and password as `test`!

Screenshot of the website:

![](/assets/ctf/picoCTF2023/findme1.png)

After logging in with the provided username and password:

![](/assets/ctf/picoCTF2023/findme2.png)

## Solution

When logging in, you get redirected multiple times. So I manually checked each of the steps, starting with logging in:

{%raw%}
```bash
curl -d "username=test&password=test\!" "[url]/login"
```
{%endraw%}

This returned:
{%raw%}
```
Found. Redirecting to /next-page/id=cGljb0NURntwcm94aWVzX2Fs
```
{%endraw%}

So I checked that page:
{%raw%}
```bash
curl "[url]/next-page/id=cGljb0NURntwcm94aWVzX2Fs"
```
{%endraw%}

And got:

{%raw%}
```html
<!DOCTYPE html>
<head>
    <title>flag</title>
</head>
<body>
    <script>
        setTimeout(function () {
            // after 2 seconds
           window.location = "/next-page/id=bF90aGVfd2F5X2EwZmUwNzRmfQ==";
        }, 0.5)
      </script>
    <p></p>
</body>                                                                 
```
{%endraw%}

The `==` in the end of that id indicated base64, so I threw it into [cyberchef](https://icyberchef.com) and got `l_the_way_a0fe074f}`, which seemed like the second half of the flag. So I prepended the id of the first redirect and got `picoCTF{proxies_all_the_way_a0fe074f}`.

