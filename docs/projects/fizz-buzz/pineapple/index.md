---
authors:
- rzuckerm
date: 2024-11-20
featured-image: fizz-buzz-in-every-language.png
last-modified: 2024-11-20
layout: default
tags:
- fizz-buzz
- pineapple
title: Fizz Buzz in Pineapple
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/pineapple/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/pineapple/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Pineapple](https://sampleprograms.io/languages/pineapple) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pineapple
def .main
    let i mutable = 1
    while i <= 100
        if i % 15 == 0
            "FizzBuzz".show
        elif i % 3 == 0
            "Fizz".show
        elif i % 5 == 0
            "Buzz".show
        else
            i.show

        i = i + 1

```

{% endraw %}

Fizz Buzz in [Pineapple](https://sampleprograms.io/languages/pineapple) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).