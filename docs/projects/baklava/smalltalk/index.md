---
authors:
- rzuckerm
date: 2024-10-22
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-22
layout: default
tags:
- baklava
- smalltalk
title: Baklava in Smalltalk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/smalltalk/how-to-implement-the-solution.md
- sources/programs/baklava/smalltalk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Smalltalk](https://sampleprograms.io/languages/smalltalk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```smalltalk
-10 to: 10 do: [ :i |
  numSpaces := i abs.
  numSpaces timesRepeat: [ ' ' display ].
  (21 - (2 * numSpaces)) timesRepeat: [ '*' display ].
  Character nl display.
]

```

{% endraw %}

Baklava in [Smalltalk](https://sampleprograms.io/languages/smalltalk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).