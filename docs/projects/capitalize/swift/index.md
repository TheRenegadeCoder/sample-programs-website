---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-24
featured-image: capitalize-in-every-language.jpg
last-modified: 2026-04-24
layout: default
tags:
- capitalize
- swift
title: Capitalize in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/swift/how-to-implement-the-solution.md
- sources/programs/capitalize/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let args = CommandLine.arguments.dropFirst()

let sentence = args
    .joined(separator: " ")
    .trimmingCharacters(in: .whitespacesAndNewlines)

guard !sentence.isEmpty else {
    print("Usage: please provide a string")
    exit(1)
}

let result = sentence.prefix(1).uppercased() + sentence.dropFirst()

print(result)
```

{% endraw %}

Capitalize in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).