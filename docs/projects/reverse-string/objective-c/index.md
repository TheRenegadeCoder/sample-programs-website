---
authors:
- Tim Lange
- Ștefan-Iulian Alecu
date: 2019-10-14
featured-image: reverse-string-in-every-language.jpg
last-modified: 2026-04-30
layout: default
tags:
- objective-c
- reverse-string
title: Reverse String in Objective-C
title1: Reverse String
title2: in Objective-C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/objective-c/how-to-implement-the-solution.md
- sources/programs/reverse-string/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Objective-C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective-c
#import <Foundation/Foundation.h>

@interface NSString (Reversal)
@property(nonatomic, readonly) NSString* reversed;
@end

@implementation NSString (Reversal)

- (NSString*)reversed {
    NSUInteger len = self.length;
    if (len < 2) return self;

    unichar buffer[len];
    [self getCharacters:buffer range:NSMakeRange(0, len)];

    NSUInteger i = 0;
    NSUInteger j = len - 1;

    while (i < j) {
        unichar tmp = buffer[i];
        buffer[i++] = buffer[j];
        buffer[j--] = tmp;
    }

    return [NSString stringWithCharacters:buffer length:len];
}

@end

int main(int argc, const char* argv[]) {
    @autoreleasepool {
        NSString* input = argc > 1 ? @(argv[1]) : nil;
        NSString* output = input.reversed;
        puts(output.UTF8String);
    }
    return 0;
}

```

{% endraw %}

Reverse String in [Objective-C](https://sampleprograms.io/languages/objective-c) was written by:

- Tim Lange
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).