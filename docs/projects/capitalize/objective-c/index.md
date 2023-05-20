---
title: Capitalize in Objective C
layout: default
date: 2020-10-03
featured-image: capitalize-in-every-language.jpg
last-modified: 2020-10-03

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Objective C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective_c
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

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Objective C](https://sampleprograms.io/languages/objective-c) was written by:

- Cristiano Lopes

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).