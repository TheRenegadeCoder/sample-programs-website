---
authors:
- Cristiano Lopes
- "\u0218tefan-Iulian Alecu"
date: 2020-10-04
featured-image: file-input-output-in-every-language.jpg
last-modified: 2026-04-30
layout: default
tags:
- file-input-output
- objective-c
title: File Input Output in Objective-C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/objective-c/how-to-implement-the-solution.md
- sources/programs/file-input-output/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Objective-C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective-c
#import <Foundation/Foundation.h>
#include <stdlib.h>

@interface NSString (FileIO)
- (BOOL)writeToDefaultPath:(NSString*)path error:(NSError**)error;
+ (nullable instancetype)stringWithDefaultPath:(NSString*)path
                                         error:(NSError**)error;
@end

@implementation NSString (FileIO)

- (BOOL)writeToDefaultPath:(NSString*)path error:(NSError**)error {
    NSURL* url = [NSURL fileURLWithPath:path];
    return [self writeToURL:url
                 atomically:YES
                   encoding:NSUTF8StringEncoding
                      error:error];
}

+ (instancetype)stringWithDefaultPath:(NSString*)path error:(NSError**)error {
    NSURL* url = [NSURL fileURLWithPath:path];
    return [self stringWithContentsOfURL:url
                                encoding:NSUTF8StringEncoding
                                   error:error];
}

@end

int main(int argc, const char* argv[]) {
    @autoreleasepool {
        NSString* path = @"output.txt";
        NSString* content = @"Hello!\nGoodbye!\n";
        NSError* error = nil;

        if (![content writeToDefaultPath:path error:&error]) {
            fprintf(stderr, "Write Error: %s\n",
                    error.localizedDescription.UTF8String);
            return EXIT_FAILURE;
        }

        NSString* result = [NSString stringWithDefaultPath:path error:&error];
        if (!result) {
            fprintf(stderr, "Read Error: %s\n",
                    error.localizedDescription.UTF8String);
            return EXIT_FAILURE;
        }

        printf("%s", result.UTF8String);
    }
    return EXIT_SUCCESS;
}
```

{% endraw %}

File Input Output in [Objective-C](https://sampleprograms.io/languages/objective-c) was written by:

- Cristiano Lopes
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).