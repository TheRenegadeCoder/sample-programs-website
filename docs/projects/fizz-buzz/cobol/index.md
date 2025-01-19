---
authors:
- Zia
date: 2025-01-19
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-19
layout: default
tags:
- cobol
- fizz-buzz
title: Fizz Buzz in Cobol
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/cobol/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Cobol](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
       IDENTIFICATION DIVISION.
           PROGRAM-ID. FIZZ-BUZZ.
       	   AUTHOR. KAAMKIYA.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
           01 COUNTER       PIC 999 VALUE 1.
           01 FIZZ          PIC 999 VALUE 1.
           01 BUZZ          PIC 999 VALUE 1.
           01 RESULT-STRING PIC xxx.
           01 SPACE-COUNT   PIC 99 VALUE ZERO.
       PROCEDURE DIVISION.
           PERFORM 100 TIMES
                IF FIZZ = 3
                    THEN IF BUZZ = 5
                        THEN DISPLAY "FizzBuzz"
                        COMPUTE BUZZ = 0
                        ELSE DISPLAY "Fizz"
                        END-IF
                        COMPUTE FIZZ = 0
                    ELSE IF BUZZ = 5
                        THEN DISPLAY "Buzz"
                        COMPUTE BUZZ = 0
                    ELSE
                        MOVE 0 TO SPACE-COUNT
                        INSPECT COUNTER TALLYING SPACE-COUNT
                            FOR LEADING ZEROS
                        MOVE COUNTER
                            (SPACE-COUNT + 1 : 
                                LENGTH OF COUNTER - SPACE-COUNT)
                                    TO RESULT-STRING
                        DISPLAY RESULT-STRING
                    END-IF
                END-IF
                ADD 1 TO COUNTER
                ADD 1 TO FIZZ
                ADD 1 TO BUZZ
           END-PERFORM
       STOP RUN.

```

{% endraw %}

Fizz Buzz in [Cobol](https://sampleprograms.io/languages/cobol) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).