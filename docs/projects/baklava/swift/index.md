---

title: Baklava in Swift
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Baklava in Swift page! Here, you'll find the source code for this program as well as a description of how the program works.

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

Baklava in Swift was written by:

- Mark Magahis

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 22 2018 22:36:07. The solution was first committed on Oct 20 2018 11:42:26. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).