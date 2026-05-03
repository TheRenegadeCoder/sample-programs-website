---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-03
featured-image: minimum-spanning-tree-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- minimum-spanning-tree
- swift
title: Minimum Spanning Tree in Swift
title1: Minimum Spanning
title2: Tree in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/minimum-spanning-tree/swift/how-to-implement-the-solution.md
- sources/programs/minimum-spanning-tree/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Minimum Spanning Tree](https://sampleprograms.io/projects/minimum-spanning-tree) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = "Usage: please provide a comma-separated list of integers"

extension StringProtocol {
    var trimmed: String { trimmingCharacters(in: .whitespacesAndNewlines) }
}

func parseMatrix(_ input: String?) -> [[Int]]? {
    guard
        let input = input,
        !input.isEmpty
    else { return nil }

    let values =
        input
        .split(separator: ",")
        .map { Int($0.trimmed) }

    guard values.allSatisfy({ $0 != nil }) else { return nil }
    let flat = values.compactMap { $0 }

    let n = Int(Double(flat.count).squareRoot())
    guard n * n == flat.count else { return nil }

    return stride(from: 0, to: flat.count, by: n)
        .map { Array(flat[$0..<$0 + n]) }
}

func minimumSpanningTreeCost(_ matrix: [[Int]]) -> Int {
    let n = matrix.count
    guard n > 0 else { return 0 }

    var visited = Array(repeating: false, count: n)
    var minEdge = Array(repeating: Int.max, count: n)
    minEdge[0] = 0

    var total = 0

    for _ in 0..<n {
        guard
            let u = (0..<n)
                .filter({ !visited[$0] })
                .min(by: { minEdge[$0] < minEdge[$1] }),
            minEdge[u] != Int.max
        else { break }

        visited[u] = true
        total += minEdge[u]

        for (v, weight) in matrix[u].enumerated()
        where weight > 0 && !visited[v] && weight < minEdge[v] {
            minEdge[v] = weight
        }
    }

    return total
}

guard
    let matrix = parseMatrix(CommandLine.arguments.dropFirst().first)
else {
    print(usage)
    exit(1)
}

print(minimumSpanningTreeCost(matrix))

```

{% endraw %}

Minimum Spanning Tree in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).