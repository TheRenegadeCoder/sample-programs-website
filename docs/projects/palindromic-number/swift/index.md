---
authors:
- Kaalid
date: 2024-11-12
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2024-11-12
layout: default
tags:
- palindromic-number
- swift
title: Palindromic Number in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/swift/how-to-implement-the-solution.md
- sources/programs/palindromic-number/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

func isPalindrome(_ input: String) -> Bool {
    return input == String(input.reversed())
}

func main() {
    let arguments = CommandLine.arguments

    guard arguments.count == 2 else {
        print("Usage: please input a non-negative integer")
        return
    }

    let input = arguments[1]
    
    if let number = Int(input), number >= 0 {
        
    
        // Check if the input is a palindrome
        if isPalindrome(input) {
            print("true")
        } else {
            print("false")
        }
    } else {
        // If the input is not a valid positive integer
        print("Usage: please input a non-negative integer")
    }
}

main()

```

{% endraw %}

Palindromic Number in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Kaalid

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).