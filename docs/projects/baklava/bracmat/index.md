---
authors:
- rzuckerm
date: 2025-01-20
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-20
layout: default
tags:
- baklava
- bracmat
title: Baklava in Bracmat
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/bracmat/how-to-implement-the-solution.md
- sources/programs/baklava/bracmat/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Bracmat](https://sampleprograms.io/languages/bracmat) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```bracmat
{
Resources:
- https://rosettacode.org/wiki/Loops/For#Bracmat
}

{for n = -10 to 10}
  -11:?n
&   whl
  ' ( 1+!n:<11:?n
    { numspaces = abs(n) }
    & abs$(!n):?numspaces
    { numstars = 21 - 2 * numspaces}
    & 21+-2*!numspaces:?numstars
    { Output numspaces " "}
    & whl'(!numspaces+-1:~<0:?numspaces&put$" ")
    { Output numstars "*"}
    & whl'(!numstars+-1:~<0:?numstars&put$"*")
    { Output newline }
    & put$\n
    )

```

{% endraw %}

Baklava in [Bracmat](https://sampleprograms.io/languages/bracmat) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).