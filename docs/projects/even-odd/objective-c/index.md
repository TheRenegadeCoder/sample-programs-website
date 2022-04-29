---

title: Even Odd in Objective C

---

Welcome to the Even Odd in Objective C page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Objective C
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.