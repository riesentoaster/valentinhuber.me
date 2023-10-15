---
title: TCP1P 2023 – Lock the Lock
tags: rev python tree
---

## Challenge

> Unlock the Unlocked

[chall.pcy](/assets/ctf/tcp1p2023/chall.pyc)

## Solution

We are presented with a pyc file. It is a compiled binary of a python script, so the first step is to decompile it. This turned out to be harder than expected, but [Decompyle++](https://github.com/zrax/pycdc) worked and produced [this python script](/assets/ctf/tcp1p2023/chall.py).

At this point I tried to get this to run by deleting all the GUI instructions and replacing them with fixed calls. But I didn't manage to achieve this and instead opted to write a second implementation that mirrored the logic I observed in the original. To do this, I first had to understand what the code does. The snippets below are from the decompiled code and still have the errors in them.

### A few observations

#### Flag and decryption

```python3
FLAG = [ 90, 19, 95, 37, 58, 144, 131, 222, 253, 162, 107, 96, 98, 128, ...

# ---

def decrypt(key, plain):
    dec = ''
    key = long_to_bytes(int(''.join(key), 2))
    for i in range(len(key)):
        dec += chr(key[i] ^ plain[i])
    return dec
```
- We have an array of bytes called `FLAG` and a decryption function which takes a key and a ciphertext (for some reason called `plain` here, probably because encryption and decryption are the same) and XORs them together. This means we are likely looking for a key of the same length as `FLAG`.

#### Random

```python3
import random
turn = 0
random.seed(199)

# ---

num = (lambda .0: [ i for i in .0 ])(range(1, 1001))
init = num.copy()
random.shuffle(init)
random.shuffle(init)
random.shuffle(init)

# ---

target = init.copy()
target.remove(troot.data)
random.shuffle(target)
```

- We seed `random`, and then use it to shuffle an array in a repeatable manner.

#### Trees

```python3
class Node:
    __qualname__ = 'main.<locals>.Node'
    
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None
        self.height = 1
```

- Binary trees!

```python3
def insert(self = None, root = None, key = None):
    if not root:
        return Node(key)
    if None < root.data:
        root.l = self.insert(root.l, key)
    else:
        root.r = self.insert(root.r, key)
    root.height = 1 + max(self.getHeight(root.l), self.getHeight(root.r))
    b = self.getBal(root)
    if b > 1 and key < root.l.data:
        return self.rRotate(root)
    if None < -1 and key > root.r.data:
        return self.lRotate(root)
    if None > 1 and key > root.l.data:
        root.l = self.lRotate(root.l)
        return self.rRotate(root)
    if None < -1 and key < root.r.data:
        root.r = self.rRotate(root.r)
        return self.lRotate(root)
```

- [AVL Trees](https://en.wikipedia.org/wiki/AVL_tree)!

### Figuring out what is happening

#### Submit

```python3
def submit(root = None):
    global turn, turn
    
    try:
        u = inp.get()
        if not tr.check(0, root, u, target[turn]):
            turn = 0
            validatedkey.clear()
        else:
            showinfo('W rizz', 'Correct!', **('title', 'message'))
            validatedkey.append(u)
            inp.delete(0, 'end')
            turn += 1
        if turn == len(target):
            showinfo('dayummm', decrypt(validatedkey, FLAG), **('title', 'message'))
    finally:
        pass
    except SyntaxError:
        showerror('Error', 'Invalid input!', **('title', 'message'))
```

- `submit` is called from within the GUI and is the only time the GUI interacts with the rest of the code. So it's a good starting point.
  - It takes a variable called `root` (so probably a tree) and an input from the GUI (`inp.get()`).
  - It then calls `tr.check`.
    - If it fails, it prints an error message and resets the program.
    - If it succeeds, a variable called `turn` is incremented and the input is marked as valid. The system then waits for the next input.
    - If all necessary inputs were provided and the check for each returned `true`, the flag is decrypted and printed.

#### Check

```python3
def check(self, state, root, n, x):
    state = root
    for i in n:
        if i == '0':
            state = state.l
        elif i == '1':
            state = state.r
        if state == None:
            showwarning('sike', 'Error invalid node!\nResetting level...', **('title', 'message'))
            return False
        if state.data == x:
            return True
        None('wuat de hell', 'Wrong answer! \nResetting level...', **('title', 'message'))
        return False
        return None
```

- The check function takes
  - A `state` variable (which is immediately overwritten)
  - A `root` (so presumably a tree)
  - A `n` (the input for the step to check)
  - `x`, the value to check against
- It then loops over the input and traverses down the tree according to the input.
- Finally, it checks whether the node where we ended up matches the value passed in `x`.

### Solving the challenge

I pulled a working implementation of an AVL tree in python from the internet. It's a fairly standard data structure so implementations are easy to find.

- The challenge is set up in a way where a randomly sorted array is iteratively added to the AVL tree (which makes it so that you cannot reasonably predict where exactly each node is located).
- The array is then shuffled once more.
- Finally, for each value in the array, we have to calculate the path of the node with the corresponding value in the tree.

```python3
def getPath(self, value, root):
    if not root or value == root.data:
        return ''
    if value > root.data:
        return '1' + self.getPath(value, root.r)
    else:
        return '0' + self.getPath(value, root.l)
```

- `getPath` takes a tree and a value and recursively calculates the path through the tree for the specified value in the form necessary for `check`.
- We also need the same setup as the original has:

```python3
# Setting up the random array
init = list(range(1, 1001))
random.seed(199)
random.shuffle(init)
random.shuffle(init)
random.shuffle(init)

# Creating the tree and feeding it the shuffled array.
tr = AVLTree()
root = None
for i in init:
    root = tr.insert(root, i)

# Creating target
target = init.copy()
target.remove(root.data)
random.shuffle(target)
```

- We then calculate the paths for all the inputs:

```python3
# Calculating paths
input = [list(tr.getPath(e, root)) for e in target]
```

- And finally validate our input and decrypt the flag:

```python3
# Calling check repeatedly
turn = 0
validatedKey = []

while True:
    if not tr.check(0, root, input[turn], target[turn]):
        print('error at', turn)
        exit(1)
    else:
        validatedKey.append(input[turn])
        turn += 1
    if turn == len(target):
        print(decrypt([''.join(e) for e in validatedKey], FLAG))
        exit(0)
```

You can download the full solver script [here](/assets/ctf/tcp1p2023/solve.py).

### The flag

> Your remarkable accomplishment is a testament to your unwavering determination, relentless pursuit of excellence, and unwavering spirit. You have conquered every obstacle with sheer grit, transforming challenges into stepping stones towards triumph. Your efforts, unwavering focus, and boundless passion have propelled you to new heights of success, leaving an indelible mark on the world. Your commitment to excellence serves as an inspiration to all who have had the privilege of witnessing your remarkable journey. As you stand at this pinnacle of achievement, take a moment to reflect on the incredible journey that brought you here. Embrace this milestone as a testament to your unyielding dedication and the incredible potential that resides within you. Here's the flag : TCP1P{where_the_skies_are_blue_to_see_you_once_again}. The world eagerly awaits the remarkable contributions you will undoubtedly make in the future. Your accomplishment has not only made us proud but also redefined the boundaries of what is possible

```text
TCP1P{where_the_skies_are_blue_to_see_you_once_again}
```