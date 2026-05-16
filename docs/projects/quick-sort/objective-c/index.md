---
authors:
- niftycode
- rzuckerm
- Ștefan-Iulian Alecu
date: 2020-10-04
featured-image: quick-sort-in-every-language.jpg
last-modified: 2026-04-30
layout: default
tags:
- objective-c
- quick-sort
title: Quick Sort in Objective-C
title1: Quick Sort in
title2: Objective-C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quick-sort/objective-c/how-to-implement-the-solution.md
- sources/programs/quick-sort/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Objective-C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

static void quickSortRange(NSMutableArray<NSNumber*>* array, NSInteger left,
                           NSInteger right) {
    if (left >= right) return;

    NSInteger i = left;
    NSInteger j = right;
    long long pivot = array[left + (right - left) / 2].longLongValue;

    while (i <= j) {
        while (array[i].longLongValue < pivot) i++;
        while (array[j].longLongValue > pivot) j--;

        if (i <= j) {
            [array exchangeObjectAtIndex:i withObjectAtIndex:j];
            i++;
            j--;
        }
    }

    quickSortRange(array, left, j);
    quickSortRange(array, i, right);
}

@interface NSArray (Sorting)
- (NSArray<NSNumber*>*)sortedArrayUsingQuickSort;
@end

@implementation NSArray (Sorting)

- (NSArray<NSNumber*>*)sortedArrayUsingQuickSort {
    if (self.count < 2) return self;

    NSMutableArray<NSNumber*>* buffer = [self mutableCopy];
    quickSortRange(buffer, 0, buffer.count - 1);

    return buffer;
}

@end

int main(int argc, const char* argv[]) {
    @autoreleasepool {
        const char* usage =
            "Usage: please provide a list of at least two integers to sort "
            "in the format \"1, 2, 3, 4, 5\"";

        if (argc < 2) {
            puts(usage);
            return 1;
        }

        NSArray<NSNumber*>* numbers = [@(argv[1]) strictIntegerList];

        if (!numbers) {
            puts(usage);
            return 1;
        }

        NSString* output = [[numbers sortedArrayUsingQuickSort]
            componentsJoinedByString:@", "];

        puts(output.UTF8String);
    }

    return 0;
}
```

{% endraw %}

Quick Sort in [Objective-C](https://sampleprograms.io/languages/objective-c) was written by:

- niftycode
- rzuckerm
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).