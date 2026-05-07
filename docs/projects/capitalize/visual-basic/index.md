---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: capitalize-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- capitalize
- visual-basic
title: Capitalize in Visual Basic
title1: Capitalize in
title2: Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/visual-basic/how-to-implement-the-solution.md
- sources/programs/capitalize/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Module Capitalize

    Sub Main(args As String())

        If args.Length = 0 OrElse String.IsNullOrWhiteSpace(args(0)) Then
            Console.WriteLine("Usage: please provide a string")
            Return
        End If

        Dim input = args(0)

        Dim output =
            Char.ToUpperInvariant(input(0)) &
            If(input.Length > 1, input.Substring(1), String.Empty)

        Console.WriteLine(output)

    End Sub

End Module
```

{% endraw %}

Capitalize in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).