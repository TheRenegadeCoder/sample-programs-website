---

---

Welcome to the File Io in C page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```C
#include <stdio.h>
#include <stdlib.h>

#define FILENAME "output.txt"

int write_file()
{
    FILE *handle;

    handle = fopen(FILENAME, "w");
    if (!handle) {
        perror("open file for writing");
        return 1;
    }

    fputs("A line of text\n", handle);
    fputs("Another line of text\n", handle);

    fclose(handle);
    return 0;
}

int read_file()
{
    char *line = NULL;
    ssize_t read;
    size_t len = 0;
    FILE *handle;

    handle = fopen(FILENAME, "r");
    if (!handle) {
        perror("open file for reading");
        return 1;
    }

    while ((read = getline(&line, &len, handle)) != -1) {
        printf("%s", line);
    }

    fclose(handle);
    free(line);

    return 0;
}

int main(int argc, char **argv)
{
    int rc;

    rc = write_file();
    if (rc != 0) {
        return EXIT_FAILURE;
    }

    rc = read_file();
    if (rc != 0) {
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.