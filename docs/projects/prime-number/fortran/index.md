---
authors:
- Mallikarjuna S J
- "\u0218tefan-Iulian Alecu"
date: 2020-10-30
featured-image: prime-number-in-every-language.jpg
last-modified: 2025-10-15
layout: default
tags:
- fortran
- prime-number
title: Prime Number in Fortran
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/fortran/how-to-implement-the-solution.md
- sources/programs/prime-number/fortran/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Fortran](https://sampleprograms.io/languages/fortran) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fortran
program prime_check
   implicit none
   integer :: argc, ios, i
   character(len=256) :: arg
   integer :: number

   argc = command_argument_count()
   if (argc /= 1) call usage()

   call get_command_argument(1, arg)
   arg = adjustl(trim(arg))
   if (len_trim(arg) == 0) call usage()

   do i = 1, len_trim(arg)
      if (arg(i:i) < '0' .or. arg(i:i) > '9') call usage()
   end do

   read(arg, *, iostat=ios) number
   if (ios /= 0 .or. number < 0) call usage()

   if (is_prime(number)) then
      print *, "Prime"
   else
      print *, "Composite"
   end if

contains
   subroutine usage()
      print *, "Usage: please input a non-negative integer"
      stop
   end subroutine usage

   pure function is_prime(n) result(prime)
      integer, intent(in) :: n
      logical :: prime
      integer :: k, w, offsets(8)

      ! Wheel offsets for 30k + {1,7,11,13,17,19,23,29}
      offsets = [1, 7, 11, 13, 17, 19, 23, 29]

      if (n < 2) then
         prime = .false.
         return
      elseif (n <= 3) then
         prime = .true.
         return
      elseif (mod(n,2) == 0 .or. mod(n,3) == 0 .or. mod(n,5) == 0) then
         prime = .false.
         return
      end if

      prime = .true.
      w = 0
      k = 7   ! start from the first wheel candidate after 5

      do while (k*k <= n)
         do w = 1, 8
            if (mod(n, k + offsets(w) - 1) == 0) then
               prime = .false.
               return
            end if
         end do
         k = k + 30
      end do

   end function is_prime

end program prime_check

```

{% endraw %}

Prime Number in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- Mallikarjuna S J
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).