---
authors:
- Jake-G123
date: 2025-10-29
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2025-10-29
layout: default
tags:
- c-plus-plus
- maximum-array-rotation
title: Maximum Array Rotation in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;
int main(int argc, char *argv[]) {
    // Check if input exists and isn't empty
    if (argc < 2 || string(argv[1]).empty()) {
        cout << "Usage: please provide a list of integers (e.g. \"8, 3, 1, 2\")";
        return 1;
    }
    // Parse input string
    vector<int> arr;
    string input = argv[1];
    stringstream ss(input);
    string token;

    while (getline(ss, token, ',')) {
        arr.push_back(stoi(token));
    }

    int n = arr.size();
    int arr_sum = 0;
    int current_sum = 0;
    // Get sum of array and first rotation sum
    for (int i = 0; i < n; i++) {
        arr_sum += arr[i];
        current_sum+= i * arr[i];
    }
    
    int max_sum = current_sum;
    // check all other possible rotations
    for (int j = 1; j < n; j++) {
        int rotating_value = arr[n-j];
        // next sum = current sum + gains of shifting values one index higher - loss of moving highest index to 0
        current_sum = current_sum + arr_sum - n * rotating_value;

        if (current_sum > max_sum) {
            max_sum = current_sum;
        }
    }
    cout << max_sum << endl;
    return 0;
}
```

{% endraw %}

Maximum Array Rotation in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jake-G123

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).