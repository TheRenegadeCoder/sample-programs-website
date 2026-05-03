---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-03
featured-image: merge-sort-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- merge-sort
- swift
title: Merge Sort in Swift
title1: Merge Sort
title2: in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/merge-sort/swift/how-to-implement-the-solution.md
- sources/programs/merge-sort/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

extension RangeReplaceableCollection
where Self: MutableCollection, Self: RandomAccessCollection, Element: Comparable {
    mutating func mergeSort(by areInIncreasingOrder: (Element, Element) -> Bool) {
        var buffer = Array(self)
        var temp = buffer

        mergeSort(&buffer, &temp, start: 0, end: buffer.count, by: areInIncreasingOrder)

        self = Self(buffer)
    }

    private func mergeSort(
        _ buffer: inout [Element],
        _ temp: inout [Element],
        start: Int,
        end: Int,
        by areInIncreasingOrder: (Element, Element) -> Bool
    ) {
        guard end - start > 1 else { return }

        let mid = (start + end) / 2

        mergeSort(&buffer, &temp, start: start, end: mid, by: areInIncreasingOrder)
        mergeSort(&buffer, &temp, start: mid, end: end, by: areInIncreasingOrder)

        merge(&buffer, &temp, start: start, mid: mid, end: end, by: areInIncreasingOrder)
    }

    private func merge(
        _ buffer: inout [Element],
        _ temp: inout [Element],
        start: Int,
        mid: Int,
        end: Int,
        by areInIncreasingOrder: (Element, Element) -> Bool
    ) {
        var i = start
        var j = mid
        var k = start

        while i < mid && j < end {
            if areInIncreasingOrder(buffer[i], buffer[j]) {
                temp[k] = buffer[i]
                i += 1
            } else {
                temp[k] = buffer[j]
                j += 1
            }
            k += 1
        }

        while i < mid {
            temp[k] = buffer[i]
            i += 1
            k += 1
        }

        while j < end {
            temp[k] = buffer[j]
            j += 1
            k += 1
        }

        for index in start..<end {
            buffer[index] = temp[index]
        }
    }
}

guard var numbers = parseIntegers(from: CommandLine.arguments) else {
    print(usage)
    exit(1)
}

numbers.mergeSort(by: <)

print(numbers.map(String.init).joined(separator: ", "))

```

{% endraw %}

Merge Sort in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).