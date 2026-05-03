---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-05-03
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- swift
- transpose-matrix
title: Transpose Matrix in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/swift/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = "Usage: please enter the dimension of the matrix and the serialized matrix"

extension StringProtocol {
    var trimmed: String { trimmingCharacters(in: .whitespacesAndNewlines) }
}

func parseInt(_ s: String?) -> Int? {
    guard let s = s else { return nil }
    return Int(s.trimmed)
}

func parseMatrix(_ input: String, rows: Int, cols: Int) -> [Int]? {
    let values = input
        .split(separator: ",")
        .compactMap { Int($0.trimmed) }

    guard values.count == rows * cols else { return nil }
    return values
}

func transpose(_ matrix: [Int], rows: Int, cols: Int) -> [Int] {
    var result = [Int]()
    result.reserveCapacity(matrix.count)

    for c in 0..<cols {
        for r in 0..<rows {
            result.append(matrix[r * cols + c])
        }
    }

    return result
}

let args = CommandLine.arguments

guard
    args.count >= 4,
    let cols = parseInt(args[1]),
    let rows = parseInt(args[2]),
    let matrix = parseMatrix(args[3], rows: rows, cols: cols)
else {
    print(usage)
    exit(1)
}

let result = transpose(matrix, rows: rows, cols: cols)
print(result.map(String.init).joined(separator: ", "))
```

{% endraw %}

Transpose Matrix in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).