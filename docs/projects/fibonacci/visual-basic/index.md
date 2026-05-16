---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: fibonacci-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- fibonacci
- visual-basic
title: Fibonacci in Visual Basic
title1: Fibonacci in
title2: Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/visual-basic/how-to-implement-the-solution.md
- sources/programs/fibonacci/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Imports System.Numerics

Module Fibonacci

    Public Sub Main(args As String())

        If args.Length = 0 Then
            ShowUsage()
            Return
        End If

        Dim n As Integer

        If Not Integer.TryParse(args(0), n) OrElse n < 0 Then
            ShowUsage()
            Return
        End If

        Dim first As BigInteger = 0
        Dim second As BigInteger = 1

        For i As Integer = 1 To n

            Dim current As BigInteger = first + second
            first = second
            second = current

            Console.WriteLine($"{i}: {first}")

        Next

    End Sub


    Private Sub ShowUsage()
        Console.WriteLine("Usage: please input the count of fibonacci numbers to output")
        Environment.Exit(1)
    End Sub

End Module
```

{% endraw %}

Fibonacci in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).