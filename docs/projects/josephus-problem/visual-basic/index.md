---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- josephus-problem
- visual-basic
title: Josephus Problem in Visual Basic
title1: Josephus Problem
title2: in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/visual-basic/how-to-implement-the-solution.md
- sources/programs/josephus-problem/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Module JosephusProblem

    Public Sub Main(args As String())

        If args.Length < 2 Then
            Console.WriteLine("Usage: please input the total number of people and number of people to skip.")
            Return
        End If

        Dim n As Integer
        Dim k As Integer

        If Not Integer.TryParse(args(0), n) OrElse
           Not Integer.TryParse(args(1), k) OrElse
           n <= 0 OrElse k <= 0 Then

            Console.WriteLine("Usage: please input the total number of people and number of people to skip.")
            Return
        End If

        Dim survivor As Integer = Josephus(n, k)

        Console.WriteLine(survivor)

    End Sub


    Private Function Josephus(n As Integer, k As Integer) As Integer

        Dim result As Integer = 0

        For m As Integer = 2 To n
            result = (result + k) Mod m
        Next

        Return result + 1

    End Function

End Module
```

{% endraw %}

Josephus Problem in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).