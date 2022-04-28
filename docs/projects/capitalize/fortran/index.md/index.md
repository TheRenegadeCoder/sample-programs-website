---

---

Welcome to the Capitalize in Fortran page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Fortran
! upcase and to_upper didn't work, 
! had to resort to check ASCII value of first letter & then
! subtract 32 from it, ... 
program capitalize
character(len=100) :: cmd
character(len=1) :: firstletter
character(len=:), allocatable :: printoutput

! Anything not equal to single argument, Print Error
IF(COMMAND_ARGUMENT_COUNT().NE.1)THEN
  write(*,'(g0.8)')"Usage: please provide a string"
  STOP
ENDIF

CALL GET_COMMAND_ARGUMENT(1,cmd)
if (cmd == "") then
  write(*,'(g0.8)')"Usage: please provide a string"
  STOP
endif
! Get first letter
  firstletter = cmd(1:1)
  ! Check if first letter is between ASCII Value of a and z
  if (iachar(firstletter)>= iachar("a") .and. iachar(firstletter)<=iachar("z") ) then
  ! Subtract 32 from ASCII Value, to convert it to respective capital letter
    firstletter = achar(iachar(firstletter)-32)
! Overwrite the first letter 
    cmd(1:1) = firstletter
  end if
    printoutput = adjustl(trim(cmd))
    write(*,'(g0.8)')printoutput
end program capitalize

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.