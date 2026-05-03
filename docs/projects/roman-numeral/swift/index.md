---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-05-03
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- roman-numeral
- swift
title: Roman Numeral in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/swift/how-to-implement-the-solution.md
- sources/programs/roman-numeral/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let romanValues: [Character: Int] = [
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
]

let usage = "Usage: please provide a string of roman numerals"
let error = "Error: invalid string of roman numerals"

func romanToInt(_ s: String) -> Int? {
    var total = 0
    var previous = 0

    for char in s.uppercased().reversed() {
        guard let value = romanValues[char] else { return nil }

        if value < previous {
            total -= value
        } else {
            total += value
            previous = value
        }
    }

    return total
}

guard let input = CommandLine.arguments.dropFirst().first else {
    print(usage)
    exit(1)
}

guard let result = romanToInt(input) else {
    print(error)
    exit(1)
}

print(result)

```

{% endraw %}

Roman Numeral in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).