---
authors:
- Jeremy Grifski
date: 2023-10-16
featured-image: baklava-in-every-language.jpg
last-modified: 2023-10-16
layout: default
tags:
- baklava
- pyret
title: Baklava in Pyret
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/pyret/how-to-implement-the-solution.md
- sources/programs/baklava/pyret/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Pyret](https://sampleprograms.io/languages/pyret) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pyret
fun print-row(n :: Number):
  spaces = string-repeat(" ", 10 - n)
  stars = string-repeat("*", (n * 2) + 1)
  print(spaces + stars + "\n")
end
  
range-by(0, 11, 1).each(print-row) 
range-by(9, -1, -1).each(print-row)
```

{% endraw %}

Baklava in [Pyret](https://sampleprograms.io/languages/pyret) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).