---
title: Prime Number in C++
layout: default
date: 2019-10-14
featured-image: prime-number-in-every-language.jpg
last-modified: 2019-10-14

---

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <stdlib.h>
#include <string.h>

using namespace std;

int main(int argc, char **argv)
{
    if (argc == 1)
    {
        cout << "Usage: please input a non-negative integer\n";
        return 1;
    }
    string tmp = argv[1];
    if (argc == 1 || argv[1][0] == '\0' || (atoi(argv[1]) == 0 && strcmp(argv[1], "0") != 0) || atoi(argv[1]) < 0 || tmp.find(".") != string::npos)
    {
        cout << "Usage: please input a non-negative integer\n";
    }
    else
    {
        int input = atoi(argv[1]);
        if (input == 0 || input == 1)
        {
            cout << "composite\n";
            return 0;
        }
        for (int i = 2; i < input; ++i)
        {
            if (input % i == 0)
            {
                cout << "composite\n";
                return 0;
            }
        }
        cout << "Prime\n";
    }

    return 0;
}
```

{% endraw %}

[Prime Number](https://sampleprograms.io/projects/prime-number) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Daffa Daraz
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 16:05:09. The solution was first committed on Oct 14 2019 00:44:05. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).