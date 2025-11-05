---
authors:
- leoraggy
date: 2025-11-05
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2025-11-05
layout: default
tags:
- bubble-sort
- fortran
title: Bubble Sort in Fortran
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/fortran/how-to-implement-the-solution.md
- sources/programs/bubble-sort/fortran/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Fortran](https://sampleprograms.io/languages/fortran) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fortran
program bubblesort
    implicit none
    character(len=256) input1
    character(len=256) output
    character(len=10) :: integer_number
    integer, allocatable :: numbers(:)
    integer :: i
    
    if(command_argument_count() /= 1) call usage()
    call get_command_argument(1, input1)
    if(input1 == "") call usage()
    call convert_to_array(input1, numbers)
    
    if(size(numbers) == 1) call usage()
    
    call bubble_sort(numbers)
    
    output = ""
    do i = 1, size(numbers)
        write(integer_number, '(I0)') numbers(i)
        if(len_trim(output) == 0) then
            output = trim(integer_number)
        else
            output = trim(output) // ", " // trim(integer_number)
        end if
    end do
    print '(A)', trim(output)
    
    
contains
    subroutine usage()
        write(*,'(a)') 'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"'
        stop
    end subroutine usage
    
    subroutine convert_to_array(input1, numbers)
        implicit none
        character(len=*), intent(in) :: input1
        integer, allocatable, intent(out) :: numbers(:)
        integer :: i, length, pos, io_status
        
        length = 1
        do i = 1, len_trim(input1)
            if (input1(i:i) == ',') length = length + 1
        end do
    
        allocate(numbers(length))
    
        pos = 1
        do i = 1, length
            read(input1(pos:), *, iostat=io_status) numbers(i)
            if (io_status /= 0) call usage()
            pos = index(input1(pos:), ',') + pos
        end do
    end subroutine convert_to_array
    
    subroutine bubble_sort(numbers)
        implicit none
        integer, intent(inout) :: numbers(:)
        integer :: i, j, temp
        
        do i = 1, size(numbers)
            do j = 1, size(numbers) - i
                if(numbers(j) > numbers(j+1)) then
                    temp = numbers(j)
                    numbers(j) = numbers(j+1)
                    numbers(j+1) = temp
                end if
            end do
        end do
    end subroutine bubble_sort
end program bubblesort
```

{% endraw %}

Bubble Sort in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- leoraggy

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).