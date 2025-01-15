---
authors:
- Zia
date: 2025-01-15
featured-image: linear-search-in-every-language.jpg
last-modified: 2025-01-15
layout: default
tags:
- elvish
- linear-search
title: Linear Search in Elvish
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/elvish/how-to-implement-the-solution.md
- sources/programs/linear-search/elvish/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Elvish](https://sampleprograms.io/languages/elvish) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elvish
use str

fn die {
  echo 'Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")'
  exit 1
}

fn validate-num {|n|
  try {
    var _ = (+ 4 $n)
  } catch _ {
    die
  }
}

if (> 2 (count $args)) {
  die
}

var list = [(str:split ', ' $args[0])]
for i $list {
  validate-num $i
}

var key = $args[1]
validate-num $key

for i $list {
  if (== $i $key) {
    echo true
    exit
  }
}

echo false

```

{% endraw %}

Linear Search in [Elvish](https://sampleprograms.io/languages/elvish) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).