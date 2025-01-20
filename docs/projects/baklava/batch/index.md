---
authors:
- rzuckerm
date: 2025-01-20
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-20
layout: default
tags:
- baklava
- batch
title: Baklava in Batch
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/batch/how-to-implement-the-solution.md
- sources/programs/baklava/batch/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Batch](https://sampleprograms.io/languages/batch) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```batch
@echo off

rem Reference: https://rosettacode.org/wiki/Loops/For#Batch_File
SETLOCAL ENABLEDELAYEDEXPANSION

for /l %%n in (0,1,20) do (
    rem num_spaces = abs(n - 10)
    set /a "num_spaces=%%n-10"
    if !num_spaces! lss 0 set /a "num_spaces=10-%%n"

    rem num_stars = 21 - 2 * num_spaces
    set /a "num_stars=21-(2*!num_spaces!)"

    rem Get num_spaces " "
    set "line="
    if !num_spaces! gtr 0 (
        for /l %%i in (1,1,!num_spaces!) do set "line=!line! "
    )

    rem Append num_stars "*"
    for /l %%i in (1,1,!num_stars!) do set "line=!line!*"

    rem Output line
    echo !line!
)

ENDLOCAL

```

{% endraw %}

Baklava in [Batch](https://sampleprograms.io/languages/batch) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).