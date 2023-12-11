---
title: HTB 2023 – WindowsOfOpportunity
tags: rev ghidra decompile
---

## Challenge

> You've located a zombie hideout and are trying to peek inside. Suddenly, a window opens a crack and a zombie peers out - they want a password...

[binary](/assets/ctf/htb2023/windows)

## Solution

I threw the binary into Ghidra and got the decompiled main function:

```c
undefined8 main(void)

{
  char attempt [43];
  char to_check;
  uint i;
  
  puts("A voice comes from the window... \'Password?\'");
  fgets(attempt,0x2a,stdin);
  i = 0;
  while( true ) {
    if (0x24 < i) {
      puts("The window opens to allow you passage...");
      return 0;
    }
    to_check = attempt[(int)(i + 1)] + attempt[(int)i];
    if (to_check != arr[(int)i]) break;
    i = i + 1;
  }
  puts("The window slams shut...");
  return 0xffffffff;
}
```

It seems like a password is read, and some calculation is done, mangling the bytes. I wrote a quick python script that reverses it and used knowledge about the flag format to bootstrap it:

```python
data = "9c 96 bd af 93 c3 94 60 a2 d1 c2 cf 9c a3 a6 68 94 c1 d7 ac 96 93 93 d6 a8 9f d2 94 a7 d6 8f a0 a3 a1 a3 56 9e"
data = data.split(" ")
data = [int(e,16) for e in data]
solution = "H"
solution = [ord(e) for e in solution]

for i in range(len(data)):
    solution.append(data[i]-solution[i])

solution = [chr(e) for e in solution]
print("".join(solution))
```

And out came `HTB{4_d00r_cl0s35_bu7_4_w1nd0w_0p3n5!}`.