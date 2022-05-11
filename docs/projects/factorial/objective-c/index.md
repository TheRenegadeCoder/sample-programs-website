---

title: Factorial in Objective C
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Factorial in Objective C page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective c
//
//  main.m
//  Factorial in ObjC
//


#import <Foundation/Foundation.h>

int fac(int n) {
    if (n > 1) {
        return fac(n -1) * n;
    }
    else {
        return 1;
    }
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        
        int input;
        
        NSLog (@"Enter a number: ");
        
        scanf("%d", &input);
        
        int result = fac(input);
        
        NSLog (@"\n %d", result);
        
    }
    return 0;
}
```

{% endraw %}

Factorial in Objective C was written by:

- niftycode

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).