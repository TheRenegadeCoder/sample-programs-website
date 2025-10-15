---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-15
featured-image: factorial-in-every-language.jpg
last-modified: 2025-10-15
layout: default
tags:
- factorial
- fortran
title: Factorial in Fortran
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/fortran/how-to-implement-the-solution.md
- sources/programs/factorial/fortran/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Fortran](https://sampleprograms.io/languages/fortran) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fortran
program factorial
   use, intrinsic :: iso_fortran_env, only: int64
   implicit none

   character(len=64) :: arg
   integer :: ios
   integer(kind=int64) :: n, i

   if (command_argument_count() /= 1) call usage()

   call get_command_argument(1, arg)
   arg = adjustl(trim(arg))
   if (len_trim(arg) == 0) call usage()

   read(arg, *, iostat=ios) n
   if (ios /= 0 .or. n < 0_int64) call usage()

   write(*,'(i0)') product((/(i, i = 1_int64, n)/))

contains

   subroutine usage()
      write(*,'(a)') "Usage: please input a non-negative integer"
      stop
   end subroutine usage

end program factorial

```

{% endraw %}

Factorial in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).