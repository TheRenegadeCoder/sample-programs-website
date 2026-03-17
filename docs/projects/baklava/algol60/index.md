---
authors:
- rzuckerm
date: 2026-03-17
featured-image: baklava-in-every-language.jpg
last-modified: 2026-03-17
layout: default
tags:
- algol60
- baklava
title: Baklava in ALGOL 60
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/algol60/how-to-implement-the-solution.md
- sources/programs/baklava/algol60/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [ALGOL 60](https://sampleprograms.io/languages/algol60) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol_60
begin
    procedure outRepeatString(n, s);
    value n;
    integer n;
    string s;
    begin
        integer i;
        for i := 1 step 1 until n do outstring(1, s)
    end outRepeatString;

    integer i, numspaces, numstars;
    for i := -10 step 1 until 10 do
    begin
        numspaces := abs(i);
        numstars := 21 - 2 * numspaces;
        outRepeatString(numspaces, " ");
        outRepeatString(numstars, "*");
        outstring(1, "\n")
    end
end

```

{% endraw %}

Baklava in [ALGOL 60](https://sampleprograms.io/languages/algol60) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).