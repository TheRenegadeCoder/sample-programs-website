---
title: Even Odd in Objective C
layout: default
date: 2020-10-01
featured-image: even-odd-in-every-language.jpg
last-modified: 2020-10-01

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Objective C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective_c
#import <Foundation/Foundation.h>
int main (int argc, char *argv[])
{
 NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];
 
 int numbertotest, remainder;
 NSLog(@"Enter your number to be tested: ");
 scanf("%i", &numbertotest);
 
 remainder = numbertotest % 2;
 
 if (remainder == 0)
 NSLog(@"The number is even.");
 else
 NSLog(@"The number is odd.");
 
 [pool drain];
 return 0;
}
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Objective C](https://sampleprograms.io/languages/objective-c) was written by:

- Siddhant

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).