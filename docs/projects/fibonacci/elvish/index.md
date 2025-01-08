---
authors:
- Zia
date: 2025-01-08
featured-image: fibonacci-in-every-language.jpg
last-modified: 2025-01-08
layout: default
tags:
- elvish
- fibonacci
title: Fibonacci in Elvish
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/elvish/how-to-implement-the-solution.md
- sources/programs/fibonacci/elvish/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Elvish](https://sampleprograms.io/languages/elvish) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elvish
if (> 1 (count $args)) {
  echo "Usage: please input the count of fibonacci numbers to output"
  exit 1
}

try {
  var r = (+ $args[0] 1) # Hacky, but it tries to add the argument with one.
} catch { # If it fails, the value is not a number.
  echo "Usage: please input the count of fibonacci numbers to output"
  exit 1
}

var a = 0
var b = 1
var c = 0

for i [(range 1 (+ $args[0] 1))] {
  set c = (+ $a $b)
  set a = $b
  set b = $c
  echo $i': '$a
}

```

{% endraw %}

Fibonacci in [Elvish](https://sampleprograms.io/languages/elvish) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).