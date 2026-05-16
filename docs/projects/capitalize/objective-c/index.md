---
authors:
- Cristiano Lopes
- rzuckerm
- Ștefan-Iulian Alecu
date: 2020-10-03
featured-image: capitalize-in-every-language.jpg
last-modified: 2026-04-30
layout: default
tags:
- capitalize
- objective-c
title: Capitalize in Objective-C
title1: Capitalize in
title2: Objective-C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/objective-c/how-to-implement-the-solution.md
- sources/programs/capitalize/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Objective-C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective-c
#import <Foundation/Foundation.h>

@interface NSString (CapitalizeFirst)
- (nullable NSString*)stringByCapitalizingFirstCharacter;
@end

@implementation NSString (CapitalizeFirst)

- (NSString*)stringByCapitalizingFirstCharacter {
    if (self.length == 0) return nil;

    NSRange firstCharRange = [self rangeOfComposedCharacterSequenceAtIndex:0];
    NSString* firstLetter =
        [[self substringWithRange:firstCharRange] uppercaseString];

    return [self stringByReplacingCharactersInRange:firstCharRange
                                         withString:firstLetter];
}

@end

int main(int argc, const char* argv[]) {
    @autoreleasepool {
        NSString* usage = @"Usage: please provide a string";
        NSString* input = argc > 1 ? @(argv[1]) : @"";

        NSString* trimmed =
            [input stringByTrimmingCharactersInSet:
                       NSCharacterSet.whitespaceAndNewlineCharacterSet];

        NSString* result = [trimmed stringByCapitalizingFirstCharacter];

        puts((result ?: usage).UTF8String);
    }

    return 0;
}

```

{% endraw %}

Capitalize in [Objective-C](https://sampleprograms.io/languages/objective-c) was written by:

- Cristiano Lopes
- rzuckerm
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).