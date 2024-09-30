---
authors:
- Sayantan Sarkar
date: 2020-10-09
featured-image: even-odd-in-every-language.jpg
last-modified: 2020-10-09
layout: default
tags:
- coffeescript
- even-odd
title: Even Odd in Coffeescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/coffeescript/how-to-implement-the-solution.md
- sources/programs/even-odd/coffeescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Coffeescript](https://sampleprograms.io/languages/coffeescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```coffeescript
USAGE = "Usage: please input a number"
main = (arg) ->
  numberParsed = parseInt(arg)
  isNumber = Number.isInteger(numberParsed)
  if isNumber
    if numberParsed % 2 == 0 then "Even" else "Odd"
  else
    USAGE

console.log main(process.argv[2])
```

{% endraw %}

Even Odd in [Coffeescript](https://sampleprograms.io/languages/coffeescript) was written by:

- Sayantan Sarkar

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).