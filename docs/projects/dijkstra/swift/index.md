---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-05-03
featured-image: dijkstra-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- dijkstra
- swift
title: Dijkstra in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/dijkstra/swift/how-to-implement-the-solution.md
- sources/programs/dijkstra/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Dijkstra](https://sampleprograms.io/projects/dijkstra) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = """
    Usage: please provide three inputs: a serialized matrix, a source node and a destination node
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

func parseArguments(from args: [String]) -> (matrix: [[Int]], source: Int, destination: Int)? {
    guard args.count == 4,
        let flat = parseList(args[1]),
        let source = Int(args[2].trimmed),
        let destination = Int(args[3].trimmed)
    else {
        return nil
    }

    let n = Int(Double(flat.count).squareRoot())

    guard n * n == flat.count,
        (0..<n).contains(source),
        (0..<n).contains(destination)
    else {
        return nil
    }

    let matrix = flat.chunked(into: n)

    for row in matrix {
        if row.contains(where: { $0 < 0 }) {
            return nil
        }
    }

    return (matrix, source, destination)
}

func shortestPath(matrix: [[Int]], from source: Int, to destination: Int) -> Int? {
    let n = matrix.count
    var dist = Array(repeating: Int.max, count: n)
    var visited = Set<Int>()

    dist[source] = 0

    for _ in 0..<n {
        // pick unvisited node with smallest distance
        guard
            let u = (0..<n)
                .lazy
                .filter({ !visited.contains($0) })
                .min(by: { dist[$0] < dist[$1] }),
            dist[u] != Int.max
        else {
            break
        }

        if u == destination { return dist[u] }

        visited.insert(u)

        let baseDist = dist[u]
        let row = matrix[u]

        for v in 0..<n where row[v] > 0 {
            let newDist = baseDist + row[v]
            if newDist < dist[v] {
                dist[v] = newDist
            }
        }
    }

    return dist[destination] == Int.max ? nil : dist[destination]
}

guard let (matrix, source, destination) = parseArguments(from: CommandLine.arguments) else {
    print(usage)
    exit(1)
}

if let result = shortestPath(matrix: matrix, from: source, to: destination) {
    print(result)
} else {
    print(usage)
}

```

{% endraw %}

Dijkstra in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).