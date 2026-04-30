---
authors:
- rzuckerm
- "\u0218tefan-Iulian Alecu"
date: 2024-12-23
featured-image: baklava-in-every-language.jpg
last-modified: 2026-04-30
layout: default
tags:
- baklava
- objective-c
title: Baklava in Objective-C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/objective-c/how-to-implement-the-solution.md
- sources/programs/baklava/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Objective-C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective-c
#import <Foundation/Foundation.h>

int main() {
    @autoreleasepool {
        const NSInteger radius = 10;

        for (NSInteger i = -radius; i <= radius; i++) {
            NSUInteger paddingCount = (NSUInteger)labs(i);
            NSUInteger starCount = (radius - paddingCount) * 2 + 1;

            NSString* padding = [@"" stringByPaddingToLength:paddingCount
                                                  withString:@" "
                                             startingAtIndex:0];

            NSString* stars = [@"" stringByPaddingToLength:starCount
                                                withString:@"*"
                                           startingAtIndex:0];

            NSString* line = [padding stringByAppendingString:stars];

            puts(line.UTF8String);
        }
    }
    return 0;
}
```

{% endraw %}

Baklava in [Objective-C](https://sampleprograms.io/languages/objective-c) was written by:

- rzuckerm
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).