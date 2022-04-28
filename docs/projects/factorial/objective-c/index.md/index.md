---

---

# Factorial in Objective C

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Objective C
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.