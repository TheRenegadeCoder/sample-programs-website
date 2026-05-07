---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: rot13-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- rot13
- visual-basic
title: Rot13 in Visual Basic
title1: Rot13 in
title2: Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/visual-basic/how-to-implement-the-solution.md
- sources/programs/rot13/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Imports System.Text

Public Module Rot13

    Private Sub ShowUsage()
        Console.WriteLine("Usage: please provide a string to encrypt")
        Environment.Exit(1)
    End Sub


    Private Function EncryptChar(c As Char) As Char

        If c >= "A"c AndAlso c <= "Z"c Then
            Return ChrW(((AscW(c) - AscW("A"c) + 13) Mod 26) + AscW("A"c))
        End If

        If c >= "a"c AndAlso c <= "z"c Then
            Return ChrW(((AscW(c) - AscW("a"c) + 13) Mod 26) + AscW("a"c))
        End If

        Return c

    End Function


    Private Function Encrypt(input As String) As String

        Dim result As New StringBuilder(input.Length)

        For Each c As Char In input
            result.Append(EncryptChar(c))
        Next

        Return result.ToString()

    End Function


    Public Function Main(args As String()) As Integer

        If args Is Nothing OrElse args.Length = 0 OrElse String.IsNullOrEmpty(args(0)) Then
            ShowUsage()
        End If

        Console.WriteLine(Encrypt(args(0)))

        Return 0

    End Function

End Module
```

{% endraw %}

Rot13 in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).