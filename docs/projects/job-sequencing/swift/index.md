---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-05-03
featured-image: job-sequencing-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- job-sequencing
- swift
title: Job Sequencing in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/job-sequencing/swift/how-to-implement-the-solution.md
- sources/programs/job-sequencing/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = """
    Usage: please provide a list of profits and a list of deadlines
    """

extension StringProtocol {
    var trimmed: String { trimmingCharacters(in: .whitespacesAndNewlines) }
}

func sequenceJobs(profits: [Int], deadlines: [Int]) -> Int {
    let jobs = zip(profits, deadlines)
        .sorted { $0.0 > $1.0 }

    guard let maxDeadline = deadlines.max() else { return 0 }

    var slots = Array(repeating: false, count: maxDeadline + 1)
    var totalProfit = 0

    for (profit, deadline) in jobs {
        let limit = min(deadline, maxDeadline)
        for slot in stride(from: limit, through: 1, by: -1) where !slots[slot] {
            slots[slot] = true
            totalProfit += profit
            break
        }
    }

    return totalProfit
}

func parseList(_ input: String) -> [Int]? {
    let parts =
        input
        .split(separator: ",")
        .map { $0.trimmed }

    let values = parts.compactMap(Int.init)

    guard values.count == parts.count else { return nil }
    return values
}

let args = CommandLine.arguments

guard args.count == 3,
    let profits = parseList(args[1]),
    let deadlines = parseList(args[2]),
    profits.count == deadlines.count
else {
    print(usage)
    exit(1)
}

print(sequenceJobs(profits: profits, deadlines: deadlines))

```

{% endraw %}

Job Sequencing in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).