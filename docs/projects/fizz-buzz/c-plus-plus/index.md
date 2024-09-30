---
authors:
- Ford Smith
- Jeremy Grifski
date: 2019-10-09
featured-image: fizz-buzz-in-every-language.png
last-modified: 2022-10-10
layout: default
tags:
- c-plus-plus
- fizz-buzz
title: Fizz Buzz in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>

int main()
{
    for (int i = 1; i <= 100; i++)
    {
        if (i % 15 == 0)
            std::cout << "FizzBuzz\n";
        else if (i % 5 == 0)
            std::cout << "Buzz\n";
        else if (i % 3 == 0)
            std::cout << "Fizz\n";
        else
            std::cout << i << "\n";
    }
    return 0;
}

```

{% endraw %}

Fizz Buzz in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Ford Smith
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).