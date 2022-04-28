# Fizz Buzz in C

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C
#include <stdio.h>

int main(void)
{
    for (unsigned int i = 1; i <= 100; i++) {
        if (i % 15 == 0) {
            puts("FizzBuzz");
        } else if (i % 3 == 0) {
            puts("Fizz");
        } else if (i % 5 == 0) {
            puts("Buzz");
        } else {
            printf("%u\n", i);
        }
    }
    return 0;
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.