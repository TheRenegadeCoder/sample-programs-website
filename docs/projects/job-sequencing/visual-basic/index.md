---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: job-sequencing-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- job-sequencing
- visual-basic
title: Job Sequencing in Visual Basic
title1: Job Sequencing
title2: in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/job-sequencing/visual-basic/how-to-implement-the-solution.md
- sources/programs/job-sequencing/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Public Class Job
    Public Property Profit As Integer
    Public Property Deadline As Integer

    Public Sub New(profit As Integer, deadline As Integer)
        Me.Profit = profit
        Me.Deadline = deadline
    End Sub
End Class


Public Module JobSequencing

    Public Sub Main(args As String())

        If args.Length <> 2 Then
            Console.WriteLine("Usage: please provide a list of profits and a list of deadlines")
            Return
        End If

        Dim profits = ParseIntList(args(0))
        Dim deadlines = ParseIntList(args(1))

        If profits Is Nothing OrElse deadlines Is Nothing OrElse
           profits.Count <> deadlines.Count Then

            Console.WriteLine("Usage: please provide a list of profits and a list of deadlines")
            Return
        End If

        Dim jobs As New List(Of Job)

        For i As Integer = 0 To profits.Count - 1
            jobs.Add(New Job(profits(i), deadlines(i)))
        Next

        Dim selected = GetMaxProfitJobSequence(jobs)

        Dim totalProfit As Integer = 0

        For Each job In selected
            totalProfit += job.Profit
        Next

        Console.WriteLine(totalProfit)

    End Sub


    Private Function ParseIntList(input As String) As List(Of Integer)

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


    Public Function GetMaxProfitJobSequence(jobs As List(Of Job)) As List(Of Job)

        jobs.Sort(Function(a, b) b.Profit.CompareTo(a.Profit))

        Dim maxDeadline As Integer = 0

        For Each job In jobs
            If job.Deadline > maxDeadline Then
                maxDeadline = job.Deadline
            End If
        Next

        Dim timeSlots(maxDeadline - 1) As Boolean
        Dim selected As New List(Of Job)

        For Each job In jobs

            For i As Integer = job.Deadline - 1 To 0 Step -1

                If Not timeSlots(i) Then
                    timeSlots(i) = True
                    selected.Add(job)
                    Exit For
                End If

            Next

        Next

        Return selected

    End Function

End Module
```

{% endraw %}

Job Sequencing in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).