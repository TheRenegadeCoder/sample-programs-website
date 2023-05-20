---
title: Even Odd in Swift
layout: default
date: 2020-10-05
featured-image: even-odd-in-every-language.jpg
last-modified: 2020-10-05

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
// for System.exit()
import Foundation


/*
    Check if there is exactly one argument and if it can be parsed as an integer
*/
guard CommandLine.argc == 2, let number = Int(CommandLine.arguments[1]) else {
    print("Usage: please input a number")
    exit(0)
}

let is_even = number % 2 == 0

if is_even {
    print("Even")
} else {
    print("Odd")
}
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Jonas Halstrup

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).