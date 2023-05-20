---
title: Even Odd in C++
layout: default
date: 2019-10-09
featured-image: even-odd-in-every-language.jpg
last-modified: 2019-10-09

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <stdlib.h>
#include <string.h>

using namespace std;

int main(int argc, char **argv)
{
    if (argc == 1 || argv[1][0] == '\0' || (atoi(argv[1]) == 0 && strcmp(argv[1], "0") != 0))
    {
        cout << "Usage: please input a number\n";
    }
    else
    {
        int input = atoi(argv[1]);
        if (input % 2 == 0)
        {
            cout << "Even\n";
        }
        else
        {
            cout << "Odd\n";
        }
    }

    return 0;
}
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- killbotxd

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 16:05:09. The solution was first committed on Oct 09 2019 12:50:24. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).