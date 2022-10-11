---

title: Palindromic Number in C++
layout: default
date: 2022-04-28
last-modified: 2022-10-11

---

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <string.h>
#include <stdlib.h>

using namespace std;

void palindromic_number(int number)
{
    int temp = number, no_of_digits = 0, reversed_number = 0;

    while (temp > 0)
    {
        reversed_number = (reversed_number * 10) + (temp % 10);
        temp = (int)(temp / 10);
        no_of_digits++;
    }
    if (no_of_digits < 2)
    {
        cout << "Usage: please input a number with at least two digits";
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

int is_int(char *number_string)
{
    if (number_string[0] > '9' || number_string[0] < '0')
        return (0);
    for (int counter = 0; number_string[counter]; counter++)
    {
        if (number_string[0] > '9' || number_string[0] < '0')
            return (0);
    }
    return (1);
}

int main(int argc, char **argv)
{
    if (argc != 2 || is_int(argv[1]) != 1)
    {
        cout << "Usage: please input a number with at least two digits";
        return (1);
    }
    palindromic_number(atoi(argv[1]));
    return (0);
}
```

{% endraw %}

[Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- smjalageri

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 16:05:09. The solution was first committed on Nov 01 2021 10:06:42. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).