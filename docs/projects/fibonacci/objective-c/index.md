---
authors:
- Renato
- rzuckerm
- "\u0218tefan-Iulian Alecu"
date: 2020-10-01
featured-image: fibonacci-in-every-language.jpg
last-modified: 2026-04-30
layout: default
tags:
- fibonacci
- objective-c
title: Fibonacci in Objective-C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/objective-c/how-to-implement-the-solution.md
- sources/programs/fibonacci/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Objective-C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

static void PrintFibonacciSequence(NSUInteger count) {
    unsigned long long previous = 0;
    unsigned long long current = 1;

    for (NSUInteger i = 1; i <= count; i++) {
        printf("%ld: %llu\n", i, current);

        unsigned long long next = previous + current;
        previous = current;
        current = next;
    }
}

int main(int argc, const char* argv[]) {
    @autoreleasepool {
        const char* usage =
            "Usage: please input the count of fibonacci numbers to output";

        if (argc < 2) {
            puts(usage);
            return 1;
        }

        NSNumber* number = @(argv[1]).strictIntegerNumber;

        if (!number || number.integerValue < 0) {
            puts(usage);
            return 1;
        }

        PrintFibonacciSequence(number.unsignedIntegerValue);
    }
    return 0;
}

```

{% endraw %}

Fibonacci in [Objective-C](https://sampleprograms.io/languages/objective-c) was written by:

- Renato
- rzuckerm
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).