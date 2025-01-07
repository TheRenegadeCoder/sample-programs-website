---
authors:
- rzuckerm
date: 2025-01-06
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-06
layout: default
tags:
- baklava
- formality
title: Baklava in Formality
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/formality/how-to-implement-the-solution.md
- sources/programs/baklava/formality/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Formality](https://sampleprograms.io/languages/formality) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```formality
baklavaLine(n: Nat): String
  let numSpaces = if Nat.gte(n, 10) then Nat.sub(n, 10) else Nat.sub(10, n)
  let numStars = Nat.sub(21, Nat.mul(2, numSpaces))
  String.repeat(" ", numSpaces) | String.repeat("*", numStars) | "\n"

baklava(lines: String, n:Nat): String
  case n {
    zero: lines | baklavaLine(0),
    succ: lines | baklavaLine(n) | baklava(lines, n.pred)
  }

Main: IO(Unit)
  do IO {
    IO.put_string(baklava("", 20))
  }

```

{% endraw %}

Baklava in [Formality](https://sampleprograms.io/languages/formality) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).