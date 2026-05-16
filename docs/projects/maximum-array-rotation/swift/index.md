---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-03
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- maximum-array-rotation
- swift
title: Maximum Array Rotation in Swift
title1: Maximum Array
title2: Rotation in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/swift/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = """
    Usage: please provide a list of integers (e.g. "8, 3, 1, 2")
    """

extension StringProtocol {
    var trimmed: String { trimmingCharacters(in: .whitespacesAndNewlines) }
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

func maximumArrayRotation(_ nums: [Int]) -> Int {
    let n = nums.count
    let totalSum = nums.reduce(0, +)

    var current = nums.enumerated().reduce(0) { $0 + $1.element * $1.offset }
    var best = current

    var suffix = nums

    for _ in 1..<n {
        let last = suffix.removeLast()
        suffix.insert(last, at: 0)

        current += totalSum - n * last
        best = max(best, current)
    }

    return best
}

let args = CommandLine.arguments

guard
    args.count == 2,
    let input = args.dropFirst().first,
    let numbers = parseList(input)
else {
    print(usage)
    exit(1)
}

print(maximumArrayRotation(numbers))

```

{% endraw %}

Maximum Array Rotation in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).