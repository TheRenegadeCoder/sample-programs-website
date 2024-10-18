---
authors:
- rzuckerm
date: 2024-10-17
featured-image: fizz-buzz-in-every-language.png
last-modified: 2024-10-17
layout: default
tags:
- fizz-buzz
- red
title: Fizz Buzz in Red
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/red/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/red/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Red](https://sampleprograms.io/languages/red) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```red
; Source: https://rosettacode.org/wiki/FizzBuzz#Red
Red [Title: "FizzBuzz"]

repeat i 100 [
    print case [
        i % 15 = 0 ["FizzBuzz"]
        i % 5 = 0 ["Buzz"]
        i % 3 = 0 ["Fizz"]
        true [i]
    ]
]

```

{% endraw %}

Fizz Buzz in [Red](https://sampleprograms.io/languages/red) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).