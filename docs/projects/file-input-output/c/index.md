---
title: File Input Output in C
layout: default
date: 2018-09-12
featured-image: file-input-output-in-every-language.jpg
last-modified: 2018-09-12

---

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
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

[File Input Output](https://sampleprograms.io/projects/file-input-output) in [C](https://sampleprograms.io/languages/c) was written by:

- Christoph Böhmwalder

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).