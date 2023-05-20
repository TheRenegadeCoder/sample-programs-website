---
title: Bubble Sort in C++
layout: default
date: 2019-10-02
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2019-10-02

---

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <cstring>
#include <iostream>
#include <vector>

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void bubbleSort(std::vector<int> &v, int n)
{
    int i, j;
    bool swapped;

    for (i = 0; i < n - 1; i++)
    {
        swapped = false;

        for (j = 0; j < n - i - 1; j++)
        {
            if (v[j] > v[j + 1])
            {
                swap(&v[j], &v[j + 1]);
                swapped = true;
            }
        }

        if (swapped == false)
        {
            break;
        }
    }
}

void print(std::vector<int> v, int size)
{
    for (int i = 0; i < size; i++)
        if (i == size - 1)
        {
            std::cout << v[i] << std::endl;
        }
        else
        {
            std::cout << v[i] << ", ";
        }
}

int main(int argc, char *argv[])
{

    char *characters = argv[1];
    bool commaSeparated = false;
    int index = 1;
    std::vector<int> numbers;

    if (argc == 2)
    {

        while (index < strlen(characters))
        {
            if (characters[index] == ',' && characters[index + 1] == ' ')
            {
                commaSeparated = true;
            }
            else
            {
                commaSeparated = false;
                break;
            }
            index += 3;
        }

        if (commaSeparated == true)
        {
            for (int i = 0; i < strlen(characters); i++)
            {

                if (characters[i] != ',' && characters[i] != ' ')
                {
                    numbers.push_back(atoi(&characters[i]));
                }
            }
        }
    }

    int size = numbers.size();
    if (size < 2)
    {
        std::cout << "Usage: please provide a list of at least two integers to "
                     "sort in the format \"1, 2, 3, 4, 5\""
                  << std::endl;
    }
    else
    {
        bubbleSort(numbers, size);
        print(numbers, size);
    }
    return 0;
}
```

{% endraw %}

[Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jayden Thrasher
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 16:05:09. The solution was first committed on Oct 02 2019 20:31:08. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).