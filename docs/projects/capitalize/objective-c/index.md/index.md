# Capitalize in Objective C

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.