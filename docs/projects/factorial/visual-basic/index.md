---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: factorial-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- factorial
- visual-basic
title: Factorial in Visual Basic
title1: Factorial in
title2: Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/visual-basic/how-to-implement-the-solution.md
- sources/programs/factorial/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Imports System.Numerics

Module Factorial

    Private Function Fact(n As BigInteger) As BigInteger
        If n <= 1 Then
            Return 1
        End If

        Return n * Fact(n - 1)
    End Function


    Public Sub Main(args As String())

        If args.Length = 0 Then
            ShowUsage()
            Return
        End If

        Dim n As BigInteger

        If Not BigInteger.TryParse(args(0), n) Then
            ShowUsage()
            Return
        End If

        If n < 0 Then
            ShowUsage()
            Return
        End If

        If n > 4550 Then
            Console.WriteLine($"{n}! is out of the reasonable bounds for calculation.")
            Environment.Exit(1)
        End If

        Dim result = Fact(n)
        Console.WriteLine(result)

    End Sub


    Private Sub ShowUsage()
        Console.WriteLine("Usage: please input a non-negative integer")
        Environment.Exit(1)
    End Sub

End Module
```

{% endraw %}

Factorial in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).