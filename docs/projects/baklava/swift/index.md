---
title: Baklava in Swift
layout: default
date: 2018-10-20
featured-image: baklava-in-every-language.jpg
last-modified: 2018-10-20

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Swift](https://sampleprograms.io/languages/swift) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```swift
func baklava(maxWidth: Int) -> Void {
    for number in 0...maxWidth {
        print(String(repeatElement(" ", count:maxWidth-number)) + String(repeatElement("*", count:number*2+1)))
    }
    for number in (0...maxWidth-1).reversed() {
        print(String(repeatElement(" ", count:maxWidth-number)) + String(repeatElement("*", count:number*2+1)))
    }
}
baklava(maxWidth: 10)
```

{% endraw %}

[Baklava](https://sampleprograms.io/projects/baklava) in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Mark Magahis

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 22 2018 22:36:07. The solution was first committed on Oct 20 2018 11:42:26. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).