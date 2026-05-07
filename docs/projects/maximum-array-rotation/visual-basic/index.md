---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- maximum-array-rotation
- visual-basic
title: Maximum Array Rotation in Visual Basic
title1: Maximum Array Rotation
title2: in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/visual-basic/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Public Module MaximumArrayRotation

    Private Sub ShowUsage()
        Console.Error.WriteLine(
            "Usage: please provide a list of integers (e.g. ""8, 3, 1, 2"")"
        )
        Environment.Exit(1)
    End Sub


    Private Function ParseList(input As String) As List(Of Integer)

        If String.IsNullOrWhiteSpace(input) Then
            ShowUsage()
        End If

        Dim result As New List(Of Integer)

        For Each part In input.Split(","c, StringSplitOptions.RemoveEmptyEntries Or StringSplitOptions.TrimEntries)

            Dim value As Integer

            If Not Integer.TryParse(part, value) OrElse value < 0 Then
                ShowUsage()
            End If

            result.Add(value)

        Next

        If result.Count = 0 Then
            ShowUsage()
        End If

        Return result

    End Function


    Private Function MaximumRotationSum(numbers As List(Of Integer)) As Integer

        Dim n As Integer = numbers.Count

        If n = 0 Then
            ShowUsage()
        End If

        Dim totalSum As Integer = 0
        Dim currentWeightedSum As Integer = 0

        For i As Integer = 0 To n - 1
            totalSum += numbers(i)
            currentWeightedSum += numbers(i) * i
        Next

        Dim maxWeightedSum As Integer = currentWeightedSum

        For i As Integer = 1 To n - 1

            currentWeightedSum =
                currentWeightedSum + totalSum - n * numbers(n - i)

            If currentWeightedSum > maxWeightedSum Then
                maxWeightedSum = currentWeightedSum
            End If

        Next

        Return maxWeightedSum

    End Function


    Public Function Main(args As String()) As Integer

        If args.Length <> 1 Then
            ShowUsage()
        End If

        Dim inputList = ParseList(args(0))

        Console.WriteLine(MaximumRotationSum(inputList))

        Return 0

    End Function

End Module
```

{% endraw %}

Maximum Array Rotation in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).