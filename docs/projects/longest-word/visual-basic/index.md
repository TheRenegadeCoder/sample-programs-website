---
authors:
- JSaiyan
date: 2025-02-18
featured-image: longest-word-in-every-language.jpg
last-modified: 2025-02-18
layout: default
tags:
- longest-word
- visual-basic
title: Longest Word in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/visual-basic/how-to-implement-the-solution.md
- sources/programs/longest-word/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Public Module LongestWord
    Public Sub Main(args As String())
        ' Check if input is provided
        If args.Length = 0 Then
            Usage()
            Exit Sub
        End If

        ' Join the arguments to form the full input string
        Dim multi As String = String.Join(" ", args).Trim()

        ' Replace newlines, carriage returns, and tabs with spaces
        multi = multi.Replace(vbCrLf, " ").Replace(vbCr, " ").Replace(vbLf, " ").Replace(vbTab, " ")

        ' Split the string into words by spaces, removing empty entries
        Dim words As String() = multi.Split(" "c, StringSplitOptions.RemoveEmptyEntries)

        ' If there are no words, print usage
        If words.Length = 0 Then
            Usage()
            Exit Sub
        End If

        ' Find the longest word length
        Dim longestWord As String = ""
        Dim maxLength As Integer = 0

        ' Loop through the words and find the longest
        For Each word As String In words
            If word.Length > maxLength Then
                longestWord = word
                maxLength = word.Length
            End If
        Next

        ' Output the length of the longest word
        System.Console.WriteLine(maxLength)
    End Sub

    Public Sub Usage()
        System.Console.WriteLine("Usage: please provide a string")
    End Sub
End Module
```

{% endraw %}

Longest Word in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- JSaiyan

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).