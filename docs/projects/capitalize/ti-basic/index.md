---
authors:
- rzuckerm
date: 2025-02-01
featured-image: capitalize-in-every-language.jpg
last-modified: 2025-02-01
layout: default
tags:
- capitalize
- ti-basic
title: Capitalize in Ti Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/ti-basic/how-to-implement-the-solution.md
- sources/programs/capitalize/ti-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Ti Basic](https://sampleprograms.io/languages/ti-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ti_basic
Input "",Str1
"abcdefghijklmnopqrstuvwxyz"->Str2
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"->Str3
If length(Str1)=0 Then Disp "Usage: please provide a string"
Else
    inString(Str2,sub(Str1,1,1))->N
    If N>0 Then Disp sub(Str3,N,1)+sub(Str1,2,length(Str1)-1)
    Else Disp Str1
    End
End

```

{% endraw %}

Capitalize in [Ti Basic](https://sampleprograms.io/languages/ti-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).