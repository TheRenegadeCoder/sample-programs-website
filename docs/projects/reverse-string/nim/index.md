---
title: Reverse String in Nim
layout: default
date: 2019-10-22
featured-image: reverse-string-in-every-language.jpg
last-modified: 2019-10-22

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Nim](https://sampleprograms.io/languages/nim) page! Here, you'll find the source code for this program as well as a description of how the program works.

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
    quit(0)

var reversed_text: string
for i in countdown(len(text)-1, 0):
  reversed_text = reversed_text & text[i]

echo reversed_text
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Nim](https://sampleprograms.io/languages/nim) was written by:

- Michael Olson
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 19 2023 22:24:49. The solution was first committed on Oct 22 2019 07:54:58. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).