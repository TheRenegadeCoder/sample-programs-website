---
authors:
- Meet Thakur
date: 2025-10-11
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2025-10-11
layout: default
tags:
- c-plus-plus
- longest-palindromic-substring
title: Longest Palindromic Substring in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <string>
#include <cstring>

#define MAX_LENGTH 1000

int expandAroundCenter(const std::string& s, int left, int right) {
    while (left >= 0 && right < s.length() && s[left] == s[right]) {
        left--;
        right++;
    }
    return right - left - 1;
}

bool longestPalindromicSubstring(const std::string& s, std::string& result) {
    if (s.empty()) {
        result = "";
        return false;
    }

    int start = 0, maxLength = 0;
    int len = s.length();

    for (int i = 0; i < len; i++) {
        int len1 = expandAroundCenter(s, i, i);
        int len2 = expandAroundCenter(s, i, i + 1);
        int len = (len1 > len2) ? len1 : len2;

        if (len > maxLength) {
            start = i - (len - 1) / 2;
            maxLength = len;
        }
    }

    if (maxLength > 1) {
        result = s.substr(start, maxLength);
        return true;
    }

    result = "";
    return false;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cout << "Usage: please provide a string that contains at least one palindrome" << std::endl;
        return 1;
    }

    std::string input = argv[1];
    std::string result;

    if (longestPalindromicSubstring(input, result) && !result.empty()) {
        std::cout << result << std::endl;
    } else {
        std::cout << "Usage: please provide a string that contains at least one palindrome" << std::endl;
    }

    return 0;
}

```

{% endraw %}

Longest Palindromic Substring in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Meet Thakur

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).