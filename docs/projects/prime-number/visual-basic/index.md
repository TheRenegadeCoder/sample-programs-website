---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: prime-number-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- prime-number
- visual-basic
title: Prime Number in Visual Basic
title1: Prime Number in
title2: Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/visual-basic/how-to-implement-the-solution.md
- sources/programs/prime-number/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Public Module PrimeNumber

    Private Sub ShowUsage()
        Console.WriteLine("Usage: please input a non-negative integer")
        Environment.Exit(1)
    End Sub

    Private Function IsPrime(value As ULong) As Boolean

        If value <= 1UL Then Return False
        If value <> 2UL AndAlso value Mod 2UL = 0 Then Return False

        Dim limit As ULong = CULng(Math.Sqrt(value))

        Dim i As ULong = 3UL
        While i <= limit

            If value Mod i = 0UL Then
                Return False
            End If

            i += 2UL

        End While

        Return True

    End Function


    Public Function Main(args As String()) As Integer

        If args.Length <> 1 Then
            ShowUsage()
        End If

        Dim value As ULong

        If Not ULong.TryParse(args(0), value) Then
            ShowUsage()
        End If

        Console.WriteLine((If(IsPrime(value), "Prime", "Composite")))

        Return 0

    End Function

End Module
```

{% endraw %}

Prime Number in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).