---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-05-03
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- insertion-sort
- swift
title: Insertion Sort in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/insertion-sort/swift/how-to-implement-the-solution.md
- sources/programs/insertion-sort/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = """
    Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"
    """

extension StringProtocol {
    var trimmed: String { trimmingCharacters(in: .whitespacesAndNewlines) }
}

func parseIntegers(from args: [String]) -> [Int]? {
    guard args.count == 2 else { return nil }

    let parts = args[1].split(separator: ",", omittingEmptySubsequences: false)
    let values = parts.compactMap { Int($0.trimmed) }

    guard values.count == parts.count,
        values.count >= 2
    else {
        return nil
    }

    return values
}

extension MutableCollection where Self: BidirectionalCollection {
    mutating func insertionSort(by areInIncreasingOrder: (Element, Element) -> Bool) {
        guard count > 1 else { return }

        var i = index(after: startIndex)

        while i < endIndex {
            let key = self[i]
            var j = i

            while j > startIndex {
                let prev = index(before: j)

                if areInIncreasingOrder(key, self[prev]) {
                    self[j] = self[prev]
                    j = prev
                } else {
                    break
                }
            }

            self[j] = key
            i = index(after: i)
        }
    }
}

guard var numbers = parseIntegers(from: CommandLine.arguments) else {
    print(usage)
    exit(1)
}

numbers.insertionSort(by: <)

print(numbers.map(String.init).joined(separator: ", "))

```

{% endraw %}

Insertion Sort in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).