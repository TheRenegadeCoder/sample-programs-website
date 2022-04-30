---

title: Quick Sort in Objective C
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Quick Sort in Objective C page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```objective c
//
//  main.m
//
//  QuickSort in ObjC
//


#import <Foundation/Foundation.h>

@interface QuickSort: NSObject
 
- (NSArray *)quickSort:(NSArray *)dataset;
- (NSString *)getUserInput;

@end

@implementation QuickSort

- (NSArray *)quickSort:(NSArray *)dataset {
    
    int numberOfItems = (int)[dataset count];
    
    if (numberOfItems < 2) {
        return dataset;
    }
    
    // Here, the pivot variable is the item in the  m i d d l e  of the array.
    // There are also other ways to find the pivot item.
    int pivot = [[dataset objectAtIndex: (numberOfItems/2)] intValue];
    
    NSMutableArray *less = [NSMutableArray array];
    NSMutableArray *greater = [NSMutableArray array];
    NSMutableArray *equal = [NSMutableArray array];
    
    [equal addObject: @(pivot)];
    
    for (int i = 0; i < numberOfItems; i++) {
        
        int item = [[dataset objectAtIndex: i] intValue];
        
        if (item < pivot) {
            [less addObject: @(item)];
        } else if (item > pivot) {
            [greater addObject: @(item)];
        } else if (i != (numberOfItems/2) && pivot == item) {
            [equal addObject: @(item)];
        }
        
    }
    
    NSMutableArray *returnSortedArray = [NSMutableArray array];
    [returnSortedArray addObjectsFromArray: [self quickSort: less]];
    [returnSortedArray addObjectsFromArray: equal];
    [returnSortedArray addObjectsFromArray: [self quickSort: greater]];
     
    return returnSortedArray;
    
}

- (NSString *)getUserInput {

    NSFileHandle *handle = [NSFileHandle fileHandleWithStandardInput];
    NSData *data = handle.availableData;
    NSString *input = [[NSString alloc]initWithData:data encoding:NSUTF8StringEncoding];
    
    NSCharacterSet *set = [NSCharacterSet newlineCharacterSet];
    NSString *userInput = [input stringByTrimmingCharactersInSet:set];

    return userInput;
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        
        QuickSort *quickSort = [[QuickSort alloc] init];
        
        // Hardcoded values
        // NSArray *data = @[@33, @12, @104, @87, @12, @60, @93, @6, @18, @40, @52, @22, @43];
        
        // Command line input
        NSLog(@"Enter comma separated values: ");
        NSString* userInput = [quickSort getUserInput];
        
        NSArray *data = [userInput componentsSeparatedByString:@","];
        
        NSArray *sortedArray = [quickSort quickSort: (NSArray *)data];
        
        NSLog(@"%@", sortedArray);
        
    }
    return 0;
}

@end
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).