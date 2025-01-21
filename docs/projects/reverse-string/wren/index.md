---
authors:
- Zia
date: 2025-01-21
featured-image: reverse-string-in-every-language.jpg
last-modified: 2025-01-21
layout: default
tags:
- reverse-string
- wren
title: Reverse String in Wren
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/wren/how-to-implement-the-solution.md
- sources/programs/reverse-string/wren/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Wren](https://sampleprograms.io/languages/wren) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```wren
import "os" for Process

var args = Process.arguments

if (args.count < 1) {
  args.add("")
}

var rev = ""

for (c in args[0]) {
  rev = c + rev
}

System.print(rev)

```

{% endraw %}

Reverse String in [Wren](https://sampleprograms.io/languages/wren) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).