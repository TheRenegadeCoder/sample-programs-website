# Capitalize in C

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char *captialize(char str[]) {
    for(int i = 0; i < strlen(str); i++) {
        if(i == 0) {
            str[i] = toupper(str[i]);
        } else {
            continue;
        }
    }
    return str;
}

int main(int argc, char *argv[]) {
    if(argc == 2 && strlen(argv[1]) != 0) {
        printf("%s\n", captialize(argv[1]));
    } else if(argc > 2) {
        printf("Use quotes around multiple strings.\n");
    } else {
        printf("Usage: please provide a string\n");
    }

    return 0;
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.