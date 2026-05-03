---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-03
featured-image: factorial-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- factorial
- swift
title: Factorial in Swift
title1: Factorial
title2: in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/swift/how-to-implement-the-solution.md
- sources/programs/factorial/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = """
    Usage: please input a non-negative integer
    """

extension FixedWidthInteger {
    var factorial: Self? {
        guard self >= 0 else { return nil }
        guard self > 1 else { return 1 }

        var result: Self = 1

        for i in 2...self {
            let (value, overflow) = result.multipliedReportingOverflow(by: i)
            if overflow { return nil }
            result = value
        }

        return result
    }
}

extension StringProtocol {
    var trimmed: String { trimmingCharacters(in: .whitespacesAndNewlines) }
}

guard
    let raw = CommandLine.arguments.dropFirst().first?.trimmed,
    let n = Int(raw),
    let result = n.factorial
else {
    print(usage)
    exit(1)
}

print(result)

```

{% endraw %}

Factorial in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).