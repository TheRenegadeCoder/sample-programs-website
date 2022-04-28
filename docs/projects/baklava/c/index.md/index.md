# Baklava in C

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C
#include "stdio.h"

int main (void)
{

  for (int i = 0; i < 10; i++)
  {
    printf ("%.*s", (10 - i), "                                 ");
    printf ("%.*s", (i * 2 + 1), "******************************");
    printf ("\n");
  }

  for (int i = 10; -1 < i; i--)
  {
    printf ("%.*s", (10 - i), "                                 ");
    printf ("%.*s", (i * 2 + 1), "******************************");
    printf ("\n");
  }

  return 0;

}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.