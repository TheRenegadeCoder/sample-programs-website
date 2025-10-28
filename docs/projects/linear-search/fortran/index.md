---
authors:
- leoraggy
date: 2025-10-28
featured-image: linear-search-in-every-language.jpg
last-modified: 2025-10-28
layout: default
tags:
- fortran
- linear-search
title: Linear Search in Fortran
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/fortran/how-to-implement-the-solution.md
- sources/programs/linear-search/fortran/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Fortran](https://sampleprograms.io/languages/fortran) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fortran
Program linearsearch
    implicit none

    character(len=256) :: input1
    character(len=10) :: input2
    integer :: key
    integer, dimension(5) :: array
    logical :: searched
    integer :: io_status

    if(command_argument_count() < 2) call usage()

    call get_command_argument(1, input1)
    call get_command_argument(2,input2)

    if(input1 == "") call usage()

    read(unit=input1, fmt=*, iostat=io_status) array
    read(unit=input2, fmt=*, iostat=io_status) key
    
    searched = exists(array,key)

    if (searched) then
        print '(a)', 'true'
    else
        print '(a)', 'false'
    end if

    contains

    pure function exists(array, key) result(answer)
        implicit none
        INTEGER :: i
        integer, intent(in) :: key
        integer, intent(in) :: array(:)
        logical :: answer

        answer = .false.

        do i = 1, size(array), 1
            if(array(i) == key) then
                answer = .true.
                return
            end if
        end do

    end function exists

subroutine usage()
    write(*,'(a)') "Usage: please provide a list of integers (""1, 4, 5, 11, 12"") and the integer to find (""11"")"
    stop
end subroutine usage

End Program linearsearch
```

{% endraw %}

Linear Search in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- leoraggy

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).