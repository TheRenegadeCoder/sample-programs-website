---
authors:
- Riley Martine
date: 2018-10-03
featured-image: fizz-buzz-in-every-language.png
last-modified: 2018-10-03
layout: default
tags:
- dg
- fizz-buzz
title: Fizz Buzz in Dg
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/dg/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/dg/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Dg](https://sampleprograms.io/languages/dg) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dg
fizz_buzz = n -> if
    n % 15 == 0 => "FizzBuzz"
    n % 3  == 0 => "Fizz"
    n % 5  == 0 => "Buzz"
    otherwise   => n

main = start end ruleset ->
    for i in range start (end + 1) =>
        print <| ruleset i

main 1 100 fizz_buzz

```

{% endraw %}

Fizz Buzz in [Dg](https://sampleprograms.io/languages/dg) was written by:

- Riley Martine

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).