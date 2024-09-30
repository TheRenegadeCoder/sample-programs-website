---
authors:
- rzuckerm
- Siddhant
date: 2020-10-01
featured-image: even-odd-in-every-language.jpg
last-modified: 2023-12-16
layout: default
tags:
- even-odd
- objective-c
title: Even Odd in Objective C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/objective-c/how-to-implement-the-solution.md
- sources/programs/even-odd/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Objective C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective_c
#import <Foundation/Foundation.h>

// Function to convert and validate the input string
// Source: ChatGPT
NSInteger convertAndValidateInput(NSString *inputString) {
    NSScanner *scanner = [NSScanner scannerWithString:inputString];
    NSInteger integerValue = 0;

    // Check if the scanner successfully scanned an integer
    if ([scanner scanInteger:&integerValue] && [scanner isAtEnd]) {
        return integerValue;
    } else {
        // Raise an exception for invalid input
        @throw [NSException exceptionWithName:@"InvalidInputException"
            reason:@"Input is not a valid integer"
            userInfo:nil];
    }
}

int main (int argc, char *argv[])
{
    NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];
    NSString *usage = @"Usage: please input a number";

    if (argc < 2) {
        printf("%s\n", [usage UTF8String]);
    }
    else {
        NSString* inputStr = [NSString stringWithUTF8String:argv[1]];
        @try {
            int input = (int)convertAndValidateInput(inputStr);
            int remainder = input % 2;
            if (remainder == 0) {
                printf("Even\n");
            }
            else {
                printf("Odd\n");
            }
        }
        @catch (NSException *) {
            printf("%s\n", [usage UTF8String]);
        }
    }

    [pool drain];
    return 0;
}
```

{% endraw %}

Even Odd in [Objective C](https://sampleprograms.io/languages/objective-c) was written by:

- rzuckerm
- Siddhant

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).