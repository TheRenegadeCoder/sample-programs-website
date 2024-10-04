---
authors:
- rzuckerm
date: 2024-10-03
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-03
layout: default
tags:
- baklava
- visual-basic
title: Baklava in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/visual-basic/how-to-implement-the-solution.md
- sources/programs/baklava/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Public Module Baklava
  Public Sub Main()
    Dim numSpaces As Integer
    For i As Integer = -10 To 10
        numSpaces = Math.Abs(i)
        System.Console.WriteLine(StrDup(numSpaces, " ") + StrDup(21 - 2 * numSpaces, "*"))
    Next i
  End Sub
End Module

```

{% endraw %}

Baklava in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).