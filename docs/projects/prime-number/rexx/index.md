---
title: Prime Number in Rexx
layout: default
date: 2020-10-07
featured-image: prime-number-in-every-language.jpg
last-modified: 2020-10-07

---

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Rexx](https://sampleprograms.io/languages/rexx) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rexx
/* ARG with source string named in REXX program invocation */
arg number
If (DATATYPE(number, 'W') == 0) then signal err
If (number < 0) then signal err
isPrime = 1
if \((number // 2 = 0) & (number \= 2) | (number == 1)) then
    do
        i = TRUNC(number / 2)
        do while(i > 3)
            if (number // i == 0) then
                isPrime = 0
            i = i - 1
        end
    end
else
    isPrime = 0

if (isPrime == 1) then
    say "Prime"
else
    say "Composite"
;exit

Err:
say 'Usage: please input a non-negative integer'; exit
```

{% endraw %}

[Prime Number](https://sampleprograms.io/projects/prime-number) in [Rexx](https://sampleprograms.io/languages/rexx) was written by:

- Sudhanshu Dubey

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).