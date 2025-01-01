---
authors:
- rzuckerm
date: 2025-01-01
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-01
layout: default
tags:
- baklava
- grain
title: Baklava in Grain
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/grain/how-to-implement-the-solution.md
- sources/programs/baklava/grain/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Grain](https://sampleprograms.io/languages/grain) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```grain
module Main

from "array" include Array
from "number" include Number
from "range" include Range
from "string" include String

let repeatString = (s, n) => Array.join("", Array.make(n, s))
let baklavaLine = (n) => {
  let numSpaces = Number.abs(n)
  let numStars = 21 - 2 * numSpaces
  return String.concat(repeatString(" ", numSpaces), repeatString("*", numStars))
}

Range.forEach(n => print(baklavaLine(n)), {rangeStart: -10, rangeEnd: 11})

```

{% endraw %}

Baklava in [Grain](https://sampleprograms.io/languages/grain) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).