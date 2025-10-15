---
authors:
- Mallikarjuna S J
- "\u0218tefan-Iulian Alecu"
date: 2020-10-29
featured-image: capitalize-in-every-language.jpg
last-modified: 2025-10-15
layout: default
tags:
- capitalize
- fortran
title: Capitalize in Fortran
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/fortran/how-to-implement-the-solution.md
- sources/programs/capitalize/fortran/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Fortran](https://sampleprograms.io/languages/fortran) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fortran
program capitalize
   implicit none
   character(len=100) :: cmd
   integer :: argc

   argc = command_argument_count()
   if (argc /= 1) call usage()

   call get_command_argument(1, cmd)
   cmd = adjustl(trim(cmd))
   if (len_trim(cmd) == 0) call usage()

   cmd(1:1) = upper(cmd(1:1))

   write(*,*) cmd

contains

   subroutine usage()
      write(*,*) "Usage: please provide a string"
      stop
   end subroutine

   pure elemental function upper(str) result(string)
      character(*), intent(in) :: str
      character(len(str)) :: string
      integer :: i, iend
      integer, parameter :: toupper = iachar('A') - iachar('a')

      iend = len_trim(str)
      string = str(:iend)

      do concurrent (i = 1:iend)
         select case (str(i:i))
          case ('a':'z')
            string(i:i) = achar(iachar(str(i:i)) + toupper)
         end select
      end do
   end function upper

end program capitalize

```

{% endraw %}

Capitalize in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- Mallikarjuna S J
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).