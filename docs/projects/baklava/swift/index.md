---
authors:
- Mark Magahis
date: 2018-10-20
featured-image: baklava-in-every-language.jpg
last-modified: 2018-10-22
layout: default
tags:
- baklava
- swift
title: Baklava in Swift
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/swift/how-to-implement-the-solution.md
- sources/programs/baklava/swift/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

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

Baklava in [Swift](https://sampleprograms.io/languages/swift) was written by:

- Mark Magahis

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).