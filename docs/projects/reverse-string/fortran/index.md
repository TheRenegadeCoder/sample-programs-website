---
authors:
- Mallikarjuna S J
- rzuckerm
date: 2020-10-27
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-03-19
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
program reversestring
character(len=100) :: argument
character(len=:), allocatable :: buff, reversed
integer :: i, n
call GET_COMMAND_ARGUMENT(1,argument)
allocate (buff, mold=argument)
n = len(argument)
do i = 0, n - 1
    buff(n-i : n-i) = argument(i+1 : i+1)
end do
reversed = adjustl(trim(buff))
write(*,'(g0.8)')reversed
end program reversestring

```

{% endraw %}

Reverse String in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- Mallikarjuna S J
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).