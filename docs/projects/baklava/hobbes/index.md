---
authors:
- rzuckerm
date: 2025-01-01
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-01
layout: default
tags:
- baklava
- hobbes
title: Baklava in Hobbes
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/hobbes/how-to-implement-the-solution.md
- sources/programs/baklava/hobbes/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Hobbes](https://sampleprograms.io/languages/hobbes) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```hobbes
repeatString :: (string, int) -> string
repeatString s n = if (n > 0) then s ++ repeatString(s, n - 1) else ""

iabs :: int -> int
iabs n = if (n < 0) then -n else n

baklavaLine :: int -> string
baklavaLine n =
  let
    numSpaces = iabs(n);
    numStars = 21 - 2 * numSpaces
  in
    repeatString(" ", numSpaces) ++ repeatString("*", numStars)

baklava :: (int, int) -> ()
baklava n ne = if (n <= ne) then do {
  putStrLn(baklavaLine(n));
  baklava(n + 1, ne);
} else ()

baklava(-10, 10)

```

{% endraw %}

Baklava in [Hobbes](https://sampleprograms.io/languages/hobbes) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).