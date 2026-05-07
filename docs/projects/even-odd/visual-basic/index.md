---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: even-odd-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- even-odd
- visual-basic
title: Even Odd in Visual Basic
title1: Even Odd in
title2: Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/visual-basic/how-to-implement-the-solution.md
- sources/programs/even-odd/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Module EvenOdd

    Public Sub Main(args As String())

        If args.Length = 0 Then
            Console.WriteLine("Usage: please input a number")
            Environment.Exit(1)
        End If

        Dim n As Integer

        If Not Integer.TryParse(args(0), n) Then
            Console.WriteLine("Usage: please input a number")
            Environment.Exit(1)
        End If

        Dim result As String = If(n Mod 2 = 0, "Even", "Odd")

        Console.WriteLine(result)

    End Sub

End Module
```

{% endraw %}

Even Odd in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).