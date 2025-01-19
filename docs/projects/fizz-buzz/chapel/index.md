---
authors:
- Zia
date: 2025-01-19
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-19
layout: default
tags:
- chapel
- fizz-buzz
title: Fizz Buzz in Chapel
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/chapel/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/chapel/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Chapel](https://sampleprograms.io/languages/chapel) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```chapel
for i in 1..100 do
  if (i % 15 == 0) {
    writeln("FizzBuzz");
  } else if (i % 5 == 0) {
    writeln("Buzz");
  } else if (i % 3 == 0) {
    writeln("Fizz");
  } else {
    writeln(i);
  }

```

{% endraw %}

Fizz Buzz in [Chapel](https://sampleprograms.io/languages/chapel) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).