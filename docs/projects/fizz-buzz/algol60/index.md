---
authors:
- rzuckerm
date: 2026-03-17
featured-image: fizz-buzz-in-every-language.png
last-modified: 2026-03-17
layout: default
tags:
- algol60
- fizz-buzz
title: Fizz Buzz in ALGOL 60
title1: Fizz Buzz
title2: in ALGOL 60
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/algol60/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/algol60/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [ALGOL 60](https://sampleprograms.io/languages/algol60) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol_60
begin
    integer procedure mod(x, n);
    value x, n;
    integer x, n;
    begin
        mod := x - n * (x % n)
    end mod;

    integer i;
    for i := 1 step 1 until 100 do
    begin
        if mod(i, 15) = 0 then outstring(1, "FizzBuzz")
        else if mod(i, 3) = 0 then outstring(1, "Fizz")
        else if mod(i, 5) = 0 then outstring(1, "Buzz")
        else outinteger(1, i);
        outstring(1, "\n")
    end
end

```

{% endraw %}

Fizz Buzz in [ALGOL 60](https://sampleprograms.io/languages/algol60) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).