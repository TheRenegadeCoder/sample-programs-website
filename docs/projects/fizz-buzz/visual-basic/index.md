---
authors:
- rzuckerm
- Thomas Braccia
date: 2020-10-01
featured-image: fizz-buzz-in-every-language.png
last-modified: 2023-05-16
layout: default
tags:
- fizz-buzz
- visual-basic
title: Fizz Buzz in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/visual-basic/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Option Explicit On
Module FizzBuzz
    Public Sub Main()
        FizzBuzz()
    End Sub
    Sub FizzBuzz()
        Dim i As Integer
        For i = 1 To 100
            If i Mod 15 = 0 Then
                System.Console.WriteLine("FizzBuzz")
            ElseIf i Mod 5 = 0 Then
                System.Console.WriteLine("Buzz")
            ElseIf i Mod 3 = 0 Then
                System.Console.WriteLine("Fizz")
            Else
                System.Console.WriteLine(i)
            End If
        Next
    End Sub
End Module

```

{% endraw %}

Fizz Buzz in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- rzuckerm
- Thomas Braccia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).