---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-24
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2026-04-24
layout: default
tags:
- roman-numeral
- visual-basic
title: Roman Numeral in Visual Basic
title1: Roman Numeral
title2: in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/visual-basic/how-to-implement-the-solution.md
- sources/programs/roman-numeral/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Imports System
Imports System.Collections.Generic
Imports System.Linq

Module RomanNumeral

    Private Function GetValue(c As Char) As Integer
        Select Case c
            Case "M"c : Return 1000
            Case "D"c : Return 500
            Case "C"c : Return 100
            Case "L"c : Return 50
            Case "X"c : Return 10
            Case "V"c : Return 5
            Case "I"c : Return 1
            Case Else
                Throw New ArgumentException("Invalid Roman numeral character")
        End Select
    End Function

    Private Function RomanToDecimal(roman As String) As Integer
        Dim total As Integer = 0
        Dim lastValue As Integer = 0

        For i As Integer = roman.Length - 1 To 0 Step -1
            Dim currentValue As Integer = GetValue(roman(i))

            If currentValue < lastValue Then
                total -= currentValue
            Else
                total += currentValue
            End If

            lastValue = currentValue
        Next

        Return total
    End Function

    Sub Main(args As String())
        If args.Length = 0 Then
            Console.WriteLine("Usage: please provide a string of roman numerals")
            Return
        End If

        If args(0) = "" Then
            Console.WriteLine(0)
            Return
        End If

        Try
            Console.WriteLine(RomanToDecimal(args(0).ToUpperInvariant()))
        Catch ex As ArgumentException
            Console.WriteLine("Error: invalid string of roman numerals")
        End Try
    End Sub

End Module
```

{% endraw %}

Roman Numeral in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).