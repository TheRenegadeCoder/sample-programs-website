---
authors:
- Juan D Frias
- rzuckerm
date: 2019-10-16
featured-image: fizz-buzz-in-every-language.png
last-modified: 2023-12-16
layout: default
tags:
- fizz-buzz
- objective-c
title: Fizz Buzz in Objective C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/objective-c/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Objective C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective_c
#import <Foundation/Foundation.h>

int main (int argc, const char *argv[]){
    NSAutoreleasePool *pool =[[NSAutoreleasePool alloc] init];
    NSMutableString* fizzbuzz = [[NSMutableString alloc] init];

    int i;
    for (i = 1; i <= 100; ++i) {
        [fizzbuzz setString: @""];

        if (i % 3 == 0) {
            [fizzbuzz appendString: @"Fizz"];
        }

        if (i % 5 == 0) {
            [fizzbuzz appendString: @"Buzz"];
        }

        if ([fizzbuzz length] != 0) {
            printf("%s\n", [fizzbuzz UTF8String]);

        } else {
            printf("%d\n", i);
        }
    }

    [fizzbuzz release];
    [pool drain];
    return 0;
}

```

{% endraw %}

Fizz Buzz in [Objective C](https://sampleprograms.io/languages/objective-c) was written by:

- Juan D Frias
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).