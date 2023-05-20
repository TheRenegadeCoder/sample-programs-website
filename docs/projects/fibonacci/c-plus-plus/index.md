---
title: Fibonacci in C++
layout: default
date: 2018-10-06
featured-image: fibonacci-in-every-language.jpg
last-modified: 2018-10-06

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

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
        cout << "Usage: please input the count of fibonacci numbers to output" << endl;
        return 1;
    }

    int n = atoi(argv[1]);
    if (n == 0 && std::string(argv[1]) != "0")
    {
        cout << "Usage: please input the count of fibonacci numbers to output" << endl;
        return 1;
    }
    int first = 0;
    int second = 1;
    int result = 0;

    for (int i = 1; i <= n; ++i)
    {
        result = first + second;
        first = second;
        second = result;
        cout << i << ": " << first << endl;
    }
    return 0;
}
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- Marius
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 16:05:09. The solution was first committed on Oct 06 2018 16:51:18. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).