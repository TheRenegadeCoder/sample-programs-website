---
title: Factorial in C++
layout: default
date: 2019-10-09
featured-image: factorial-in-every-language.jpg
last-modified: 2019-10-09

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <cstdlib>
using namespace std;

int main(int argc, char *argv[])
{
    if (argc < 2 || std::string(argv[1]) == "")
    {
        cout << "Usage: please input a non-negative integer" << endl;
        return 1;
    }

    int n = atoi(argv[1]);
    if (n == 0 && std::string(argv[1]) != "0")
    {
        cout << "Usage: please input a non-negative integer" << endl;
        return 1;
    }
    if (n < 0)
    {
        cout << "Usage: please input a non-negative integer" << endl;
        return 1;
    }
    int i, fact = 1;
    for (i = 1; i <= n; i++)
    {
        fact = fact * i;
    }
    cout << fact << endl;
    return 0;
}
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Angooj Kumar Singh
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 16:05:09. The solution was first committed on Oct 09 2019 11:12:44. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).