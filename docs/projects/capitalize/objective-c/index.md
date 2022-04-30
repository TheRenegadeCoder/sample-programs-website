---

title: Capitalize in Objective C
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Capitalize in Objective C page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Objective C
#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
  @autoreleasepool {
    
    NSLog(@"Enter the text to be capitalized: ");
    NSString* textFromStdin = [[NSString alloc] initWithData:[[NSFileHandle fileHandleWithStandardInput] availableData] encoding:NSUTF8StringEncoding];
    
    NSString* normalizedText = [textFromStdin stringByTrimmingCharactersInSet:[NSCharacterSet newlineCharacterSet]];
    
    if([normalizedText length] < 1){
      NSLog(@"Usage: please provide a string");
      return 0;
    }
    
    NSString *firstChar = [[normalizedText substringToIndex:1] uppercaseString];
    NSString *remainingText = [normalizedText substringFromIndex:1];
    NSString *capitalizedText = [firstChar stringByAppendingString:remainingText];
    
    NSLog(@"%@", capitalizedText);
    
    return 0;
    
  }
  return 0;
}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).