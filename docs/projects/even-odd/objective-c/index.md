---
authors:
- rzuckerm
- Siddhant
- "\u0218tefan-Iulian Alecu"
date: 2020-10-01
featured-image: even-odd-in-every-language.jpg
last-modified: 2026-04-30
layout: default
tags:
- even-odd
- objective-c
title: Even Odd in Objective-C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/objective-c/how-to-implement-the-solution.md
- sources/programs/even-odd/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Objective-C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective-c
#import <Foundation/Foundation.h>

@interface NSString (Parsing)
@property(nonatomic, readonly, nullable) NSNumber* strictIntegerNumber;
@end

@implementation NSString (Parsing)

- (NSNumber*)strictIntegerNumber {
    NSString* trimmed = [self
        stringByTrimmingCharactersInSet:NSCharacterSet
                                            .whitespaceAndNewlineCharacterSet];
    if (trimmed.length == 0) return nil;

    NSInteger offset = 0;
    if ([trimmed hasPrefix:@"-"] || [trimmed hasPrefix:@"+"]) {
        offset = 1;
    }

    if (trimmed.length <= offset) return nil;

    NSString* core = [trimmed substringFromIndex:offset];
    NSRange invalidRange =
        [core rangeOfCharacterFromSet:NSCharacterSet.decimalDigitCharacterSet
                                          .invertedSet];

    if (invalidRange.location != NSNotFound) {
        return nil;
    }

    return @(trimmed.longLongValue);
}

@end

int main(int argc, const char* argv[]) {
    @autoreleasepool {
        if (argc < 2) {
            puts("Usage: please input a number");
            return 1;
        }

        NSNumber* number = @(argv[1]).strictIntegerNumber;

        if (!number) {
            puts("Usage: please input a number");
            return 1;
        }

        puts(number.longLongValue % 2 == 0 ? "Even" : "Odd");
    }
    return 0;
}
```

{% endraw %}

Even Odd in [Objective-C](https://sampleprograms.io/languages/objective-c) was written by:

- rzuckerm
- Siddhant
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).