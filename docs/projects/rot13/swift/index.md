---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-03
featured-image: rot13-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- rot13
- swift
title: Rot13 in Swift
title1: Rot13 in
title2: Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/swift/how-to-implement-the-solution.md
- sources/programs/rot13/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = "Usage: please provide a string to encrypt"

extension StringProtocol {
    var rot13: String {
        String(
            unicodeScalars.map { scalar in
                switch scalar {
                case "A"..."M", "a"..."m":
                    return Character(UnicodeScalar(scalar.value + 13)!)
                case "N"..."Z", "n"..."z":
                    return Character(UnicodeScalar(scalar.value - 13)!)
                default:
                    return Character(scalar)
                }
            }
        )
    }
}

guard
    let input = CommandLine.arguments.dropFirst().first,
    !input.isEmpty
else {
    print(usage)
    exit(1)
}

print(input.rot13)

```

{% endraw %}

Rot13 in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).