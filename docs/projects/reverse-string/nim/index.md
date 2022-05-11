---

title: Reverse String in Nim
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Reverse String in Nim page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```nim
# For reversing a string passed in as a parameter
import os
import strutils

var text: string
try:
    text = paramStr(1)
except IndexError:
    echo "Usage: please input a string to reverse"
    quit(1)

var reversed_text: string
for i in countdown(len(text)-1, 0):
  reversed_text = reversed_text & text[i]

echo reversed_text
```

{% endraw %}

Reverse String in Nim was written by:

- Michael Olson

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).