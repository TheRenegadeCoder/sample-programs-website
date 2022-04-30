---

title: Even Odd in C++
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Even Odd in C++ page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).