---

title: Fizz Buzz in Objective C
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Fizz Buzz in Objective C page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Objective C
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.