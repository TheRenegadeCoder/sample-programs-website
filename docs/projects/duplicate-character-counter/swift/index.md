---
authors:
- Lizock
date: 2024-11-12
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2024-11-12
layout: default
tags:
- duplicate-character-counter
- swift
title: Duplicate Character Counter in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/swift/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

func error() {
    print("Usage: please provide a string")
}

func duplicateCharacterCounter(string: [String]) {
    if string.isEmpty || string[0].isEmpty {
        error()
    } else {
        let input = string[0]
        var dict = [Character: Int]()

        for char in input{
        dict[char, default: 0] += 1
        }

        var flag = false
        for char in input{
            if let count = dict[char], count > 1 {
                flag = true
                print("\(char): \(count)")
                dict[char] = 0
            }
        }
        if !flag {
            print("No duplicate characters")
        }
    } 
}

let string = CommandLine.arguments.dropFirst().map { String($0) }
duplicateCharacterCounter(string: Array(string))
```

{% endraw %}

Duplicate Character Counter in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Lizock

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).