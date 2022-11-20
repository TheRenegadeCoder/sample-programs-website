---

title: Reverse String in Fortran
layout: default
date: 2022-04-28
last-modified: 2022-11-20

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
if (argument == "") then
  write(*,'(g0.8)')"Usage: please provide a string"
else
  allocate (buff, mold=argument)
  n = len(argument)
  do i = 0, n - 1
     buff(n-i : n-i) = argument(i+1 : i+1)
  end do
  reversed = adjustl(trim(buff))
  write(*,'(g0.8)')reversed
  n = len(reversed)
end if 
end program reversestring
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- Mallikarjuna S J

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).