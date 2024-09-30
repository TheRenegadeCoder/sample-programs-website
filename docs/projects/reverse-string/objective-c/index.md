---
authors:
- rzuckerm
- Tim Lange
date: 2019-10-14
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-12-16
layout: default
tags:
- objective-c
- reverse-string
title: Reverse String in Objective C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/objective-c/how-to-implement-the-solution.md
- sources/programs/reverse-string/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Objective C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective_c
#import <Foundation/Foundation.h>

@interface StringHelper:NSObject
- (NSString *) reverseString:(NSString *)stringToReverse;
@end

@implementation StringHelper 
- (NSString *) reverseString:(NSString *)stringToReverse {
    NSMutableString* result = [NSMutableString string];
    NSInteger index = [stringToReverse length];
    while (index > 0) {
        index--;
        NSRange range = NSMakeRange(index, 1);
        [result appendString:[stringToReverse substringWithRange:range]];
    }
    return result;
}

@end

int main (int argc, const char *argv[]){
    NSAutoreleasePool *pool =[[NSAutoreleasePool alloc] init];
    if (argc >= 2){
        NSString *userInput =[NSString stringWithUTF8String:argv[1]];
        if([userInput length] > 0){
            StringHelper* helper = [[StringHelper alloc] init];
            printf("%s\n", [[helper reverseString: userInput] UTF8String]);
        }
    }
    [pool drain];
    return 0;
}

```

{% endraw %}

Reverse String in [Objective C](https://sampleprograms.io/languages/objective-c) was written by:

- rzuckerm
- Tim Lange

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).