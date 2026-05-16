---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- duplicate-character-counter
- visual-basic
title: Duplicate Character Counter in Visual Basic
title1: Duplicate Character
title2: Counter in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/visual-basic/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Imports System.Text

Public Module DuplicateCharacterCounter

    Public Sub Main(args As String())

        If args.Length = 0 OrElse String.IsNullOrEmpty(args(0)) Then
            Console.WriteLine("Usage: please provide a string")
            Return
        End If

        Dim input As String = args(0)

        Dim countMap As New Dictionary(Of Char, Integer)

        For Each c As Char In input

            If countMap.ContainsKey(c) Then
                countMap(c) += 1
            Else
                countMap(c) = 1
            End If

        Next

        Dim result As New StringBuilder()
        Dim seen As New HashSet(Of Char)

        For Each c As Char In input

            If countMap(c) > 1 AndAlso Not seen.Contains(c) Then
                result.AppendLine($"{c}: {countMap(c)}")
                seen.Add(c)
            End If

        Next

        If result.Length = 0 Then
            Console.WriteLine("No duplicate characters")
        Else
            Console.WriteLine(result.ToString().TrimEnd())
        End If

    End Sub

End Module
```

{% endraw %}

Duplicate Character Counter in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).