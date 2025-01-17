---
authors:
- Zia
date: 2025-01-17
featured-image: prime-number-in-every-language.jpg
last-modified: 2025-01-17
layout: default
tags:
- elvish
- prime-number
title: Prime Number in Elvish
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/elvish/how-to-implement-the-solution.md
- sources/programs/prime-number/elvish/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Elvish](https://sampleprograms.io/languages/elvish) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elvish
use str
use math

fn die {
  echo 'Usage: please input a non-negative integer'
  exit 1
}

if (> 1 (count $args)) {
  die
}

var n = 0
try {
  set n = (num $args[0])
} catch _ {
  die
}

if (or (> 0 $n) (str:contains (to-string $n) .)) {
  die
}

if (> 2 $n) {
  echo 'composite'
  exit 0
}

if (== $n 2) {
  echo 'prime'
  exit 0
}

for i [(range 2 (+ 1 (exact-num (math:ceil (math:sqrt $n)))))] {
  if (== 0 (% $n $i)) {
    echo 'composite'
    exit 0
  }
}

echo 'prime'

```

{% endraw %}

Prime Number in [Elvish](https://sampleprograms.io/languages/elvish) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).