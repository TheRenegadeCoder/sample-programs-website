---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-03
featured-image: longest-common-subsequence-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- longest-common-subsequence
- swift
title: Longest Common Subsequence in Swift
title1: Longest Common
title2: Subsequence in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-common-subsequence/swift/how-to-implement-the-solution.md
- sources/programs/longest-common-subsequence/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Common Subsequence](https://sampleprograms.io/projects/longest-common-subsequence) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = """
    Usage: please provide two lists in the format "1, 2, 3, 4, 5"
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

func parseInput(_ args: [String]) -> ([Int], [Int])? {
    guard
        let a = args.dropFirst().first,
        let b = args.dropFirst().dropFirst().first,
        let listA = parseList(a),
        let listB = parseList(b)
    else {
        return nil
    }

    return (listA, listB)
}

func longestCommonSubsequence(_ a: [Int], _ b: [Int]) -> [Int] {
    let n = a.count
    let m = b.count

    var dp = Array(
        repeating: Array(repeating: 0, count: m + 1),
        count: n + 1
    )

    for i in 1...n {
        for j in 1...m {
            if a[i - 1] == b[j - 1] {
                dp[i][j] = dp[i - 1][j - 1] + 1
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            }
        }
    }

    var result: [Int] = []
    var i = n
    var j = m

    while i > 0 && j > 0 {
        if a[i - 1] == b[j - 1] {
            result.append(a[i - 1])
            i -= 1
            j -= 1
        } else if dp[i - 1][j] > dp[i][j - 1] {
            i -= 1
        } else {
            j -= 1
        }
    }

    return result.reversed()
}

guard let (a, b) = parseInput(CommandLine.arguments) else {
    print(usage)
    exit(1)
}

let lcs = longestCommonSubsequence(a, b)
print(lcs.map(String.init).joined(separator: ", "))

```

{% endraw %}

Longest Common Subsequence in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).