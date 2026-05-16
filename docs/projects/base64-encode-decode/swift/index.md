---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-24
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2026-04-24
layout: default
tags:
- base64-encode-decode
- swift
title: Base64 Encode Decode in Swift
title1: Base64 Encode
title2: Decode in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/swift/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

private enum Base64Processor {
    private static let alphabet = CharacterSet(charactersIn: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=")

    static func isValid(_ string: String) -> Bool {
        guard string.count % 4 == 0 else { return false }
        
        guard string.unicodeScalars.allSatisfy(alphabet.contains) else { return false }
        
        let paddingCount = string.reversed().prefix(while: { $0 == "=" }).count
        guard paddingCount <= 2 else { return false }
        
        let withoutPadding = string.dropLast(paddingCount)
        return !withoutPadding.contains("=")
    }
}

func usage() -> Never {
    print("Usage: please provide a mode and a string to encode/decode")
    exit(1)
}

let args = CommandLine.arguments

guard args.count == 3 else { usage() }

let mode = args[1]
let input = args[2]

guard !input.isEmpty else { usage() }

switch mode {
case "encode":
    guard let data = input.data(using: .ascii) else { usage() }
    print(data.base64EncodedString())
    
case "decode":
    guard Base64Processor.isValid(input),
          let data = Data(base64Encoded: input),
          let decoded = String(data: data, encoding: .ascii) else {
        usage()
    }
    print(decoded)
    
default:
    usage()
}
```

{% endraw %}

Base64 Encode Decode in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).