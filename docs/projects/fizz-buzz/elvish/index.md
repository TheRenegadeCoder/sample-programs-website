---
authors:
- Zia
date: 2025-01-08
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-08
layout: default
tags:
- elvish
- fizz-buzz
title: Fizz Buzz in Elvish
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/elvish/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/elvish/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Elvish](https://sampleprograms.io/languages/elvish) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elvish
for i [(range 1 101)] {
  if (== (% $i 15) 0) {
    echo FizzBuzz
  } elif (== (% $i 5) 0) {
    echo Buzz
  } elif (== (% $i 3) 0) {
    echo Fizz
  } else {
    echo $i
  }
}

```

{% endraw %}

Fizz Buzz in [Elvish](https://sampleprograms.io/languages/elvish) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).