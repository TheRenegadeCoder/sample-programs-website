---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: linear-search-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- linear-search
- visual-basic
title: Linear Search in Visual Basic
title1: Linear Search
title2: in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/visual-basic/how-to-implement-the-solution.md
- sources/programs/linear-search/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Module LinearSearch

    Public Sub Main(args As String())

        If args.Length < 2 Then
            ShowUsage()
            Return
        End If

        Dim list = ParseList(args(0))
        Dim target As Integer

        If list Is Nothing OrElse
           Not Integer.TryParse(args(1), target) Then

            ShowUsage()
            Return
        End If

        Console.WriteLine(Search(list, target))

    End Sub


    Private Function Search(list As List(Of Integer), target As Integer) As Boolean

        For Each value In list
            If value = target Then
                Return True
            End If
        Next

        Return False

    End Function


    Private Function ParseList(input As String) As List(Of Integer)

        If String.IsNullOrWhiteSpace(input) Then
            Return Nothing
        End If

        Dim result As New List(Of Integer)

        For Each part In input.Split(","c, StringSplitOptions.RemoveEmptyEntries)

            Dim value As Integer

            If Not Integer.TryParse(part.Trim(), value) Then
                Return Nothing
            End If

            result.Add(value)

        Next

        Return result

    End Function


    Private Sub ShowUsage()
        Console.WriteLine("Usage: please provide a list of integers (""1, 4, 5, 11, 12"") and the integer to find (""11"")")
        Environment.Exit(1)
    End Sub

End Module
```

{% endraw %}

Linear Search in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).