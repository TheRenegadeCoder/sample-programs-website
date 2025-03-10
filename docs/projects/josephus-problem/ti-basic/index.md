---
authors:
- rzuckerm
date: 2025-02-03
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2025-02-03
layout: default
tags:
- josephus-problem
- ti-basic
title: Josephus Problem in Ti Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/ti-basic/how-to-implement-the-solution.md
- sources/programs/josephus-problem/ti-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Ti Basic](https://sampleprograms.io/languages/ti-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ti_basic
"0123456789"->Str2
2->dim(l1)
1->M
0->E
While E=0 and M<=2
    Input "",Str1
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
    E or D<1->E
    V->l1(M)
    M+1->M
End
If E Then Disp "Usage: please input the total number of people and number of people to skip."
Else
    :"Source: https://en.wikipedia.org/wiki/Josephus_problem#The_general_case"
    0->G
    l1(1)->N
    l1(2)->K
    For(M,2,N)
        remainder(G+K,M)->G
    End
    Disp G+1
End

```

{% endraw %}

Josephus Problem in [Ti Basic](https://sampleprograms.io/languages/ti-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).