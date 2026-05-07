---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: file-input-output-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- file-input-output
- visual-basic
title: File Input Output in Visual Basic
title1: File Input Output
title2: in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/visual-basic/how-to-implement-the-solution.md
- sources/programs/file-input-output/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Imports System.IO

Module FileInputOutput

    Private Const FileName As String = "output.txt"
    Private Const Content As String = "Hello from VB.NET!"

    Public Sub WriteFile()
        File.WriteAllText(FileName, Content)
    End Sub

    Public Function ReadFile() As String
        Return File.ReadAllText(FileName)
    End Function

    Public Sub Main()

        Try
            WriteFile()
            Console.WriteLine(ReadFile())
        Catch ex As Exception
            Console.WriteLine($"File operation failed: {ex.Message}")
        End Try

    End Sub

End Module
```

{% endraw %}

File Input Output in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).