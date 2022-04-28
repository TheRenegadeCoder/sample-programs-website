---

---

Welcome to the Baklava in Fortran page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Fortran
program Baklava
    do i = 0, 10, 1
        print '(10a)', repeat (" ", (10 - i)), repeat ("*", (i * 2 + 1))
    end do
    do i = 9, 0, -1
        print '(10a)', repeat (" ", (10 - i)), repeat ("*", (i * 2 + 1))
    end do
end program Baklava

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.