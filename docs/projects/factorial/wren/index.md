---
authors:
- Zia
date: 2025-01-21
featured-image: factorial-in-every-language.jpg
last-modified: 2025-01-21
layout: default
tags:
- factorial
- wren
title: Factorial in Wren
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/wren/how-to-implement-the-solution.md
- sources/programs/factorial/wren/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Wren](https://sampleprograms.io/languages/wren) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```wren
import "os" for Process

var args = Process.arguments

if (args.count < 1 || args[0].count < 1) {
  System.print("Usage: please input a non-negative integer")
  Fiber.suspend()
}

var n = Num.fromString(args[0])
if (n == null || n < 0) {
  System.print("Usage: please input a non-negative integer")
  Fiber.suspend()
}

if (n <= 1) {
  System.print(1)
  Fiber.suspend()
}

var res = 1
for (i in 1..n) {
  res = res * i
}

System.print(res)

```

{% endraw %}

Factorial in [Wren](https://sampleprograms.io/languages/wren) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).