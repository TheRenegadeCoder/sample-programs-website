---

---

# Even Odd in Objective C

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.