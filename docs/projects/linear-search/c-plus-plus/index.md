---

title: Linear Search in C++
layout: default
date: 2022-04-28
last-modified: 2023-01-25

---

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

int main(int argc, char *argv[])
{
    string error = "Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")";

    if (argc != 3)
    {
        cout << error << endl;
        return 1;
    }
    int numberLength = strlen(argv[1]);
    int keyLength = strlen(argv[1]);

    if (numberLength == 0 || keyLength == 0)
    {
        cout << error << endl;
        return 1;
    }
    vector<int> arr;
    string temp = "";
    for (int i = 0; i < numberLength; i++)
    {
        if (argv[1][i] == ',')
        {
            arr.push_back(stoi(temp));
            temp = "";
        }
        else
        {
            temp = temp + argv[1][i];
        }
    }
    arr.push_back(stoi(temp));
    int key = stoi(argv[2]);
    bool found = false;
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] == key)
        {
            found = true;
        }
    }
    if (found)
    {
        cout << "true";
    }
    else
    {
        cout << "false";
    }
}
```

{% endraw %}

[Linear Search](https://sampleprograms.io/projects/linear-search) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 16:05:09. The solution was first committed on Oct 03 2022 18:47:58. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).