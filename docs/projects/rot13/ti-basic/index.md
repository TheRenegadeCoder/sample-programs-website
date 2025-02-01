---
authors:
- rzuckerm
date: 2025-02-01
featured-image: rot13-in-every-language.jpg
last-modified: 2025-02-01
layout: default
tags:
- rot13
- ti-basic
title: Rot13 in Ti Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/ti-basic/how-to-implement-the-solution.md
- sources/programs/rot13/ti-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Ti Basic](https://sampleprograms.io/languages/ti-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ti_basic
Input "",Str1
"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"->Str2
"nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"->Str3
length(Str1)->L
"Usage: please provide a string to encrypt"->Str4
If L>0 Then
    ""->Str4
    For(N,1,L)
        sub(Str1,N,1)->Str5
        inString(Str2,Str5)->K
        If K>0 Then Str4+sub(Str3,K,1)->Str4
        Else Str4+Str5->Str4
        End
    End
End
Disp Str4

```

{% endraw %}

Rot13 in [Ti Basic](https://sampleprograms.io/languages/ti-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).