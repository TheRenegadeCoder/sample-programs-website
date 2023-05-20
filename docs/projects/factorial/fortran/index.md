---
title: Factorial in Fortran
layout: default
date: 2020-10-29
featured-image: factorial-in-every-language.jpg
last-modified: 2020-10-29

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Fortran](https://sampleprograms.io/languages/fortran) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fortran
! In program name, - is not allowed
!works till 77
! 78 and above is out of the reasonable bounds for calculation
program factorial_generate
  character(len=10) :: argument
  Character(26) :: low = 'abcdefghijklmnopqrstuvwxyz'
  Character(26) :: cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  integer :: number, check_capital_letters, check_small_letters, i
  integer(kind = 16):: factorial
  ! Anything not equal to single argument, Print Error
  IF(COMMAND_ARGUMENT_COUNT().NE.1)THEN
    write(*,'(g0.8)')"Usage: please input a non-negative integer"
    STOP
  ENDIF
  
  CALL GET_COMMAND_ARGUMENT(1,argument)
  if (argument == "") then
    write(*,'(g0.8)')"Usage: please input a non-negative integer"
    STOP
  endif
  ! Scan for letters
  check_capital_letters = scan(argument, cap)
  check_small_letters = scan(argument, low)
  ! If capital letters exist, print error
  if (check_capital_letters > 0) then
    write(*,'(g0.8)')"Usage: please input a non-negative integer"
    STOP
  endif
  ! If small letters exist, print error
  if (check_small_letters > 0) then
    write(*,'(g0.8)')"Usage: please input a non-negative integer"
    STOP
  endif
  ! read the cmd line arg into number
  read (argument, '(I10)') number

  if (number < 0) then
    write(*,'(g0.8)')"Usage: please input a non-negative integer"
    STOP
  endif
  if (number > 77) then
    write(*,'(g0.8)')"Input is out of the reasonable bounds for calculation"
    STOP
  endif

  factorial = 1
  do i = 1, number
    factorial = factorial * i
  end do
  write(*,'(g0.8)') factorial
end program
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- Mallikarjuna S J

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).