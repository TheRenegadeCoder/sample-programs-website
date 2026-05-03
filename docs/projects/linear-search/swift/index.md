---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-05-03
featured-image: linear-search-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- linear-search
- swift
title: Linear Search in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/swift/how-to-implement-the-solution.md
- sources/programs/linear-search/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = """
    Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")
    """

extension StringProtocol {
    var trimmed: String { trimmingCharacters(in: .whitespacesAndNewlines) }
}

extension Collection {
    subscript(safe index: Index) -> Element? {
        indices.contains(index) ? self[index] : nil
    }
}

extension Collection where Element: Equatable {
    func linearSearch(for target: Element) -> Index? {
        firstIndex(of: target)
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

    return values.isEmpty ? nil : (values, target)
}

guard let (values, target) = parseInput(CommandLine.arguments) else {
    print(usage)
    exit(1)
}

print(values.linearSearch(for: target) != nil)

```

{% endraw %}

Linear Search in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).