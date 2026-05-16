---
authors:
- niftycode
- rzuckerm
- Ștefan-Iulian Alecu
date: 2020-10-01
featured-image: factorial-in-every-language.jpg
last-modified: 2026-04-30
layout: default
tags:
- factorial
- objective-c
title: Factorial in Objective-C
title1: Factorial in
title2: Objective-C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/objective-c/how-to-implement-the-solution.md
- sources/programs/factorial/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Objective-C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

static unsigned long long Factorial(NSUInteger n) {
    if (n == 0 || n == 1) return 1;

    unsigned long long result = 1;
    for (NSUInteger i = 2; i <= n; i++) {
        result *= i;
    }

    return result;
}

int main(int argc, const char* argv[]) {
    @autoreleasepool {
        const char* usage = "Usage: please input a non-negative integer";
        if (argc < 2) {
            puts(usage);
            return 1;
        }

        NSNumber* number = @(argv[1]).strictIntegerNumber;

        if (!number || number.integerValue < 0) {
            puts(usage);
            return 1;
        }

        printf("%llu\n", Factorial(number.unsignedIntegerValue));
    }
    return 0;
}
```

{% endraw %}

Factorial in [Objective-C](https://sampleprograms.io/languages/objective-c) was written by:

- niftycode
- rzuckerm
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).