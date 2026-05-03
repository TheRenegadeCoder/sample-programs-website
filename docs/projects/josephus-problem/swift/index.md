---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-05-03
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- josephus-problem
- swift
title: Josephus Problem in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/swift/how-to-implement-the-solution.md
- sources/programs/josephus-problem/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = "Usage: please input the total number of people and number of people to skip."

extension StringProtocol {
    var trimmed: String { trimmingCharacters(in: .whitespacesAndNewlines) }
}

extension Array {
    func argument(at index: Int) -> Element? {
        indices.contains(index) ? self[index] : nil
    }
}

func solveJosephus(_ n: Int, _ k: Int) -> Int {
    guard n > 0 else { return 0 }

    if k == 2 {
        let mostSignificantBit = 1 << (Int.bitWidth - 1 - n.leadingZeroBitCount)
        return 2 * (n - mostSignificantBit) + 1
    }

    return (2...n).reduce(0) { (survivor, i) in
        (survivor + k) % i
    } + 1
}

func parseInput(from args: [String]) -> (n: Int, k: Int)? {
    guard let rawN = args.argument(at: 1),
        let rawK = args.argument(at: 2),
        let n = Int(rawN.trimmed),
        let k = Int(rawK.trimmed),
        n > 0, k > 0
    else { return nil }

    return (n, k)
}

guard let (n, k) = parseInput(from: CommandLine.arguments) else {
    print(usage)
    exit(1)
}

print(solveJosephus(n, k))

```

{% endraw %}

Josephus Problem in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).