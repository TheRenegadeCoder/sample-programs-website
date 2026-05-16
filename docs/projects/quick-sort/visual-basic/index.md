---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: quick-sort-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- quick-sort
- visual-basic
title: Quick Sort in Visual Basic
title1: Quick Sort in
title2: Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quick-sort/visual-basic/how-to-implement-the-solution.md
- sources/programs/quick-sort/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Public Module QuickSort

    Public Function Sort(Of T)(input As IEnumerable(Of T),
                               Optional compare As IComparer(Of T) = Nothing) As List(Of T)

        If compare Is Nothing Then
            compare = Comparer(Of T).Default
        End If

        Dim list As New List(Of T)(input)
        If list.Count < 2 Then Return list

        QuickSortInternal(list, 0, list.Count - 1, compare)
        Return list

    End Function


    Private Sub QuickSortInternal(Of T)(list As List(Of T),
                                       low As Integer,
                                       high As Integer,
                                       comparer As IComparer(Of T))

        If low >= high Then
            Return
        End If

        Dim pivotIndex As Integer = Partition(list, low, high, comparer)

        QuickSortInternal(list, low, pivotIndex - 1, comparer)
        QuickSortInternal(list, pivotIndex + 1, high, comparer)

    End Sub


    Private Function Partition(Of T)(list As List(Of T),
                                    low As Integer,
                                    high As Integer,
                                    comparer As IComparer(Of T)) As Integer

        Dim pivot = list(high)
        Dim i As Integer = low - 1

        For j As Integer = low To high - 1

            If comparer.Compare(list(j), pivot) <= 0 Then
                i += 1
                Swap(list, i, j)
            End If

        Next

        Swap(list, i + 1, high)

        Return i + 1

    End Function


    Private Sub Swap(Of T)(list As List(Of T), i As Integer, j As Integer)
        Dim temp = list(i)
        list(i) = list(j)
        list(j) = temp
    End Sub


    Private Sub ShowUsage()

        Console.WriteLine(
            "Usage: please provide a list of at least two integers to sort " &
            "in the format ""1, 2, 3, 4, 5"""
        )

        Environment.Exit(1)

    End Sub


    Public Sub Main(args As String())

        If args.Length <> 1 Then
            ShowUsage()
        End If

        Dim parts = args(0).Split(","c, StringSplitOptions.RemoveEmptyEntries)

        Dim numbers As New List(Of Integer)

        For Each p In parts

            Dim value As Integer

            If Not Integer.TryParse(p.Trim(), value) Then
                ShowUsage()
            End If

            numbers.Add(value)

        Next

        If numbers.Count < 2 Then
            ShowUsage()
        End If

        Dim sorted = Sort(numbers)

        Console.WriteLine(String.Join(", ", sorted))

    End Sub

End Module
```

{% endraw %}

Quick Sort in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).