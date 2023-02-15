---

title: Baklava in C++
layout: default
date: 2022-04-28
last-modified: 2023-02-15

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int i, j, k, n;
    n = 21;
    for (i = 1; i <= (n + 1) / 2;)
    {
        for (k = 1; (n + 1) / 2 - i >= k; k++)
            cout << " ";
        for (j = 1; j < 2 * i; j++)
            cout << "*";
        cout << "\n";
        i++;
    }
    if (2 * i - 1 >= n)
    {
        for (i = (n + 1) / 2 - 1; i >= 1; i--)
        {
            for (k = 1; (n + 1) / 2 - i >= k; k++)
                cout << " ";
            for (j = 1; j < 2 * i; j++)
                cout << "*";
            cout << "\n";
        }
    }
    return (0);
}
```

{% endraw %}

[Baklava](https://sampleprograms.io/projects/baklava) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Behnam Ahmad khan beigi
- Jeremy Grifski
- yottanami

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 16:05:09. The solution was first committed on Oct 09 2019 12:45:32. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).