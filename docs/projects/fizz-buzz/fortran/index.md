---

title: Fizz Buzz in Fortran
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Fizz Buzz in Fortran page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Fortran
program fizz_buzz
        integer :: i

        do i = 1,100
                if ((modulo(i,3) == 0) .and. (modulo(i,5) == 0)) then 
                        write (*,'(a)') "FizzBuzz"
                else if (modulo(i,3) == 0) then
                        write (*,'(a)') "Fizz"
                else if (modulo(i,5) == 0) then
                        write (*,'(a)') "Buzz"
                else
                        write (*,'(I0)') i
                end if
        end do
        
end program fizz_buzz

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.