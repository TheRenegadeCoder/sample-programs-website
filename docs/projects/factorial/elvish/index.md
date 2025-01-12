---
authors:
- Zia
date: 2025-01-12
featured-image: factorial-in-every-language.jpg
last-modified: 2025-01-12
layout: default
tags:
- elvish
- factorial
title: Factorial in Elvish
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/elvish/how-to-implement-the-solution.md
- sources/programs/factorial/elvish/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Elvish](https://sampleprograms.io/languages/elvish) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elvish
if (> 1 (count $args)) {
  echo "Usage: please input a non-negative integer"
  exit 1
}

try {
  var r = (+ $args[0] 1) # Hacky, but it tries to add the argument with one.
} catch { # If it fails, the value is not a number.
  echo "Usage: please input a non-negative integer"
  exit 1
}

if (> 0 $args[0]) {
  echo "Usage: please input a non-negative integer"
  exit 1
}

var f = 1

for i [(range 1 (+ 1 $args[0]))] {
  set f = (* $f $i)
}

echo $f

```

{% endraw %}

Factorial in [Elvish](https://sampleprograms.io/languages/elvish) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).