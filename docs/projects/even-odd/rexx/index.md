---
title: Even Odd in Rexx
layout: default
date: 2020-10-07
featured-image: even-odd-in-every-language.jpg
last-modified: 2020-10-07

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Rexx](https://sampleprograms.io/languages/rexx) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rexx
/* ARG with source string named in REXX program invocation */
arg number
If (DATATYPE(number, 'W') == 0) then signal err
if (number // 2 == 0) then
    say "Even"
else
    say "Odd"
;exit

Err:
say 'Usage: please input a number'; exit
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Rexx](https://sampleprograms.io/languages/rexx) was written by:

- Sudhanshu Dubey

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).