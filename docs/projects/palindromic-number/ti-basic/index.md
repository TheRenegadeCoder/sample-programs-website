---
authors:
- rzuckerm
date: 2025-02-02
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2025-02-02
layout: default
tags:
- palindromic-number
- ti-basic
title: Palindromic Number in Ti Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/ti-basic/how-to-implement-the-solution.md
- sources/programs/palindromic-number/ti-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Ti Basic](https://sampleprograms.io/languages/ti-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ti_basic
Input "",Str1
"0123456789"->Str2
length(Str1)->L
L<1->E
0->D
0->V
1->N
1->S
While E=0 and N<=L
    sub(Str1,N,1)->C
    inString(Str2,C)-1->K
    If C="+" or C="-"
    Then
        D>0->E
        If C="-"
        Then 0-S->S
        End
    Else
        K<0->E
        D+1->D
        V*10+K*S->V
    End
    N+1->N
End
If E or D<1 or V<0 Then Disp "Usage: please input a non-negative integer"
Else
    V->T
    0->R
    While T>0
        10*R+remainder(T,10)->R
        int(T/10)->T
    End
    If R=V Then Disp "true"
    Else Disp "false"
    End
End

```

{% endraw %}

Palindromic Number in [Ti Basic](https://sampleprograms.io/languages/ti-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).