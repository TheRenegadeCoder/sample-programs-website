---
authors:
- Himanshu Raheja
date: 2023-10-19
featured-image: rot13-in-every-language.jpg
last-modified: 2023-10-19
layout: default
tags:
- c-plus-plus
- rot13
title: Rot13 in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/rot13/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <string>

using namespace std;

void rot13(string& str) {
    for (char& c : str) {
        if (('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z')) {
            if (('a' <= c && c <= 'm') || ('A' <= c && c <= 'M')) {
                c += 13;
            } else {
                c -= 13;
            }
        }
    }
}

int main(int argc, char* argv[]) {
    if (argc == 2 && string(argv[1]).size() != 0) {
        string inputString(argv[1]);
        rot13(inputString);
        cout << inputString << endl;
    } else {
        cout << "Usage: please provide a string to encrypt" << endl;
    }

    return 0;
}

```

{% endraw %}

Rot13 in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Himanshu Raheja

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).