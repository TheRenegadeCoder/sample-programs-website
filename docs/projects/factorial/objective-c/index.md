---
title: Factorial in Objective C
layout: default
date: 2020-10-01
featured-image: factorial-in-every-language.jpg
last-modified: 2020-10-01

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Objective C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective_c
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

[Factorial](https://sampleprograms.io/projects/factorial) in [Objective C](https://sampleprograms.io/languages/objective-c) was written by:

- niftycode

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).