---
title: Prime Number in Fortran
layout: default
date: 2020-10-30
featured-image: prime-number-in-every-language.jpg
last-modified: 2020-10-30

---

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Fortran](https://sampleprograms.io/languages/fortran) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fortran
! In program name, - is not allowed
!works till 100938872634753805466563377840038871040
! Commenting out of the reasonable bounds for calculation
program prime_check
  character(len=10) :: argument
  Character(26) :: low = 'abcdefghijklmnopqrstuvwxyz'
  Character(26) :: cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  integer :: check_capital_letters, check_small_letters, i, decimal_check, even_check, remainder, flag_prime
  integer(kind = 16):: number
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
  decimal_check = scan(argument, '.')
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

  ! Decimal Check
  if (decimal_check > 0) then
    write(*,'(g0.8)')"Usage: please input a non-negative integer"
    STOP
  endif
  ! read the cmd line arg into number
  read (argument, '(I10)') number

  ! negative number
  if (number < 0) then
    write(*,'(g0.8)')"Usage: please input a non-negative integer"
    STOP
  endif

  ! ! Maximum Limit
  ! if (number > 100938872634753805466563377840038871040) then
  !   write(*,'(g0.8)')"Input is out of the reasonable bounds for calculation"
  !   STOP
  ! endif

  ! 2 is Prime
  if (number == 2) then
    write(*,'(g0.8)')"Prime"
    STOP
  endif
  ! 0, 1 and even numbers are Even
  even_check = modulo(number, 2)
  if ((number == 0) .or. (number == 1) .or. ( even_check == 0 )) then
    write(*,'(g0.8)')"Composite"
    STOP
  endif
  ! Check Prime
  max = number / 2
  flag_prime = 1
  do i = 3, max
    remainder = modulo(number, i)
    if (remainder == 0) then
      flag_prime = 0
      exit
    end if
  end do

  if(flag_prime == 1) then
    write(*,'(g0.8)') "Prime"
  else 
    write(*,'(g0.8)') "Composite"
  end if
end program
```

{% endraw %}

[Prime Number](https://sampleprograms.io/projects/prime-number) in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- Mallikarjuna S J

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).