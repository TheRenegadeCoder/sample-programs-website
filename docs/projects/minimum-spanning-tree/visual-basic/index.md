---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: minimum-spanning-tree-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- minimum-spanning-tree
- visual-basic
title: Minimum Spanning Tree in Visual Basic
title1: Minimum Spanning
title2: Tree in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/minimum-spanning-tree/visual-basic/how-to-implement-the-solution.md
- sources/programs/minimum-spanning-tree/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Minimum Spanning Tree](https://sampleprograms.io/projects/minimum-spanning-tree) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Public Module MinimumSpanningTree

    Private Sub ShowUsage()
        Console.Error.WriteLine(
            "Usage: please provide a comma-separated list of integers"
        )
        Environment.Exit(1)
    End Sub


    Private Function ParseMatrix(input As String) As List(Of Integer)

        If String.IsNullOrWhiteSpace(input) Then
            ShowUsage()
        End If

        Dim result As New List(Of Integer)

        For Each token In input.Split(","c, StringSplitOptions.RemoveEmptyEntries Or StringSplitOptions.TrimEntries)

            Dim value As Integer
            If Not Integer.TryParse(token, value) Then
                ShowUsage()
            End If

            result.Add(value)

        Next

        If result.Count < 4 Then
            ShowUsage()
        End If

        Dim dimension As Integer = CInt(Math.Sqrt(result.Count))

        If dimension * dimension <> result.Count Then
            ShowUsage()
        End If

        Return result

    End Function


    Private Function MinimumSpanningTreeWeight(matrix As List(Of Integer), dimension As Integer) As Integer

        Dim inMST(dimension - 1) As Boolean
        Dim minEdge(dimension - 1) As Integer

        For i As Integer = 0 To dimension - 1
            minEdge(i) = Integer.MaxValue
        Next

        minEdge(0) = 0
        Dim totalWeight As Integer = 0

        For i As Integer = 0 To dimension - 1

            Dim minValue As Integer = Integer.MaxValue
            Dim node As Integer = -1

            For j As Integer = 0 To dimension - 1
                If Not inMST(j) AndAlso minEdge(j) < minValue Then
                    minValue = minEdge(j)
                    node = j
                End If
            Next

            If node = -1 Then
                ShowUsage()
            End If

            inMST(node) = True
            totalWeight += minValue

            For adj As Integer = 0 To dimension - 1

                Dim weight As Integer = matrix(node * dimension + adj)

                If weight <> 0 AndAlso Not inMST(adj) AndAlso weight < minEdge(adj) Then
                    minEdge(adj) = weight
                End If

            Next

        Next

        Return totalWeight

    End Function


    Public Function Main(args As String()) As Integer

        If args.Length <> 1 Then
            ShowUsage()
        End If

        Dim matrix = ParseMatrix(args(0))
        Dim dimension As Integer = CInt(Math.Sqrt(matrix.Count))

        Dim result = MinimumSpanningTreeWeight(matrix, dimension)

        Console.WriteLine(result)

        Return 0

    End Function

End Module
```

{% endraw %}

Minimum Spanning Tree in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).