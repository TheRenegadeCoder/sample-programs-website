---

title: Even Odd in Fortran
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Even Odd in Fortran page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Fortran
! In program name, - is not allowed
program evenodd
character(len=10) :: argument
Character(26) :: low = 'abcdefghijklmnopqrstuvwxyz'
Character(26) :: cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
integer :: number, check_capital_letters, check_small_letters, remainder 
! Anything not equal to single argument, Print Error
IF(COMMAND_ARGUMENT_COUNT().NE.1)THEN
  write(*,'(g0.8)')"Usage: please input a number"
  STOP
ENDIF

CALL GET_COMMAND_ARGUMENT(1,argument)
if (argument == "") then
  write(*,'(g0.8)')"Usage: please input a number"
  STOP
endif
! Scan for letters
check_capital_letters = scan(argument, cap)
check_small_letters = scan(argument, low)
! If capital letters exist, print error
if (check_capital_letters > 0) then
  write(*,'(g0.8)')"Usage: please input a number"
  STOP
endif
! If small letters exist, print error
if (check_small_letters > 0) then
  write(*,'(g0.8)')"Usage: please input a number"
  STOP
endif
! read the cmd line arg into number
read (argument, '(I10)') number
! get the remainder
remainder = modulo(number, 2)
if (remainder == 0) then
  write(*,'(g0.8)') "Even"
else
  write(*,'(g0.8)') "Odd"
end if
end program

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.