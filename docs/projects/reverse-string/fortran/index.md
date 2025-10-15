---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-10-15
featured-image: reverse-string-in-every-language.jpg
last-modified: 2025-10-15
layout: default
tags:
- fortran
- reverse-string
title: Reverse String in Fortran
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/fortran/how-to-implement-the-solution.md
- sources/programs/reverse-string/fortran/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Fortran](https://sampleprograms.io/languages/fortran) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fortran
program reverse_string
   implicit none
   character(len=:), allocatable :: arg, rev
   integer :: i, n, error

   if (command_argument_count() < 1) then
      print '("")'
      stop
   end if

   ! Get length of argument
   call get_command_argument(1, length=n, status=error)
   if (error /= 0 .or. n == 0) then
      print '("")'
      stop
   end if

   ! Allocate and read argument
   allocate(character(len=n) :: arg)
   call get_command_argument(1, arg, status=error)
   if (error /= 0) then
      print '("")'
      deallocate(arg)
      stop 0
   end if

   ! Allocate and create reversed string
   allocate(character(len=n) :: rev)
   do i = 1, n
      rev(i:i) = arg(n-i+1:n-i+1)
   end do

   print '(A)', rev
end program reverse_string

```

{% endraw %}

Reverse String in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).