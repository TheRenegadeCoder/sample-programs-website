---
authors:
- Ben Hekster
date: 2023-01-16
featured-image: baklava-in-every-language.jpg
last-modified: 2023-01-16
layout: default
tags:
- baklava
- mathematica
title: Baklava in Mathematica
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/mathematica/how-to-implement-the-solution.md
- sources/programs/baklava/mathematica/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Mathematica](https://sampleprograms.io/languages/mathematica) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```mathematica
(* Code *)

TableForm[
   Table[
    Table[
     (* asterisk or space depending on Manhattan distance *)
     If[Abs[i] + Abs[j] <= #, "*", " "],
     {i, -#, +#}],
    {j, -#, +#}],
   TableSpacing -> {0, 0}] &[10]
```

{% endraw %}

Baklava in [Mathematica](https://sampleprograms.io/languages/mathematica) was written by:

- Ben Hekster

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).