---
authors:
- rzuckerm
date: 2025-02-01
featured-image: baklava-in-every-language.jpg
last-modified: 2025-02-01
layout: default
tags:
- baklava
- ti-basic
title: Baklava in Ti Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/ti-basic/how-to-implement-the-solution.md
- sources/programs/baklava/ti-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Ti Basic](https://sampleprograms.io/languages/ti-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ti_basic
For(N,0,20)
    abs(10-N)->S
    21-2*S->T
    ""->Str1
    For(I,1,S)
        Str1+" "->Str1
    End
    For(I,1,T)
        Str1+"*"->Str1
    End
    Disp Str1
End

```

{% endraw %}

Baklava in [Ti Basic](https://sampleprograms.io/languages/ti-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).