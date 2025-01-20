---
authors:
- rzuckerm
date: 2025-01-20
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-20
layout: default
tags:
- batch
- fizz-buzz
title: Fizz Buzz in Batch
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/batch/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/batch/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Batch](https://sampleprograms.io/languages/batch) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```batch
@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION

for /l %%i in (1,1,100) do (
    set /A "m3=%%i %% 3"
    set /A "m5=%%i %% 5"
    set /A "m15=%%i %% 15"

    if !m15! equ 0 (
        echo FizzBuzz
    ) else if !m3! equ 0 (
        echo Fizz
    ) else if !m5! equ 0 (
        echo Buzz
    ) else (
        echo %%i
    )
)

ENDLOCAL

```

{% endraw %}

Fizz Buzz in [Batch](https://sampleprograms.io/languages/batch) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).