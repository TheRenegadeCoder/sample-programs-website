---
authors:
- Jeremy Grifski
date: 2018-09-17
featured-image: baklava-in-every-language.jpg
last-modified: 2019-04-02
layout: default
tags:
- baklava
- fortran
title: Baklava in Fortran
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/fortran/how-to-implement-the-solution.md
- sources/programs/baklava/fortran/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Fortran](https://sampleprograms.io/languages/fortran) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fortran
program Baklava
    do i = 0, 10, 1
        print '(10a)', repeat (" ", (10 - i)), repeat ("*", (i * 2 + 1))
    end do
    do i = 9, 0, -1
        print '(10a)', repeat (" ", (10 - i)), repeat ("*", (i * 2 + 1))
    end do
end program Baklava

```

{% endraw %}

Baklava in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).