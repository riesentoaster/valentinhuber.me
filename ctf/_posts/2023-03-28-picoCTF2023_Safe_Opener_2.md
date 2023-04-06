---
title: picoCTF 2023 – Safe Opener 2
tags: rev java decompile
---

## Challenge

> What can you do with this file?
> I forgot the key to my safe but this [file](/assets/ctf/picoCTF2023/SafeOpener.class) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

## Solution

The file is a Java `.class` file, so a compiled file ready to be run in the Java Virtual Machine. I used this [online decompiler](http://www.javadecompilers.com/) to get the decompiled file:

{%raw%}
```java
import java.io.IOException;
import java.util.Base64;
import java.io.Reader;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class SafeOpener
{
    public static void main(final String[] args) throws IOException {
        final BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
        final Base64.Encoder encoder = Base64.getEncoder();
        String encodedkey = "";
        String key = "";
        for (int i = 0; i < 3; ++i) {
            System.out.print("Enter password for the safe: ");
            key = keyboard.readLine();
            encodedkey = encoder.encodeToString(key.getBytes());
            System.out.println(encodedkey);
            final boolean isOpen = openSafe(encodedkey);
            if (isOpen) {
                break;
            }
            System.out.println("You have  " + (2 - i) + " attempt(s) left");
        }
    }
    
    public static boolean openSafe(final String password) {
        final String encodedkey = "picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_0e57c117}";
        if (password.equals(encodedkey)) {
            System.out.println("Sesame open");
            return true;
        }
        System.out.println("Password is incorrect\n");
        return false;
    }
}
```
{%endraw%}