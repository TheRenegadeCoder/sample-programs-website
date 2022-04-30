---

title: Reverse String in Objective C
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Reverse String in Objective C page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Objective C
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).