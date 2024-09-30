---
authors:
- Harshal Singh Raushan
- rzuckerm
date: 2020-10-03
featured-image: merge-sort-in-every-language.jpg
last-modified: 2023-12-16
layout: default
tags:
- merge-sort
- objective-c
title: Merge Sort in Objective C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/merge-sort/objective-c/how-to-implement-the-solution.md
- sources/programs/merge-sort/objective-c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Objective C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

// Function to convert a comma-separated string to an array of integers
// Source: ChatGPT
NSArray *convertStringToListOfIntegers(NSString *inputString) {
    NSMutableArray *resultArray = [NSMutableArray array];

    // Separate the input string into components using the comma as a delimiter
    NSArray *components = [inputString componentsSeparatedByString:@","];

    // Convert each component to an integer using the previous function
    for (NSString *component in components) {
        NSNumber *numberValue = [NSNumber numberWithInteger:convertAndValidateInput(component)];
        [resultArray addObject:numberValue];
    }

    return [resultArray copy];
}

// Display array of integers
void displayListOfIntegers(NSArray *integerArray) {
    NSString *displayString = [integerArray componentsJoinedByString:@", "];
    printf("%s\n", [displayString UTF8String]);
}

////////////////MERGE-SORT////////////////
NSArray* mergeArrays(NSArray* A, NSArray* B) 
{
    NSMutableArray *orderedArray = [NSMutableArray new];
    long indexLeft = 0;
    long indexRight = 0;
    
    while (indexLeft < [A count] && indexRight < [B count]) {
        int leftValue = [[A objectAtIndex:indexLeft] intValue];
        int rightValue = [[B objectAtIndex:indexRight] intValue];
        if (leftValue < rightValue) {
            [orderedArray addObject:[A objectAtIndex:indexLeft++]];
        }else if (leftValue > rightValue){
            [orderedArray addObject:[B objectAtIndex:indexRight++]];
        }else { //equal values
            [orderedArray addObject:[A objectAtIndex:indexLeft++]];
            [orderedArray addObject:[B objectAtIndex:indexRight++]];
        }
    }
    
    //If one array has more positions than the other (odd lenght of the inital array)
    NSRange rangeRestLeft = NSMakeRange(indexLeft, A.count - indexLeft);
    NSRange rangeRestRight = NSMakeRange(indexRight, B.count - indexRight);
    NSArray *arrayTotalRight = [B subarrayWithRange:rangeRestRight];
    NSArray *arrayTotalLeft = [A subarrayWithRange:rangeRestLeft];
    arrayTotalLeft = [orderedArray arrayByAddingObjectsFromArray:arrayTotalLeft];
    NSArray *orderedArrayCompleted = [arrayTotalLeft arrayByAddingObjectsFromArray:arrayTotalRight];
    return orderedArrayCompleted;
}

NSArray* mergeSort(NSArray* randomArray){
    
    if ([randomArray count] < 2)
    {
        return randomArray;
    }
    int middlePivot = (int)[randomArray count]/2;
    NSRange rangeLeft = NSMakeRange(0, middlePivot);
    NSRange rangeRight = NSMakeRange(middlePivot, randomArray.count-middlePivot);
    NSArray *leftArray = [randomArray subarrayWithRange:rangeLeft];
    NSArray *rightArray = [randomArray subarrayWithRange:rangeRight];
    return mergeArrays(mergeSort(leftArray),mergeSort(rightArray));
}

int main(int argc, char *argv[]) {
    NSAutoreleasePool *pool =[[NSAutoreleasePool alloc] init];
    NSString *usage = @"Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"";
    if (argc < 2) {
        printf("%s\n", [usage UTF8String]);
    }
    else {
        NSString* inputStr = [NSString stringWithUTF8String:argv[1]];
        @try {
            NSArray *inputArray = convertStringToListOfIntegers(inputStr);
            if ([inputArray count] < 2) {
                printf("%s\n", [usage UTF8String]);
            }
            else {
                NSArray *sortedArray = mergeSort(inputArray);
                displayListOfIntegers(sortedArray);
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

Merge Sort in [Objective C](https://sampleprograms.io/languages/objective-c) was written by:

- Harshal Singh Raushan
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).