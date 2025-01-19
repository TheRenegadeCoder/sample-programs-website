---
authors:
- Maximillian Naza
date: 2025-01-19
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2025-01-19
layout: default
tags:
- c
- longest-palindromic-substring
title: Longest Palindromic Substring in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/c/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX_LENGTH 1000

int expandAroundCenter(const char* s, int left, int right) {
    while (left >= 0 && right < strlen(s) && s[left] == s[right]) {
        left--;
        right++;
    }
    return right - left - 1;
}

bool longestPalindromicSubstring(const char* s, char* result) {
    if (s == NULL || strlen(s) == 0) {
        strcpy(result, "");
        return false;
    }

    int start = 0, maxLength = 0;
    int len = strlen(s);

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
        strncpy(result, s + start, maxLength);
        result[maxLength] = '\0';
        return true;
    }

    strcpy(result, "");
    return false;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("Usage: please provide a string that contains at least one palindrome\n");
        return 1;
    }

    const char* input = argv[1];
    char result[MAX_LENGTH];

    if (longestPalindromicSubstring(input, result) && strlen(result) > 0) {
        printf("%s\n", result);
    } else {
        printf("Usage: please provide a string that contains at least one palindrome\n");
    }

    return 0;
}

```

{% endraw %}

Longest Palindromic Substring in [C](https://sampleprograms.io/languages/c) was written by:

- Maximillian Naza

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).