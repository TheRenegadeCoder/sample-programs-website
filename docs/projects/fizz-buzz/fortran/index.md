---
authors:
- sniklas142
- "\u0218tefan-Iulian Alecu"
date: 2020-10-01
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-10-15
layout: default
tags:
- fizz-buzz
- fortran
title: Fizz Buzz in Fortran
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/fortran/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/fortran/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Fortran](https://sampleprograms.io/languages/fortran) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fortran
program fizzbuzz
   implicit none
   integer, parameter :: n = 100
   integer :: i

   do i = 1, n
      write(*,'(A)') fizzbuzz_string(i)
   end do

contains

   pure function fizzbuzz_string(x) result(str)
      integer, intent(in) :: x
      character(len=8) :: str

      str = ''

      if (mod(x,3) == 0) str = 'Fizz'
      if (mod(x,5) == 0) str = trim(str)//'Buzz'
      if (len_trim(str) == 0) write(str,'(I0)') x
   end function fizzbuzz_string

end program fizzbuzz

```

{% endraw %}

Fizz Buzz in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- sniklas142
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).