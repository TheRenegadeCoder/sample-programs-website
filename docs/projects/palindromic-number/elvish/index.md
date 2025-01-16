---
authors:
- Zia
date: 2025-01-16
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2025-01-16
layout: default
tags:
- elvish
- palindromic-number
title: Palindromic Number in Elvish
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/elvish/how-to-implement-the-solution.md
- sources/programs/palindromic-number/elvish/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Elvish](https://sampleprograms.io/languages/elvish) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elvish
use str

fn die {
  echo 'Usage: please input a non-negative integer'
  exit 1
}

if (> 1 (count $args)) {
  die
}

var n = $args[0]

# Check if the number contains a decimal point
if (str:contains $n .) {
  die
}

try {
  var q = (+ $n 1)
} catch _ {
  die
}

if (> 0 $n) {
  die
}

if (eq $n (echo $n|rev)) {
  echo true
} else {
  echo false
}

```

{% endraw %}

Palindromic Number in [Elvish](https://sampleprograms.io/languages/elvish) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).