---
authors:
- rzuckerm
date: 2023-12-26
featured-image: even-odd-in-every-language.jpg
last-modified: 2024-01-01
layout: default
tags:
- even-odd
- pyret
title: Even Odd in Pyret
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/pyret/how-to-implement-the-solution.md
- sources/programs/even-odd/pyret/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Pyret](https://sampleprograms.io/languages/pyret) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pyret
import cmdline-lib as CL

usage = "Usage: please input a number\n"
args = CL.command-line-arguments()
cases(Option) string-to-number(if args.length() > 1: args.get(1) else: "" end):
  | none => print(usage)
  | some(n) =>
    if not(num-is-integer(n)): print(usage)
    else if num-modulo(n, 2) == 0: print("Even\n")
    else: print("Odd\n")
    end
end

```

{% endraw %}

Even Odd in [Pyret](https://sampleprograms.io/languages/pyret) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).