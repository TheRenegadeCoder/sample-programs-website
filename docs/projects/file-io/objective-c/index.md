---

title: File Io in Objective C
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the File Io in Objective C page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Objective C
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.