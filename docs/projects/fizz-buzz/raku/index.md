---
authors:
- xavierb117
date: 2025-02-17
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-02-17
layout: default
tags:
- fizz-buzz
- raku
title: Fizz Buzz in Raku
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/raku/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/raku/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Raku](https://sampleprograms.io/languages/raku) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```raku
for 1..100 -> $i {
    if $i % 3 == 0 && $i % 5 == 0 {
        say "FizzBuzz"
    }
    elsif $i % 5 == 0 {
        say "Buzz"
    }
    elsif $i % 3 == 0 {
        say "Fizz"
    }
    else {
        say $i
    }
}
```

{% endraw %}

Fizz Buzz in [Raku](https://sampleprograms.io/languages/raku) was written by:

- xavierb117

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).