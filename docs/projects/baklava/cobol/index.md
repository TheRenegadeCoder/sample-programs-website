---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-18
featured-image: baklava-in-every-language.jpg
last-modified: 2026-04-18
layout: default
tags:
- baklava
- cobol
title: Baklava in COBOL
title1: Baklava
title2: in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/cobol/how-to-implement-the-solution.md
- sources/programs/baklava/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. baklava.

data division.
working-storage section.

01 max-width        pic 9(2) value 21.
01 half-width       pic 9(2).

01 row              pic 9(2).
01 num-spaces       pic 9(2).
01 num-stars        pic 9(2).

01 space-line       pic x(21) value all spaces.
01 star-line        pic x(21) value all "*".

procedure division.
main.
    compute half-width = (max-width - 1) / 2

    perform varying row from 0 by 1 until row = max-width
        perform compute-line
        perform render-line
    end-perform

    stop run.

compute-line.
    compute num-spaces = function abs(row - half-width)
    compute num-stars  = max-width - (2 * num-spaces).

render-line.
    display space-line(1:num-spaces) with no advancing
    display star-line(1:num-stars).

```

{% endraw %}

Baklava in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).