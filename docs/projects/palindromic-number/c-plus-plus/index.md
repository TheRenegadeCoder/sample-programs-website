---
authors:
- Jeremy Grifski
- rzuckerm
- smjalageri
date: 2021-11-01
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2023-03-30
layout: default
tags:
- c-plus-plus
- palindromic-number
title: Palindromic Number in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/palindromic-number/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

using namespace std;

void palindromic_number(int number)
{
    int temp = number, reversed_number = 0;

    while (temp > 0)
    {
        reversed_number = (reversed_number * 10) + (temp % 10);
        temp = (int)(temp / 10);
    }
    if (number < 0)
    {
        cout << "Usage: please input a non-negative integer";
        exit(1);
    }
    else
    {
        if (reversed_number == number)
        {
            cout << "true";
        }
        else
        {
            cout << "false";
        }
    }
}

int is_int(char **argv)
{
    int j = 0;
    while (isdigit(argv[1][j]))
        ++j;

    if (strlen(argv[1]) != j || j == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main(int argc, char **argv)
{
    if (argc != 2 || is_int(argv))
    {
        cout << "Usage: please input a non-negative integer";
        return (1);
    }
    palindromic_number(atoi(argv[1]));
    return (0);
}

```

{% endraw %}

Palindromic Number in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- rzuckerm
- smjalageri

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).