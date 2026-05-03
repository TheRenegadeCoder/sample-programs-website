---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-05-03
featured-image: file-input-output-in-every-language.jpg
last-modified: 2026-05-03
layout: default
tags:
- file-input-output
- swift
title: File Input Output in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/swift/how-to-implement-the-solution.md
- sources/programs/file-input-output/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

let url = URL(fileURLWithPath: "output.txt")
let text = "Line 1\nLine 2\nLine 3"

// Write: Create file and write content
try? text.write(to: url, atomically: true, encoding: .utf8)

// Read: Print file content directly
if let content = try? String(contentsOf: url, encoding: .utf8) {
    print(content)
}

```

{% endraw %}

File Input Output in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).