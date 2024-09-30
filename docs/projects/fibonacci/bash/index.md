---
authors:
- Parker Johansen
date: 2018-10-26
featured-image: fibonacci-in-every-language.jpg
last-modified: 2019-04-07
layout: default
tags:
- bash
- fibonacci
title: Fibonacci in Bash
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/bash/how-to-implement-the-solution.md
- sources/programs/fibonacci/bash/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Bash](https://sampleprograms.io/languages/bash) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```bash
#!/bin/bash

count=$1

[[ $count =~ ^[0-9]+$ ]] || { echo "Usage: please input the count of fibonacci numbers to output"; exit 1; }

n=1
n_minus_1=1
[[ $count < 1 ]] && exit 0

echo "1: 1"
for i in $(seq 2 $count); do
    echo "$i: $n"
    tmp=$n
    n=$[$n+$n_minus_1]
    n_minus_1=$tmp
done

```

{% endraw %}

Fibonacci in [Bash](https://sampleprograms.io/languages/bash) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).