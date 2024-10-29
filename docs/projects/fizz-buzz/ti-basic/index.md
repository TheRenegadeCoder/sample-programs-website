---
authors:
- rzuckerm
date: 2024-10-28
featured-image: fizz-buzz-in-every-language.png
last-modified: 2024-10-28
layout: default
tags:
- fizz-buzz
- ti-basic
title: Fizz Buzz in Ti Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/ti-basic/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/ti-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Ti Basic](https://sampleprograms.io/languages/ti-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ti_basic
For(N,1,100)
    If remainder(N,15)=0 Then Disp("FizzBuzz")
    Else
        If remainder(N,3)=0 Then Disp("Fizz")
        Else
            If remainder(N,5)=0 Then Disp("Buzz")
            Else Disp(N)
            End
        End
    End
End

```

{% endraw %}

Fizz Buzz in [Ti Basic](https://sampleprograms.io/languages/ti-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).