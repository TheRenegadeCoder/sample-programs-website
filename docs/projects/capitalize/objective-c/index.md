---
authors:
- Cristiano Lopes
- rzuckerm
date: 2020-10-03
featured-image: capitalize-in-every-language.jpg
last-modified: 2023-12-16
layout: default
tags:
- capitalize
- objective-c
title: Capitalize in Objective C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/objective-c/how-to-implement-the-solution.md
- sources/programs/capitalize/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Objective C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective_c
#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
  NSAutoreleasePool *pool =[[NSAutoreleasePool alloc] init];
  NSString *usage = @"Usage: please provide a string";
  if (argc < 2) {
    printf("%s\n", [usage UTF8String]);
  }
  else {
    NSString* textFromArg = [NSString stringWithUTF8String:argv[1]];
    NSString* normalizedText = [textFromArg stringByTrimmingCharactersInSet:[NSCharacterSet newlineCharacterSet]];

    if([normalizedText length] < 1){
      printf("%s\n", [usage UTF8String]);
    }
    else {
      NSString *firstChar = [[normalizedText substringToIndex:1] uppercaseString];
      NSString *remainingText = [normalizedText substringFromIndex:1];
      NSString *capitalizedText = [firstChar stringByAppendingString:remainingText];
      printf("%s\n", [capitalizedText UTF8String]);
    }
  }

  [pool drain];
  return 0;
}

```

{% endraw %}

Capitalize in [Objective C](https://sampleprograms.io/languages/objective-c) was written by:

- Cristiano Lopes
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).