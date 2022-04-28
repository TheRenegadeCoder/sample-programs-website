# Reverse String in C

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
    char *text;
    size_t textlen;

    /* check argument count (trailing arguments are ignored) */
    if (argc < 2) {
        fputs("Not enough arguments", stderr);
        return 1;
    }

    /* get text from command line and calculate length */
    text = argv[1];
    textlen = strlen(text);

    /* print characters in reverse */
    while (textlen-- > 0) {
        putchar(text[textlen]);
    }

    /* put a newline at the end */
    putchar('\n');

    return 0;
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.