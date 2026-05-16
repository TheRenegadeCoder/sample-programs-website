---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- palindromic-number
- visual-basic
title: Palindromic Number in Visual Basic
title1: Palindromic Number
title2: in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/visual-basic/how-to-implement-the-solution.md
- sources/programs/palindromic-number/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Public Module PalindromeNumber

    Private Sub ShowUsage()
        Console.WriteLine("Usage: please input a non-negative integer")
        Environment.Exit(1)
    End Sub


    Private Function IsPalindromeNumber(value As Long) As Boolean

        If value < 0 Then Return False

        Dim original As Long = value
        Dim reversed As Long = 0

        While value > 0
            Dim digit As Long = value Mod 10
            reversed = reversed * 10 + digit
            value \= 10
        End While

        Return original = reversed

    End Function


    Public Function Main(args As String()) As Integer

        If args.Length <> 1 Then
            ShowUsage()
        End If

        Dim value As Long

        If Not Long.TryParse(args(0), value) OrElse value < 0 Then
            ShowUsage()
        End If

        Console.WriteLine(IsPalindromeNumber(value).ToString().ToLower())

        Return 0

    End Function

End Module
```

{% endraw %}

Palindromic Number in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).