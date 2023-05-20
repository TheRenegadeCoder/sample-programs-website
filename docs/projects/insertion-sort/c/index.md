---
title: Insertion Sort in C
layout: default
date: 2019-10-18
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2019-10-18

---

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>

void insertion_sort(long *, int); // insertion sort function

size_t parse_list(const char *orig_list, long **arr)          // used for parsing the input in array arr
{
    char *list;
    char *token;
    size_t num_elements = 0;
    int i;
    int curr_index = 0;
    long temp_num;

    /* find the length of the array */
    for (i = 0; orig_list[i]; i++) {
        if (orig_list[i] == ',') {
            num_elements++;
        }
    }

    /* if there are no commas, invalid input */
    if (num_elements == 0) {
        *arr = NULL;
        return 0;
    }

    /* since there is one more element than commas */
    num_elements++;

    /* allocate memory for the array */
    *arr = malloc(num_elements * sizeof(long));

    /* store numbers in the array */
    list = strdup(orig_list);
    token = strtok(list, ",");
    while (token != NULL) {
        errno = 0;
        temp_num = strtol(token, NULL, 10);
        if (errno != 0) {
            *arr = NULL;
            return 0;
        }

        (*arr)[curr_index++] = temp_num;

        token = strtok(NULL, ",");
    }

    free(list);

    return num_elements;
}

/* print the elements of array */
void print_array(long *arr, size_t num_elems)               
{
    int i;

    for (i = 0; i < num_elems - 1; i++) {
        printf("%ld, ", arr[i]);
    }

    printf("%ld\n", arr[num_elems - 1]);
}

/* error message if input is not in desired format */
void error_message()
{
    fputs("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"\n", stderr);
}

int main(int argc, char **argv)
{
    long *arr;
    long num_elements;

    if (argc < 2) {
        error_message();
        return 1;
    }

    num_elements = parse_list(argv[1], &arr);
    if (num_elements == 0) {
        error_message();
        return 1;
    }

    insertion_sort(arr, num_elements);
    print_array(arr, num_elements);

    free(arr);
}

void insertion_sort(long * arr_sort, int n)
{
    int i, j;
    int tmp;

    /* insertion sort logic */
    for(i = 1; i < n; i++)
    {
        tmp = arr_sort[i];
        for(j = i; j > 0 && arr_sort[j-1] > tmp; j--)
            arr_sort[j] = arr_sort[j-1];
        arr_sort[j] = tmp;
    }
}
```

{% endraw %}

[Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [C](https://sampleprograms.io/languages/c) was written by:

- sourabbr

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).