---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-18
featured-image: factorial-in-every-language.jpg
last-modified: 2026-04-18
layout: default
tags:
- cobol
- factorial
title: Factorial in COBOL
title1: Factorial
title2: in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/cobol/how-to-implement-the-solution.md
- sources/programs/factorial/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. factorial.

data division.
working-storage section.

01 cmd-args  pic x(38).
01 num       pic s9(7).
01 result    pic z(18)9 value 1.

procedure division.

main.
    accept cmd-args from command-line

    if function test-numval(cmd-args) not = 0
        perform show-usage
    end-if

    compute num = function numval(cmd-args)

    if num < 0
        perform show-usage
    end-if

    compute result = function factorial(num)
    display result

    stop run.

show-usage.
    display "Usage: please input a non-negative integer"
    stop run.

```

{% endraw %}

Factorial in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).