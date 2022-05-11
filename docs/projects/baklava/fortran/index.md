---

title: Baklava in Fortran
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Baklava in Fortran page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fortran
program Baklava
    do i = 0, 10, 1
        print '(10a)', repeat (" ", (10 - i)), repeat ("*", (i * 2 + 1))
    end do
    do i = 9, 0, -1
        print '(10a)', repeat (" ", (10 - i)), repeat ("*", (i * 2 + 1))
    end do
end program Baklava
```

{% endraw %}

Baklava in Fortran was written by:

- Jeremy Grifski

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 02 2019 15:07:11. The solution was first committed on Sep 17 2018 16:48:59. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).