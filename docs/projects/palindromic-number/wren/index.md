---
authors:
- Zia
date: 2025-01-21
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2025-01-21
layout: default
tags:
- palindromic-number
- wren
title: Palindromic Number in Wren
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/wren/how-to-implement-the-solution.md
- sources/programs/palindromic-number/wren/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Wren](https://sampleprograms.io/languages/wren) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```wren
import "os" for Process

var args = Process.arguments

if (args.count < 1 || args[0].count < 1) {
  System.print("Usage: please input a non-negative integer")
  Fiber.suspend()
}

var s = args[0]
var n = Num.fromString(s)

if (n == null || n < 0) {
  System.print("Usage: please input a non-negative integer")
  Fiber.suspend()
}

var a = ""

for (c in s) {
  a = c + a
  if (c == ".") {
    System.print("Usage: please input a non-negative integer")
    Fiber.suspend()
  }
}

System.print(a == s)

```

{% endraw %}

Palindromic Number in [Wren](https://sampleprograms.io/languages/wren) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).