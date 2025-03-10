---
authors:
- rzuckerm
date: 2025-02-02
featured-image: even-odd-in-every-language.jpg
last-modified: 2025-02-02
layout: default
tags:
- even-odd
- ti-basic
title: Even Odd in Ti Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/ti-basic/how-to-implement-the-solution.md
- sources/programs/even-odd/ti-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Ti Basic](https://sampleprograms.io/languages/ti-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

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
While E=0 and N<=L
    sub(Str1,N,1)->C
    inString(Str2,C)-1->K
    If C="+" or C="-" Then D>0->E
    Else
        K<0->E
        D+1->D
        V*10+K->V
    End
    N+1->N
End
If E or D<1 Then Disp "Usage: please input a number"
Else
    If remainder(V,2)=0 Then Disp "Even"
    Else Disp "Odd"
    End
End

```

{% endraw %}

Even Odd in [Ti Basic](https://sampleprograms.io/languages/ti-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).