---
authors:
- rzuckerm
date: 2024-12-23
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-23
layout: default
tags:
- baklava
- objective-c
title: Baklava in Objective C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/objective-c/how-to-implement-the-solution.md
- sources/programs/baklava/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Objective C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective_c
#import <Foundation/Foundation.h>

// Source:
// https://stackoverflow.com/questions/260945/create-nsstring-by-repeating-another-string-a-given-number-of-times
@interface NSString (Baklava)
- (NSString *) repeatString: (NSUInteger) times;
@end

@implementation NSString (Baklava)
- (NSString *) repeatString: (NSUInteger) times {
    return [
        @"" 
        stringByPaddingToLength: [self length] * times
        withString:self startingAtIndex: 0
    ];
}
@end

int main(int argc, const char * argv[]) {
    NSAutoreleasePool *pool =[[NSAutoreleasePool alloc] init];

    int i;
    for (i = -10; i <= 10; i++) {
        int numSpaces = abs(i);
        int numStars = 21 - 2 * numSpaces;
        printf(
            "%s%s\n",
            [[@" " repeatString: numSpaces] UTF8String],
            [[@"*" repeatString: numStars] UTF8String]
        );
    }

    [pool drain];
    return 0;
}

```

{% endraw %}

Baklava in [Objective C](https://sampleprograms.io/languages/objective-c) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).