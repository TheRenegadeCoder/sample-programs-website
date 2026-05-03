---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-05-03
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- maximum-subarray
- swift
title: Maximum Subarray in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/swift/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = """
    Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"
    """

extension StringProtocol {
    var trimmed: String { trimmingCharacters(in: .whitespacesAndNewlines) }
}

extension Collection {
    subscript(safe index: Index) -> Element? {
        indices.contains(index) ? self[index] : nil
    }
}

func parseList(_ input: String?) -> [Int]? {
    guard let input = input, !input.isEmpty else { return nil }

    let values =
        input
        .split(separator: ",")
        .map { $0.trimmed }
        .compactMap(Int.init)

    return values.isEmpty ? nil : values
}

func maxSubarraySum(_ numbers: [Int]) -> Int {
    var best = numbers[0]
    var current = numbers[0]

    for value in numbers.dropFirst() {
        current = max(value, current + value)
        best = max(best, current)
    }

    return best
}

let args = CommandLine.arguments

guard let list = parseList(args[safe: 1]) else {
    print(usage)
    exit(1)
}

let result = maxSubarraySum(list)
print(result)

```

{% endraw %}

Maximum Subarray in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).