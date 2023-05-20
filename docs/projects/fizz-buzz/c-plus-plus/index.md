---
title: Fizz Buzz in C++
layout: default
date: 2019-10-09
featured-image: fizz-buzz-in-every-language.png
last-modified: 2019-10-09

---

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

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Ford Smith
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 16:05:09. The solution was first committed on Oct 09 2019 00:53:15. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).