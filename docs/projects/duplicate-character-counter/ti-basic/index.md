---
authors:
- rzuckerm
date: 2025-02-03
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2025-02-03
layout: default
tags:
- duplicate-character-counter
- ti-basic
title: Duplicate Character Counter in Ti Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/ti-basic/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/ti-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Ti Basic](https://sampleprograms.io/languages/ti-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ti_basic
Input "",Str1
length(Str1)->L
If L<1 Then Disp "Usage: please provide a string"
Else
    {}->l1
    ""->Str2
    0->M
    For(N,1,L)
        sub(Str1,N,1)->C
        inString(Str2,C)->K
        If K<1
        Then
            Str2+C->Str2
            M+1->M
            M->dim(l1)
            1->l1(M)
        Else
            l1(K)+1->l1(K)
        End
    End
    0->D
    For(N,1,M)
        If l1(N)>1
        Then
            Disp sub(Str2,N,1)+": "+toString(l1(N))
            1->D
        End
    End
    If D=0
    Then Disp "No duplicate characters"
    End
End

```

{% endraw %}

Duplicate Character Counter in [Ti Basic](https://sampleprograms.io/languages/ti-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).