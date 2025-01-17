---
authors:
- rzuckerm
date: 2025-01-17
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-17
layout: default
tags:
- baklava
- cobol
title: Baklava in Cobol
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/cobol/how-to-implement-the-solution.md
- sources/programs/baklava/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Cobol](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
        IDENTIFICATION DIVISION.
        PROGRAM-ID. BAKLAVA.
        DATA DIVISION.
        WORKING-STORAGE SECTION.
            01  NUM             PIC 9(2).
            01  NUM-SPACES      PIC 9(2).
            01  NUM-STARS       PIC 9(2).
            01  BAKLAVA-SPACES  PIC X(10) VALUE SPACES.
            01  BAKLAVA-STARS   PIC X(21) VALUE ALL "*".

        PROCEDURE DIVISION.
            PERFORM VARYING NUM FROM 0 BY 1 UNTIL NUM > 20
                COMPUTE NUM-SPACES = FUNCTION ABS(NUM - 10)
                COMPUTE NUM-STARS = 21 - 2 * NUM-SPACES

      * Display NUM-SPACES " " without newline
                DISPLAY BAKLAVA-SPACES(1:NUM-SPACES) NO ADVANCING

      * Display NUM-STARS "*" with newline
                DISPLAY BAKLAVA-STARS(1:NUM-STARS)
            END-PERFORM
            STOP RUN.

```

{% endraw %}

Baklava in [Cobol](https://sampleprograms.io/languages/cobol) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).