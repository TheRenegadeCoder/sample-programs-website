---
title: Reverse String in Fortran
layout: default
date: 2020-10-27
featured-image: reverse-string-in-every-language.jpg
last-modified: 2020-10-27

---

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

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- Mallikarjuna S J
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 19 2023 22:24:49. The solution was first committed on Oct 27 2020 09:31:11. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).