---
authors:
- rzuckerm
date: 2024-12-30
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-30
layout: default
tags:
- baklava
- mojiscript
title: Baklava in Mojiscript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/mojiscript/how-to-implement-the-solution.md
- sources/programs/baklava/mojiscript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Mojiscript](https://sampleprograms.io/languages/mojiscript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mojiscript
import log from 'mojiscript/console/log'
import pipe from 'mojiscript/core/pipe'
import run from 'mojiscript/core/run'
import map from 'mojiscript/list/map'
import range from 'mojiscript/list/range'

const numSpaces = n => Math.abs(n)
const numStars = n => 21 - 2 * numSpaces (n)
const baklavaLine = n => ' '.repeat(numSpaces (n)) + '*'.repeat(numStars (n))

const main = pipe([
    range (-10) (11),
    map (baklavaLine),
    map (log)
])

run({main})

```

{% endraw %}

Baklava in [Mojiscript](https://sampleprograms.io/languages/mojiscript) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).