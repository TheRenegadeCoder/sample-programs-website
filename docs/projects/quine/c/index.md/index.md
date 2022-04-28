---

---

# Quine in C

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C
#include "stdio.h"
int main() { char* s="#include %cstdio.h%c%cint main() { char* s=%c%s%c; printf(s,34,34,10,34,s,34,10); return 0; }%c"; printf(s,34,34,10,34,s,34,10); return 0; }

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.