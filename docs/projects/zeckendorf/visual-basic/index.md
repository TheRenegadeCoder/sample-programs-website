---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-05-07
layout: default
tags:
- visual-basic
- zeckendorf
title: Zeckendorf in Visual Basic
title1: Zeckendorf in
title2: Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/visual-basic/how-to-implement-the-solution.md
- sources/programs/zeckendorf/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Public Module Zeckendorf

    Private ReadOnly Fibs As Long() = GenerateFibs()


    Private Function GenerateFibs() As Long()

        Dim fs As New List(Of Long) From {1L, 2L}

        While Long.MaxValue - fs(fs.Count - 1) >= fs(fs.Count - 2)
            fs.Add(fs(fs.Count - 1) + fs(fs.Count - 2))
        End While

        Return fs.ToArray()

    End Function


    Public Sub Main(args As String())

        Dim n As Long

        If args.Length = 0 OrElse Not Long.TryParse(args(0), n) OrElse n < 0 Then

            Console.WriteLine("Usage: please input a non-negative integer")
            Return

        End If

        If n = 0 Then Return

        Dim terms As New List(Of Long)

        Dim count As Integer = Decompose(n, terms)

        Console.WriteLine(String.Join(", ", terms.GetRange(0, count)))

    End Sub


    Private Function Decompose(n As Long, terms As List(Of Long)) As Integer

        Dim count As Integer = 0

        Dim i As Integer = Array.BinarySearch(Fibs, n)

        If i < 0 Then
            i = Not i - 1
        End If

        For idx As Integer = i To 0 Step -1

            If n <= 0 Then Exit For

            If Fibs(idx) <= n Then
                terms.Add(Fibs(idx))
                n -= Fibs(idx)
                count += 1
            End If

        Next

        Return count

    End Function

End Module
```

{% endraw %}

Zeckendorf in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).