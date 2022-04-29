---

title: Fibonacci in Objective C

---

Welcome to the Fibonacci in Objective C page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Objective C
#include <stdio.h>

int fibonacci(int n)
{
    return ( n<=2 ? 1 : fibonacci(n-1) + fibonacci(n-2) );
}

int main(void)
{
    int n;
    for (n=1; n<=16; n++)
        printf("%d, ", fibonacci(n));
    printf("...\n");
    return 0;
}
```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.