---
authors:
- Zia
date: 2025-01-25
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2025-01-25
layout: default
tags:
- remove-all-whitespace
- wren
title: Remove All Whitespace in Wren
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/wren/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/wren/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Wren](https://sampleprograms.io/languages/wren) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```wren
import "os" for Process

var args = Process.arguments

if (args.count < 1 || args[0].count < 1) {
  System.print("Usage: please provide a string")
  Fiber.suspend()
}

var s = ""

for (c in args[0]) {
  if (c != " " && c != "\n" && c != "\t" && c != "\r" && c != "\f") {
    s = s + c
  }
}

System.print(s)

```

{% endraw %}

Remove All Whitespace in [Wren](https://sampleprograms.io/languages/wren) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).