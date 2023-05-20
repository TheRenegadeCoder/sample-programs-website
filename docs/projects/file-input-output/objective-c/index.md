---
title: File Input Output in Objective C
layout: default
date: 2020-10-04
featured-image: file-input-output-in-every-language.jpg
last-modified: 2020-10-04

---

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Objective C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective_c
#import <Foundation/Foundation.h>

NSString* readFileWith(NSString* path) {
  NSFileHandle* fileHandle = [NSFileHandle fileHandleForReadingAtPath:path];
  if (fileHandle) {
    @try {
      NSData* fileData  = [fileHandle availableData];
      return [[NSString alloc] initWithBytes:[fileData bytes] length:[fileData length] encoding:NSUTF8StringEncoding];
    } @catch (NSException *e) {
      NSLog(@"Error reading file %@", e);
      return nil;
    }
    @finally{
      [fileHandle closeFile];
    }
  }else{
    NSLog(@"File to read not found %@", path);
  }
  
};

BOOL writeFileWith(NSString* path, NSString* content) {
  NSFileHandle* fileHandle = [NSFileHandle fileHandleForWritingAtPath:path];
  if(fileHandle){
    @try {
      NSData* fileData  = [content dataUsingEncoding:NSUTF8StringEncoding];
      [fileHandle writeData:fileData];
      return YES;
    } @catch (NSException *e) {
      NSLog(@"Error writing file %@", e);
      return NO;
    }
    @finally{
      [fileHandle closeFile];
    }
  }else{
    NSLog(@"File to write not found %@", path);
  }
  
};

BOOL createFileIfNotExistsAt(NSString* path) {
  return [[NSFileManager defaultManager] createFileAtPath:path contents:nil attributes:nil];
};

int main(int argc, const char * argv[]) {
  @autoreleasepool {
    
    NSString* path = @"output.txt";
    if(createFileIfNotExistsAt(path)){
      BOOL result = writeFileWith(path, @"Hello!");
      if (result) {
        NSString* contents = readFileWith(path);
        if (contents) {
          NSLog(@"%@", contents);
        }
      }
    }else{
      NSLog(@"Unable to create file at %@", path);
    }
    
    return 0;
    
  }
  return 0;
}
```

{% endraw %}

[File Input Output](https://sampleprograms.io/projects/file-input-output) in [Objective C](https://sampleprograms.io/languages/objective-c) was written by:

- Cristiano Lopes

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).