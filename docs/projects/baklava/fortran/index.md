---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-15
featured-image: baklava-in-every-language.jpg
last-modified: 2025-10-15
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
program baklava
   implicit none
   integer :: i, size, spaces, stars

   parameter (size = 10)

   do i = 0, size
      spaces = size - i
      stars  = i * 2 + 1
      print '(A)', repeat(' ', spaces)//repeat('*', stars)
   end do

   do i = size-1, 0, -1
      spaces = size - i
      stars  = i * 2 + 1
      print '(A)', repeat(' ', spaces)//repeat('*', stars)
   end do
end program baklava

```

{% endraw %}

Baklava in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).