---
authors:
- Zia
date: 2025-01-26
featured-image: prime-number-in-every-language.jpg
last-modified: 2025-01-26
layout: default
tags:
- prime-number
- wren
title: Prime Number in Wren
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/wren/how-to-implement-the-solution.md
- sources/programs/prime-number/wren/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Wren](https://sampleprograms.io/languages/wren) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

if (n == null || n < 0 || n.floor != n) {
  System.print("Usage: please input a non-negative integer")
  Fiber.suspend()
}

if (n < 2) {
  System.print("composite")
  Fiber.suspend()
}

if (n == 2) {
  System.print("prime")
  Fiber.suspend()
}

for (i in 2..(n.sqrt.floor)) {
  if (n % i == 0) {
    System.print("composite")
    Fiber.suspend()
  }
}
System.print("prime")

```

{% endraw %}

Prime Number in [Wren](https://sampleprograms.io/languages/wren) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).