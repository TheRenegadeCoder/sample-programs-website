---
authors:
- Mallikarjuna S J
- "\u0218tefan-Iulian Alecu"
date: 2020-10-29
featured-image: even-odd-in-every-language.jpg
last-modified: 2025-10-15
layout: default
tags:
- even-odd
- fortran
title: Even Odd in Fortran
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/fortran/how-to-implement-the-solution.md
- sources/programs/even-odd/fortran/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Fortran](https://sampleprograms.io/languages/fortran) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fortran
program evenodd
   implicit none
   character(len=12) :: arg
   character(len=52) :: letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
   integer :: number, ios, argc

   argc = command_argument_count()
   if (argc /= 1) call usage()

   call get_command_argument(1, arg)
   if (len_trim(arg) == 0) call usage()
   if (scan(arg, letters) > 0) call usage()

   read(arg, *, iostat=ios) number
   if (ios /= 0) call usage()

   if (mod(number,2) == 0) then
      write(*,*) "Even"
   else
      write(*,*) "Odd"
   end if

contains

   subroutine usage()
      write(*,*) "Usage: please input a number"
      stop
   end subroutine

end program evenodd

```

{% endraw %}

Even Odd in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- Mallikarjuna S J
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).