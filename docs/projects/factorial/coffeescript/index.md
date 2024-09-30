---
authors:
- Hanyuan Li
- Jeremy Grifski
date: 2019-10-11
featured-image: factorial-in-every-language.jpg
last-modified: 2020-10-15
layout: default
tags:
- coffeescript
- factorial
title: Factorial in Coffeescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/coffeescript/how-to-implement-the-solution.md
- sources/programs/factorial/coffeescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Coffeescript](https://sampleprograms.io/languages/coffeescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```coffeescript
factorial = (n) ->
    return usage() if n < 0
    return 1 if n == "0"
    [1..n].reduce (x, y) -> x * y
    
usage = () ->
    "Usage: please input a non-negative integer"
    
main = () ->
    args = process.argv
    return factorial(args[2]) if args.length == 3 and isFinite(args[2]) and args[2] != ""
    usage()

console.log main()

```

{% endraw %}

Factorial in [Coffeescript](https://sampleprograms.io/languages/coffeescript) was written by:

- Hanyuan Li
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).