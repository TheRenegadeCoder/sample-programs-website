# Import in C

## Solution

```C
#include <stdio.h>
#include "export.c"

extern char[] str;
void main()
{
    printf (str);
}

```