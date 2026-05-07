---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-08
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2026-05-08
layout: default
tags:
- sleep-sort
- visual-basic
title: Sleep Sort in Visual Basic
title1: Sleep Sort in
title2: Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/sleep-sort/visual-basic/how-to-implement-the-solution.md
- sources/programs/sleep-sort/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Imports System.Collections.Concurrent

Public Module SleepSort

    Private Sub ShowUsage()
        Console.WriteLine("Usage: please provide a list of at least two integers to sort in the format ""1, 2, 3, 4, 5""")
        Environment.Exit(1)
    End Sub

    Public Sub Main(args As String())

        If args.Length <> 1 Then
            ShowUsage()
        End If

        Try
            Dim xs = args(0).
                Split(","c, StringSplitOptions.RemoveEmptyEntries).
                Select(Function(i) Integer.Parse(i.Trim())).
                ToList()

            If xs.Count <= 1 Then
                ShowUsage()
            End If

            Dim sortedXs As New ConcurrentQueue(Of Integer)
            Dim tasks As New List(Of Task)

            For Each x In xs

                Dim captured = x

                tasks.Add(Task.Run(Async Function()
                                       Await Task.Delay(captured * 1000)
                                       sortedXs.Enqueue(captured)
                                   End Function))

            Next

            Task.WaitAll(tasks.ToArray())

            Console.WriteLine(String.Join(", ", sortedXs))

        Catch
            ShowUsage()
        End Try

    End Sub

End Module
```

{% endraw %}

Sleep Sort in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).