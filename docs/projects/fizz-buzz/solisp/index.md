---
authors:
- Stuart Irwin
date: 2020-02-25
featured-image: fizz-buzz-in-every-language.png
last-modified: 2020-03-23
layout: default
tags:
- fizz-buzz
- solisp
title: Fizz Buzz in Solisp
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/solisp/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/solisp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Solisp](https://sampleprograms.io/languages/solisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```solisp
(Join (Map num (Seq 1 100)
	(Switch
        {(== (% num 3) (% num 5) 0) "FizzBuzz"}
        {(== (% num 3) 0) "Fizz"}
        {(== (% num 5) 0) "Buzz"}
        {true num}
    )
) "\n")
```

{% endraw %}

Fizz Buzz in [Solisp](https://sampleprograms.io/languages/solisp) was written by:

- Stuart Irwin

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).