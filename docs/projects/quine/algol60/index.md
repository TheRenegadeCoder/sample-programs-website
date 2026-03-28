---
authors:
- rzuckerm
date: 2026-03-28
featured-image: quine-in-every-language.jpg
last-modified: 2026-03-28
layout: default
tags:
- algol60
- quine
title: Quine in ALGOL 60
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quine/algol60/how-to-implement-the-solution.md
- sources/programs/quine/algol60/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [ALGOL 60](https://sampleprograms.io/languages/algol60) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol_60
begin procedure q(a,b,c);string a,b,c;begin outstring(1,c);outchar(1,a,2);outchar(1,a,1);outchar(1,a,1);outstring(1,a);outchar(1,a,2);outchar(1,a,3);outchar(1,a,2);outstring(1,b);outchar(1,a,2);outchar(1,a,3);outchar(1,a,2);outstring(1,c);outchar(1,a,2);outstring(1,b) end q;q("\\\",",") end","begin procedure q(a,b,c);string a,b,c;begin outstring(1,c);outchar(1,a,2);outchar(1,a,1);outchar(1,a,1);outstring(1,a);outchar(1,a,2);outchar(1,a,3);outchar(1,a,2);outstring(1,b);outchar(1,a,2);outchar(1,a,3);outchar(1,a,2);outstring(1,c);outchar(1,a,2);outstring(1,b) end q;q(") end
```

{% endraw %}

Quine in [ALGOL 60](https://sampleprograms.io/languages/algol60) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).