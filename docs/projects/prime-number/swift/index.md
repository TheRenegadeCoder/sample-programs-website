---
authors:
- Vidish Kumar
date: 2026-03-10
featured-image: prime-number-in-every-language.jpg
last-modified: 2026-03-10
layout: default
tags:
- prime-number
- swift
title: Prime Number in Swift
title1: Prime Number
title2: in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/swift/how-to-implement-the-solution.md
- sources/programs/prime-number/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = "Usage: please input a non-negative integer"

if CommandLine.arguments.count != 2 {
    print(usage)
    exit(0)
}

guard let number = Int(CommandLine.arguments[1]), number >= 0 else {
    print(usage)
    exit(0)
}

if number < 2 {
    print("composite")
    exit(0)
}

var isPrime = true
let limit = Int(Double(number).squareRoot())

if limit >= 2 {
    for i in 2...limit {
        if number % i == 0 {
            isPrime = false
            break
        }
    }
}

print(isPrime ? "prime" : "composite")
```

{% endraw %}

Prime Number in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Vidish Kumar

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).