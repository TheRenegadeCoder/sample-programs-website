---

title: Fizz Buzz in C++
layout: default
date: 2022-04-28
last-modified: 2022-10-08

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>

int main()
{
    for (int i = 1; i <= 100; i++) {
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

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).