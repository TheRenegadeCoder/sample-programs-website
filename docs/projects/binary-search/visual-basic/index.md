---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: binary-search-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- binary-search
- visual-basic
title: Binary Search in Visual Basic
title1: Binary Search
title2: in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/visual-basic/how-to-implement-the-solution.md
- sources/programs/binary-search/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Imports System

Module BinarySearch

    Sub Main(args As String())

        If args.Length <> 2 Then
            ShowUsage()
            Return
        End If

        Dim list = ParseList(args(0))
        Dim target As Integer

        If list Is Nothing OrElse Not Integer.TryParse(args(1), target) Then
            ShowUsage()
            Return
        End If

        If Not IsSorted(list) Then
            ShowUsage()
            Return
        End If

        Console.WriteLine(BinarySearch(list, target))

    End Sub

    Private Function ParseList(input As String) As List(Of Integer)

        Dim result As New List(Of Integer)

        For Each part In input.Split(","c)

            Dim value As Integer

            If Not Integer.TryParse(part.Trim(), value) Then
                Return Nothing
            End If

            result.Add(value)

        Next

        Return result

    End Function

    Private Function BinarySearch(list As List(Of Integer), target As Integer) As Boolean

        Dim low = 0
        Dim high = list.Count - 1

        While low <= high

            Dim mid = (low + high) \ 2

            If list(mid) = target Then
                Return True
            ElseIf list(mid) < target Then
                low = mid + 1
            Else
                high = mid - 1
            End If

        End While

        Return False

    End Function

    Private Function IsSorted(list As List(Of Integer)) As Boolean

        For i = 0 To list.Count - 2
            If list(i) > list(i + 1) Then
                Return False
            End If
        Next

        Return True

    End Function

    Private Sub ShowUsage()
        Console.WriteLine(
            "Usage: please provide a list of sorted integers " &
            "(""1, 4, 5, 11, 12"") and the integer to find (""11"")"
        )
    End Sub

End Module
```

{% endraw %}

Binary Search in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).