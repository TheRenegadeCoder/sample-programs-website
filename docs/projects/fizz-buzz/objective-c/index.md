---

title: Fizz Buzz in Objective C
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Fizz Buzz in Objective C page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective c
#import <Foundation/Foundation.h>

int main (int argc, const char *argv[]){
    NSAutoreleasePool *pool =[[NSAutoreleasePool alloc] init];
    NSMutableString* fizzbuzz = [[NSMutableString alloc] init];

    int i;
    for (i = 1; i <= 100; ++i) {
        [fizzbuzz setString: @""];

        if (i % 3 == 0) {
            [fizzbuzz appendString: @"Fizz"];
        }

        if (i % 5 == 0) {
            [fizzbuzz appendString: @"Buzz"];
        }

        if ([fizzbuzz length] != 0) {
            NSLog(fizzbuzz);

        } else {
            NSLog(@"%d", i);
        }
    }

    [fizzbuzz release];
    [pool drain];
    return 0;
}
```

{% endraw %}

Fizz Buzz in Objective C was written by:

- Juan D Frias

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).