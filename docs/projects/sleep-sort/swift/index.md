---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-05-03
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- sleep-sort
- swift
title: Sleep Sort in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/sleep-sort/swift/how-to-implement-the-solution.md
- sources/programs/sleep-sort/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

func sleepSorted(_ numbers: [Int]) -> [Int] {
    let group = DispatchGroup()
    let lock = NSLock()

    var result: [Int] = []

    let minValue = numbers.min() ?? 0
    let offset = minValue < 0 ? abs(minValue) : 0

    for number in numbers {
        group.enter()

        let delayMilliseconds = (number + offset) * 1000

        DispatchQueue.global().asyncAfter(deadline: .now() + .milliseconds(delayMilliseconds)) {
            lock.lock()
            result.append(number)
            lock.unlock()

            group.leave()
        }
    }

    group.wait()
    return result
}

guard let numbers = parseIntegers(from: CommandLine.arguments) else {
    print(usage)
    exit(1)
}

let sorted = sleepSorted(numbers)
print(sorted.map(String.init).joined(separator: ", "))

```

{% endraw %}

Sleep Sort in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).