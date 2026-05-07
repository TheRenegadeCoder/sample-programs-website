---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: convex-hull-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- convex-hull
- visual-basic
title: Convex Hull in Visual Basic
title1: Convex Hull in
title2: Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/convex-hull/visual-basic/how-to-implement-the-solution.md
- sources/programs/convex-hull/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Convex Hull](https://sampleprograms.io/projects/convex-hull) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Module ConvexHull

    Public Structure Point
        Implements IComparable(Of Point)

        Public ReadOnly X As Integer
        Public ReadOnly Y As Integer

        Public Sub New(x As Integer, y As Integer)
            Me.X = x
            Me.Y = y
        End Sub

        Public Function CompareTo(other As Point) As Integer _
        Implements IComparable(Of Point).CompareTo

            Dim cx = X.CompareTo(other.X)
            If cx <> 0 Then Return cx
            Return Y.CompareTo(other.Y)
        End Function

        Public Overrides Function ToString() As String
            Return $"({X}, {Y})"
        End Function
    End Structure

    Sub Main(args As String())

        If args.Length <> 2 Then
            ShowUsage()
            Return
        End If

        Dim xCoords = ParseList(args(0))
        Dim yCoords = ParseList(args(1))

        If xCoords Is Nothing OrElse yCoords Is Nothing OrElse
           xCoords.Count <> yCoords.Count OrElse xCoords.Count < 3 Then

            ShowUsage()
            Return
        End If

        Dim points As New List(Of Point)(xCoords.Count)

        For i = 0 To xCoords.Count - 1
            points.Add(New Point(xCoords(i), yCoords(i)))
        Next

        Dim hull = BuildHull(points)

        For Each p In hull
            Console.WriteLine(p)
        Next

    End Sub

    Private Function BuildHull(points As List(Of Point)) As List(Of Point)

        Dim n = points.Count
        Dim hull As New List(Of Point)

        Dim start = 0
        For i = 1 To n - 1
            If points(i).CompareTo(points(start)) < 0 Then
                start = i
            End If
        Next

        Dim current = start

        Do
            hull.Add(points(current))

            Dim nextIdx = If(current + 1 = n, 0, current + 1)

            For i = 0 To n - 1
                If Cross(points(current), points(i), points(nextIdx)) > 0 Then
                    nextIdx = i
                End If
            Next

            current = nextIdx

        Loop While current <> start

        Return hull

    End Function

    Private Function Cross(o As Point, a As Point, b As Point) As Long
        Return CLng(a.X - o.X) * (b.Y - o.Y) -
               CLng(a.Y - o.Y) * (b.X - o.X)
    End Function

    Private Function ParseList(input As String) As List(Of Integer)

        If String.IsNullOrWhiteSpace(input) Then
            Return Nothing
        End If

        Dim result As New List(Of Integer)

        For Each part In input.Split(","c)

            Dim value As Integer

            If Not Integer.TryParse(part.Trim(), value) Then
                Return Nothing
            End If

            result.Add(value)

        Next

        If result.Count < 3 Then
            Return Nothing
        End If

        Return result

    End Function

    Private Sub ShowUsage()
        Console.Error.WriteLine(
            "Usage: please provide at least 3 x and y coordinates as separate lists (e.g. ""100, 440, 210"")"
        )
    End Sub

End Module
```

{% endraw %}

Convex Hull in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).