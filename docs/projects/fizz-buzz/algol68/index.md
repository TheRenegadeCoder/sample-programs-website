---
authors:
- rzuckerm
date: 2023-01-18
featured-image: fizz-buzz-in-every-language.png
last-modified: 2023-01-21
layout: default
tags:
- algol68
- fizz-buzz
title: Fizz Buzz in Algol68
---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
FOR n FROM 1 TO 100
DO
    STRING s := (n MOD 3 = 0 | "Fizz" | "");
    s +:= (n MOD 5 = 0 | "Buzz" | "");
    printf(($gl$, (s /= "" | s | whole(n, 0))))
OD

```

{% endraw %}

Fizz Buzz in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).