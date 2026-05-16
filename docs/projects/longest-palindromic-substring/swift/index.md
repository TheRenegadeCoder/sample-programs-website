---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-03
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- longest-palindromic-substring
- swift
title: Longest Palindromic Substring in Swift
title1: Longest Palindromic
title2: Substring in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/swift/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = """
    Usage: please provide a string that contains at least one palindrome
    """

extension Collection {
    subscript(safe index: Index) -> Element? {
        indices.contains(index) ? self[index] : nil
    }
}

func findLongestPalindrome(_ s: String) -> String {
    let originalChars = Array(s)
    guard !originalChars.isEmpty else { return "" }

    let processed: [Character] = ["#"] + originalChars.flatMap { [$0, "#"] }

    let n = processed.count
    var radii = Array(repeating: 0, count: n)
    var center = 0
    var rightBoundary = 0

    var maxRadius = 0
    var centerOfMax = 0

    for i in 0..<n {
        if i < rightBoundary {
            let mirror = 2 * center - i
            radii[i] = min(rightBoundary - i, radii[mirror])
        }

        var left = i - (1 + radii[i])
        var right = i + (1 + radii[i])

        while left >= 0 && right < n, processed[left] == processed[right] {
            radii[i] += 1
            left -= 1
            right += 1
        }

        if i + radii[i] > rightBoundary {
            center = i
            rightBoundary = i + radii[i]
        }

        if radii[i] > maxRadius {
            maxRadius = radii[i]
            centerOfMax = i
        }
    }

    guard maxRadius > 1 else { return "" }

    let start = (centerOfMax - maxRadius) / 2
    let resultRange = start..<(start + maxRadius)

    return String(originalChars[resultRange])
}

guard let input = CommandLine.arguments[safe: 1], !input.isEmpty else {
    print(usage)
    exit(1)
}

let result = findLongestPalindrome(input)

if result.isEmpty {
    print(usage)
    exit(1)
} else {
    print(result)
}

```

{% endraw %}

Longest Palindromic Substring in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).