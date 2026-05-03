---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-05-03
featured-image: depth-first-search-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- depth-first-search
- swift
title: Depth First Search in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/depth-first-search/swift/how-to-implement-the-solution.md
- sources/programs/depth-first-search/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Depth First Search](https://sampleprograms.io/projects/depth-first-search) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = """
    Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")
    """

extension Collection {
    func chunked(into size: Int) -> [[Element]] {
        stride(from: 0, to: count, by: size).map { offset in
            let start = index(startIndex, offsetBy: offset)
            let end = index(start, offsetBy: size, limitedBy: endIndex) ?? endIndex
            return Array(self[start..<end])
        }
    }
}

extension StringProtocol {
    var trimmed: String { trimmingCharacters(in: .whitespacesAndNewlines) }
}

func parseList(_ input: String) -> [Int]? {
    let parts = input.split(separator: ",").map { $0.trimmed }
    let values = parts.compactMap(Int.init)

    guard values.count == parts.count, !values.isEmpty else {
        return nil
    }

    return values
}

func parseArguments(_ args: [String]) -> (adj: [[Int]], labels: [Int], target: Int)? {
    guard args.count == 4,
        let flat = parseList(args[1]),
        let labels = parseList(args[2]),
        let target = Int(args[3].trimmed),
        flat.count == labels.count * labels.count
    else {
        return nil
    }

    let adj = flat.chunked(into: labels.count)
    return (adj, labels, target)
}

func depthFirstSearch(adj: [[Int]], labels: [Int], target: Int) -> Bool {
    guard !labels.isEmpty else { return false }

    var visited = Set<Int>()

    func dfs(_ node: Int) -> Bool {
        guard !visited.contains(node) else { return false }

        if labels[node] == target { return true }
        visited.insert(node)

        for (neighbor, edge) in adj[node].enumerated() where edge == 1 {
            if dfs(neighbor) { return true }
        }

        return false
    }

    return dfs(0)
}

guard let (adj, labels, target) = parseArguments(CommandLine.arguments) else {
    print(usage)
    exit(1)
}

print(depthFirstSearch(adj: adj, labels: labels, target: target))

```

{% endraw %}

Depth First Search in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).