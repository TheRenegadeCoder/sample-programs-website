---
authors:
- Butenkite
- "\u0218tefan-Iulian Alecu"
date: 2025-02-16
featured-image: fibonacci-in-every-language.jpg
last-modified: 2025-10-15
layout: default
tags:
- fibonacci
- fortran
title: Fibonacci in Fortran
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/fortran/how-to-implement-the-solution.md
- sources/programs/fibonacci/fortran/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Fortran](https://sampleprograms.io/languages/fortran) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fortran
program fibonacci
   implicit none
   integer(kind=8) :: prev, curr, next, n, i
   character(len=32) :: arg
   integer :: ios

   if (command_argument_count() /= 1) then
      call usage()
      return
   endif

   call get_command_argument(1, arg)
   arg = adjustl(trim(arg))
   if (len_trim(arg) == 0) then
      call usage()
      return
   endif

   read(arg, *, iostat=ios) n
   if (ios /= 0 .or. n < 0) then
      call usage()
      return
   endif

   if (n == 0) return

   prev = 0
   curr = 1

   do i = 1, n
      write(*,'(I0,": ",I0)') i, curr
      next = prev + curr
      prev = curr
      curr = next
   end do

contains

   subroutine usage()
      write(*,'(A)') "Usage: please input the count of fibonacci numbers to output"
   end subroutine usage

end program fibonacci

```

{% endraw %}

Fibonacci in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- Butenkite
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).