---
authors:
- Jeremy Griffith
- "\u0218tefan-Iulian Alecu"
date: 2018-03-21
featured-image: hello-world-in-objective-c.jpg
last-modified: 2026-04-30
layout: default
tags:
- hello-world
- objective-c
title: Hello World in Objective-C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/objective-c/how-to-implement-the-solution.md
- sources/programs/hello-world/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Objective-C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective-c
#import <Foundation/Foundation.h>

int main() {
    @autoreleasepool {
        NSString* message = @"Hello, World!\n";
        printf("%s", message.UTF8String);
    }
}
```

{% endraw %}

Hello World in [Objective-C](https://sampleprograms.io/languages/objective-c) was written by:

- Jeremy Griffith
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).