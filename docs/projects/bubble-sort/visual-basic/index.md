---
authors:
- rzuckerm
- Thomas Braccia
date: 2020-10-01
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2023-05-16
layout: default
tags:
- bubble-sort
- visual-basic
title: Bubble Sort in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/visual-basic/how-to-implement-the-solution.md
- sources/programs/bubble-sort/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Public Module BubbleSort
    Public Sub Main(args As String())
        Try
            ' Convert string to array of integers
            Dim listOfStringInputs As String() = args(0).Split(",")
            Dim n as Integer = UBound(listOfStringInputs)
            If n < 2
                Usage()
                Exit Sub
            End If
    
            Dim sortArray(n) As Integer
            For i As Integer = 0 To n
                sortArray(i) = Integer.Parse(listOfStringInputs(i))
            Next i

            ' Sort array
            BubbleSort(sortArray)
            
            ' Display array
            Dim first As Boolean = True
            For i As Integer = 0 To n
                If i <> 0
                    System.Console.Write(", ")
                End If
                    
                System.Console.Write(sortArray(i))
            Next i
            System.Console.WriteLine()
        Catch e As FormatException
            Usage()
        Catch e As IndexOutOfRangeException
            Usage()
        End Try
    End Sub

    Public Sub Usage()
        System.Console.WriteLine("Usage: please provide a list of at least two integers to sort in the format ""1, 2, 3, 4, 5""")
    End Sub

    Public Sub BubbleSort(ByRef sortArray As Integer())
        Dim holdInt As Integer
        Dim n As Integer = UBound(sortArray)
        For i As Integer = 0 To n - 1
            For x As Integer = i + 1 To n
                If sortArray(x) < sortArray(i) Then
                    holdInt = sortArray(x)
                    sortArray(x) = sortArray(i)
                    sortArray(i) = holdInt
                End If
            Next x
        Next i
    End Sub
End Module

```

{% endraw %}

Bubble Sort in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- rzuckerm
- Thomas Braccia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).