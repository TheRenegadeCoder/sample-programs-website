---
authors:
- "Christoph B\xF6hmwalder"
date: 2018-08-31
featured-image: fizz-buzz-in-every-language.png
last-modified: 2018-08-31
layout: default
tags:
- bash
- fizz-buzz
title: Fizz Buzz in Bash
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/bash/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/bash/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Bash](https://sampleprograms.io/languages/bash) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```bash
#!/bin/bash

for i in {1..100}; do
    if (( $i % 15 == 0 )); then
        echo "FizzBuzz"
    elif (( $i % 5 == 0 )); then
        echo "Buzz"
    elif (( $i % 3 == 0 )); then
        echo "Fizz"
    else
        echo $i
    fi
done

```

{% endraw %}

Fizz Buzz in [Bash](https://sampleprograms.io/languages/bash) was written by:

- Christoph Böhmwalder

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).