---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- longest-palindromic-substring
- visual-basic
title: Longest Palindromic Substring in Visual Basic
title1: Longest Palindromic
title2: Substring in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/visual-basic/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Public Module LongestPalindromicSubstring

    Public Sub Main(args As String())

        If args.Length <> 1 Then
            Console.WriteLine("Usage: please provide a string that contains at least one palindrome")
            Return
        End If

        Dim input As String = args(0)

        If String.IsNullOrWhiteSpace(input) Then
            Console.WriteLine("Usage: please provide a string that contains at least one palindrome")
            Return
        End If

        Dim result = LongestPalindrome(input)
        If result.Length < 2 Then
            Console.WriteLine("Usage: please provide a string that contains at least one palindrome")
            Return
        End If

        Console.WriteLine(result)

    End Sub


    Public Function LongestPalindrome(s As String) As String

        Dim t As String = Preprocess(s)

        Dim n As Integer = t.Length
        Dim p(n - 1) As Integer

        Dim center As Integer = 0
        Dim right As Integer = 0

        Dim maxLen As Integer = 0
        Dim maxCenter As Integer = 0

        For i As Integer = 1 To n - 2

            Dim mirror As Integer = 2 * center - i

            If i < right Then
                p(i) = Math.Min(right - i, p(mirror))
            End If

            While t(i + p(i) + 1) = t(i - p(i) - 1)
                p(i) += 1
            End While

            If i + p(i) > right Then
                center = i
                right = i + p(i)
            End If

            If p(i) > maxLen Then
                maxLen = p(i)
                maxCenter = i
            End If

        Next

        Dim startIndex As Integer = (maxCenter - maxLen) \ 2
        Return s.Substring(startIndex, maxLen)

    End Function


    Private Function Preprocess(s As String) As String

        Dim result As String = "^#"

        For Each c As Char In s
            result &= c & "#"
        Next

        result &= "$"

        Return result

    End Function

End Module
```

{% endraw %}

Longest Palindromic Substring in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).