---
title: Reverse String in Objective C
layout: default
date: 2019-10-14
featured-image: reverse-string-in-every-language.jpg
last-modified: 2019-10-14

---

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
    char textInput[1000];
    scanf ("%[^\n]%*c", textInput);
    NSString *userInput =[NSString stringWithUTF8String:textInput];
    if([userInput length] > 0){
        NSLog(@"\n%@", userInput);
        StringHelper* helper = [[StringHelper alloc] init];
        NSLog(@"\n%@", [helper reverseString: userInput]);  
    }
    [pool drain];
    return 0;
}
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Objective C](https://sampleprograms.io/languages/objective-c) was written by:

- Tim Lange

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).