---

title: Even Odd in C++
layout: default
date: 2022-04-28
last-modified: 2022-05-18


---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include<iostream>
#include<stdlib.h>
#include<string.h>

using namespace std;

int main(int argc, char **argv)
{
    if (argc == 1 || argv[1][0] == '\0' || (atoi(argv[1]) == 0 && strcmp(argv[1], "0") != 0)) {
        cout<<"Usage: please input a number\n";
    } else {
        int input = atoi(argv[1]);
        if (input % 2 == 0) {
            cout<<"Even\n";
        }
        else {
            cout<<"Odd\n";
        }
    }

    return 0;
}
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- killbotxd

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).