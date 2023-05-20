---
title: Fibonacci in Swift
layout: default
date: 2020-10-11
featured-image: fibonacci-in-every-language.jpg
last-modified: 2020-10-11

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
import Foundation

func fibonacciProgram(_ n: Int) {
    var f1=0, f2=1, fib=1
    for i in 0..<n {
        print("\(i+1): \(fib)")
        fib = f1 + f2
        f1 = f2
        f2 = fib
    }
}


func fibonacciRecursive(_ n: Int) -> Int {
    if (n == 0) {
        return 0
    } else if (n == 1) {
        return 1
    }
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
}

/*
    Check if there is exactly one argument and if it can be parsed as an integer
*/
guard CommandLine.argc == 2, let number = Int(CommandLine.arguments[1]) else {
    print("Usage: please input the count of fibonacci numbers to output")
    exit(0)
}

fibonacciProgram(number)
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Swift](https://sampleprograms.io/languages/swift) was written by:

- smallblack9

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).