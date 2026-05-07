---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- remove-all-whitespace
- visual-basic
title: Remove All Whitespace in Visual Basic
title1: Remove All Whitespace
title2: in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/visual-basic/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Public Module RemoveAllWhitespace

    Private Sub ShowUsage()
        Console.WriteLine("Usage: please provide a string")
        Environment.Exit(1)
    End Sub


    Private Sub RemoveAllWhitespace(input As String)

        Dim result As New System.Text.StringBuilder()

        For Each ch As Char In input

            If Not Char.IsWhiteSpace(ch) Then
                result.Append(ch)
            End If

        Next

        Console.WriteLine(result.ToString())

    End Sub


    Public Function Main(args As String()) As Integer

        If args Is Nothing OrElse args.Length = 0 OrElse String.IsNullOrEmpty(args(0)) Then
            ShowUsage()
        End If

        RemoveAllWhitespace(args(0))

        Return 0

    End Function

End Module
```

{% endraw %}

Remove All Whitespace in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).