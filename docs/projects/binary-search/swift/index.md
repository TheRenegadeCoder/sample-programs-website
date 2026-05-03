---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-03
featured-image: binary-search-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- binary-search
- swift
title: Binary Search in Swift
title1: Binary Search
title2: in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/swift/how-to-implement-the-solution.md
- sources/programs/binary-search/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = """
    Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")
    """

extension StringProtocol {
    var trimmed: String { trimmingCharacters(in: .whitespacesAndNewlines) }
}

extension Collection where Element: Comparable {
    var isSorted: Bool { zip(self, dropFirst()).allSatisfy(<=) }
}

extension Collection {
    subscript(safe index: Index) -> Element? {
        indices.contains(index) ? self[index] : nil
    }
}

extension RandomAccessCollection where Element: Comparable {
    func binarySearch(for target: Element) -> Index? {
        var low = startIndex
        var high = index(before: endIndex)

        while low <= high {
            let distance = self.distance(from: low, to: high)
            let mid = index(low, offsetBy: distance / 2)

            let value = self[mid]

            if value == target { return mid }
            if value < target {
                low = index(after: mid)
            } else {
                high = index(before: mid)
            }
        }

        return nil
    }
}

func parseInput(_ args: [String]) -> ([Int], Int)? {
    guard
        let rawList = args[safe: 1],
        let rawTarget = args[safe: 2],
        let target = Int(rawTarget)
    else { return nil }

    let values =
        rawList
        .split(separator: ",")
        .compactMap { Int($0.trimmed) }

    guard !values.isEmpty, values.isSorted else {
        return nil
    }

    return (values, target)
}

guard let (values, target) = parseInput(CommandLine.arguments) else {
    print(usage)
    exit(1)
}

print(values.binarySearch(for: target) != nil)

```

{% endraw %}

Binary Search in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).