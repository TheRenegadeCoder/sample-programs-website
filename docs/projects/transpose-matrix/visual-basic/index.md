---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- transpose-matrix
- visual-basic
title: Transpose Matrix in Visual Basic
title1: Transpose Matrix
title2: in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/visual-basic/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Public Module TransposeMatrix

    Private Sub ShowUsage()
        Console.Error.WriteLine("Usage: please enter the dimension of the matrix and the serialized matrix")
        Environment.Exit(1)
    End Sub


    Private Function ParseIntegerList(input As String) As List(Of Integer)

        If String.IsNullOrWhiteSpace(input) Then
            ShowUsage()
        End If

        Dim numbers As New List(Of Integer)

        For Each token In input.Split(","c, StringSplitOptions.RemoveEmptyEntries Or StringSplitOptions.TrimEntries)

            Dim value As Integer

            If Not Integer.TryParse(token, value) Then
                ShowUsage()
            End If

            numbers.Add(value)

        Next

        Return numbers

    End Function


    Private Function TransposeMatrix(cols As Integer, rows As Integer, input As List(Of Integer)) As List(Of Integer)

        Dim result As New List(Of Integer)(New Integer(rows * cols - 1) {})

        For i As Integer = 0 To rows - 1

            For j As Integer = 0 To cols - 1

                Dim sourceIndex As Integer = i * cols + j
                Dim targetIndex As Integer = j * rows + i

                result(targetIndex) = input(sourceIndex)

            Next

        Next

        Return result

    End Function


    Public Sub Main(args As String())

        If args.Length <> 3 Then
            ShowUsage()
        End If

        Dim cols As Integer
        Dim rows As Integer

        If Not Integer.TryParse(args(0), cols) OrElse Not Integer.TryParse(args(1), rows) Then
            ShowUsage()
        End If

        Dim numbers = ParseIntegerList(args(2))

        If numbers.Count <> cols * rows Then
            ShowUsage()
        End If

        Dim transposed = TransposeMatrix(cols, rows, numbers)

        Console.WriteLine(String.Join(", ", transposed))

    End Sub

End Module
```

{% endraw %}

Transpose Matrix in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).