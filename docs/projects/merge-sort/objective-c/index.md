---
authors:
- Harshal Singh Raushan
- rzuckerm
- "\u0218tefan-Iulian Alecu"
date: 2020-10-03
featured-image: merge-sort-in-every-language.jpg
last-modified: 2026-04-30
layout: default
tags:
- merge-sort
- objective-c
title: Merge Sort in Objective-C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/merge-sort/objective-c/how-to-implement-the-solution.md
- sources/programs/merge-sort/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Objective-C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective-c
#import <Foundation/Foundation.h>

@interface NSString (Parsing)
- (nullable NSArray<NSNumber*>*)strictIntegerList;
@end

@implementation NSString (Parsing)

- (NSArray<NSNumber*>*)strictIntegerList {
    NSArray<NSString*>* parts = [self componentsSeparatedByString:@","];
    NSMutableArray<NSNumber*>* results =
        [NSMutableArray arrayWithCapacity:parts.count];
    NSCharacterSet* invertedDigits =
        NSCharacterSet.decimalDigitCharacterSet.invertedSet;

    for (NSString* raw in parts) {
        NSString* s = [raw stringByTrimmingCharactersInSet:
                               NSCharacterSet.whitespaceAndNewlineCharacterSet];
        if (s.length == 0) return nil;

        NSString* core = ([s hasPrefix:@"-"] || [s hasPrefix:@"+"])
                             ? [s substringFromIndex:1]
                             : s;
        if (core.length == 0 ||
            [core rangeOfCharacterFromSet:invertedDigits].location !=
                NSNotFound)
            return nil;

        [results addObject:@(s.longLongValue)];
    }
    return (results.count >= 2) ? results : nil;
}

@end

@interface NSArray (Sorting)
- (NSArray<NSNumber*>*)sortedArrayUsingMergeSort;
@end

@interface NSArray (SortingInternal)
- (NSArray<NSNumber*>*)recursivelySortedArray;
- (NSArray<NSNumber*>*)mergedWithArray:(NSArray<NSNumber*>*)other;
@end

@implementation NSArray (Sorting)

- (NSArray<NSNumber*>*)sortedArrayUsingMergeSort {
    if (self.count < 2) return self;
    return [self recursivelySortedArray];
}

@end

@implementation NSArray (SortingInternal)

- (NSArray<NSNumber*>*)recursivelySortedArray {
    if (self.count < 2) return self;

    NSUInteger mid = self.count / 2;

    NSArray* left =
        [[self subarrayWithRange:NSMakeRange(0, mid)] recursivelySortedArray];

    NSArray* right =
        [[self subarrayWithRange:NSMakeRange(mid, self.count - mid)]
            recursivelySortedArray];

    return [left mergedWithArray:right];
}

- (NSArray<NSNumber*>*)mergedWithArray:(NSArray<NSNumber*>*)other {
    NSMutableArray* result =
        [NSMutableArray arrayWithCapacity:self.count + other.count];

    NSUInteger i = 0, j = 0;

    while (i < self.count && j < other.count) {
        if ([self[i] compare:other[j]] != NSOrderedDescending) {
            [result addObject:self[i++]];
        } else {
            [result addObject:other[j++]];
        }
    }

    if (i < self.count) {
        [result addObjectsFromArray:[self subarrayWithRange:NSMakeRange(
                                                                i, self.count -
                                                                       i)]];
    }

    if (j < other.count) {
        [result
            addObjectsFromArray:[other
                                    subarrayWithRange:NSMakeRange(
                                                          j, other.count - j)]];
    }

    return result;
}

@end

int main(int argc, const char* argv[]) {
    @autoreleasepool {
        const char* usage =
            "Usage: please provide a list of at least two integers to sort in "
            "the format \"1, 2, 3, 4, 5\"";

        if (argc < 2) {
            puts(usage);
            return 1;
        }

        NSArray<NSNumber*>* numbers = @(argv[1]).strictIntegerList;

        if (!numbers) {
            puts(usage);
            return 1;
        }

        NSString* output = [[numbers sortedArrayUsingMergeSort]
            componentsJoinedByString:@", "];

        puts(output.UTF8String);
    }
    return 0;
}
```

{% endraw %}

Merge Sort in [Objective-C](https://sampleprograms.io/languages/objective-c) was written by:

- Harshal Singh Raushan
- rzuckerm
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).