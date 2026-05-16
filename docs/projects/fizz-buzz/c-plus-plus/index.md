---
authors:
- Ford Smith
- Ștefan-Iulian Alecu
date: 2019-10-09
featured-image: fizz-buzz-in-every-language.png
last-modified: 2026-05-05
layout: default
tags:
- c-plus-plus
- fizz-buzz
title: Fizz Buzz in C++
title1: Fizz Buzz
title2: in C++
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

int main() {
    for (int i = 1; i <= 100; ++i) {
        const bool fizz = (i % 3 == 0);
        const bool buzz = (i % 5 == 0);

        if (fizz && buzz) {
            std::cout << "FizzBuzz\n";
        } else if (fizz) {
            std::cout << "Fizz\n";
        } else if (buzz) {
            std::cout << "Buzz\n";
        } else {
            std::cout << i << '\n';
        }
    }
    
    return 0;
}

```

{% endraw %}

Fizz Buzz in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Ford Smith
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).