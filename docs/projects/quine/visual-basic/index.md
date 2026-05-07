---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: quine-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- quine
- visual-basic
title: Quine in Visual Basic
title1: Quine in
title2: Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quine/visual-basic/how-to-implement-the-solution.md
- sources/programs/quine/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Module Quine
    Sub Main()
        Dim s As String = "Module Quine{0}    Sub Main(){0}        Dim s As String = {1}{2}{1}{0}        Console.WriteLine(s, Chr(10), Chr(34), s){0}    End Sub{0}End Module"
        Console.WriteLine(s, Chr(10), Chr(34), s)
    End Sub
End Module
```

{% endraw %}

Quine in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).