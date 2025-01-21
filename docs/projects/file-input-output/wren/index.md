---
authors:
- Zia
date: 2025-01-21
featured-image: file-input-output-in-every-language.jpg
last-modified: 2025-01-21
layout: default
tags:
- file-input-output
- wren
title: File Input Output in Wren
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/wren/how-to-implement-the-solution.md
- sources/programs/file-input-output/wren/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Wren](https://sampleprograms.io/languages/wren) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```wren
import "io" for File

File.create("output.txt") {|f|
  f.writeBytes("My brain has too many tabs open.")
}

System.print(File.read("output.txt"))

```

{% endraw %}

File Input Output in [Wren](https://sampleprograms.io/languages/wren) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).