# Reverse String in Fortran

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Fortran
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.