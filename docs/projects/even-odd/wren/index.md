---
authors:
- Zia
date: 2025-01-20
featured-image: even-odd-in-every-language.jpg
last-modified: 2025-01-20
layout: default
tags:
- even-odd
- wren
title: Even Odd in Wren
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/wren/how-to-implement-the-solution.md
- sources/programs/even-odd/wren/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Wren](https://sampleprograms.io/languages/wren) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```wren
import "os" for Process

var args = Process.arguments // Process.args is a bit long and annoying to type.

if (args.count < 1 || args[0].count < 1) {
  System.print("Usage: please input a number")
  Fiber.suspend()
}

var n = Num.fromString(args[0])

if (n == null) {
  System.print("Usage: please input a number")
  Fiber.suspend()
}

if (n % 2 == 0) {
  System.print("Even")
} else {
  System.print("Odd")
}

```

{% endraw %}

Even Odd in [Wren](https://sampleprograms.io/languages/wren) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).