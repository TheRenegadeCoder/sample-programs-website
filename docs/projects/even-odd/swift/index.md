---

title: Even Odd in Swift
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Even Odd in Swift page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).