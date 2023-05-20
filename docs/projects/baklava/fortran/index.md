---
title: Baklava in Fortran
layout: default
date: 2018-09-17
featured-image: baklava-in-every-language.jpg
last-modified: 2018-09-17

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Fortran](https://sampleprograms.io/languages/fortran) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

[Baklava](https://sampleprograms.io/projects/baklava) in [Fortran](https://sampleprograms.io/languages/fortran) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 02 2019 15:07:11. The solution was first committed on Sep 17 2018 16:48:59. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).