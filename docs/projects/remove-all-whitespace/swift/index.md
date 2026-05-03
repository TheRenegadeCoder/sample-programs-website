---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-03
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- remove-all-whitespace
- swift
title: Remove All Whitespace in Swift
title1: Remove All
title2: Whitespace in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/swift/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let usage = "Usage: please provide a string"

guard
    let input = CommandLine.arguments.dropFirst().first,
    !input.isEmpty
else {
    print(usage)
    exit(1)
}

print(input.filter { !$0.isWhitespace })

```

{% endraw %}

Remove All Whitespace in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).