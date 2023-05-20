---
title: Fizz Buzz in Fortran
layout: default
date: 2020-10-01
featured-image: fizz-buzz-in-every-language.png
last-modified: 2020-10-01

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Fortran](https://sampleprograms.io/languages/fortran) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fortran
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

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- sniklas142

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).