---
authors:
- LauraV-702
date: 2024-11-07
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2024-11-07
layout: default
tags:
- c-plus-plus
- remove-all-whitespace
title: Remove All Whitespace in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <string>
#include <cctype>  // for std::isspace


int main(int argc, char* argv[]) {

    // Check if given string passed
    if (argc < 2) {
        std::cout << "Usage: please provide a string" << std::endl;
        return 1; // Return error code if no string is given
    }

    // Get the string passed 
    std::string input = argv[1]; 
    std::string result;

    // Check if input string is empty
    if (input.empty()) {
        std::cout << "Usage: please provide a string" << std::endl;
        return 1; // Exit error code if the string is empty
    } 

    for(char c : input) {
        // If the character is not a whitespace character, add it to result     
        if (!std::isspace(static_cast<unsigned char>(c))) {
            result += c;
        }
    }
    //print out the result (string should have no spaces)
    std::cout << result << std::endl;
   
    return 0;
} 

```

{% endraw %}

Remove All Whitespace in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- LauraV-702

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).