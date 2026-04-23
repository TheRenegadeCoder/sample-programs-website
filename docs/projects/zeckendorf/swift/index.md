---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-24
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-04-24
layout: default
tags:
- swift
- zeckendorf
title: Zeckendorf in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/swift/how-to-implement-the-solution.md
- sources/programs/zeckendorf/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

func fibs(upTo limit: Int) -> [Int] {
    guard limit >= 1 else { return [] }

    var result = [1, 2]
    while true {
        let next = result[result.count - 1] + result[result.count - 2]
        if next > limit { break }
        result.append(next)
    }
    return result
}

func zeckendorf(_ n: Int) -> String {
    guard n > 0 else { return "" }

    let fibsList = fibs(upTo: n).reversed()

    let result = fibsList.reduce(into: (remaining: n, out: [Int]())) { acc, f in
        if f <= acc.remaining {
            acc.out.append(f)
            acc.remaining -= f
        }
    }.out

    return result.map(String.init).joined(separator: ", ")
}

guard CommandLine.argc == 2,
      let n = Int(CommandLine.arguments[1]),
      n >= 0 else {
    print("Usage: please input a non-negative integer")
    exit(0)
}

print(zeckendorf(n))
```

{% endraw %}

Zeckendorf in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).