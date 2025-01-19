---
authors:
- Zia
date: 2025-01-19
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-19
layout: default
tags:
- fizz-buzz
- forth
title: Fizz Buzz in Forth
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/forth/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/forth/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Forth](https://sampleprograms.io/languages/forth) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```forth
: divisible
  mod 0=
;

: fizz-buzz
  dup 15 divisible if
    drop
    ." FizzBuzz"
  else
    dup 5 divisible if
      drop
      ." Buzz"
    else
      dup 3 divisible if
        drop
        ." Fizz"
      else
        .
      endif
    endif
  endif
;

: fizz-buzz-loop
  101 1 do i fizz-buzz cr loop
;

fizz-buzz-loop
bye

```

{% endraw %}

Fizz Buzz in [Forth](https://sampleprograms.io/languages/forth) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).