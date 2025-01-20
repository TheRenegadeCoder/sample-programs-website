---
authors:
- Maximillian Naza
date: 2025-01-20
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2025-01-20
layout: default
tags:
- c
- sleep-sort
title: Sleep Sort in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/sleep-sort/c/how-to-implement-the-solution.md
- sources/programs/sleep-sort/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>

pthread_mutex_t print_mutex = PTHREAD_MUTEX_INITIALIZER;
int *global_sorted;
int global_index = 0;
int global_total;

typedef struct {
    int number;
} ThreadPayload;

void* sortNumber(void* args) {
    ThreadPayload* payload = (ThreadPayload*) args;
    const int number = payload->number;

    sleep(number); // Sleep for number seconds

    pthread_mutex_lock(&print_mutex);
    global_sorted[global_index++] = number;
    pthread_mutex_unlock(&print_mutex);

    free(payload);
    return NULL;
}

void parseInput(const char *input, int **arr, int *n) {
    char *token;
    char *inputCopy = strdup(input);
    token = strtok(inputCopy, ",");

    while (token != NULL) {
        (*arr)[(*n)++] = atoi(token);
        token = strtok(NULL, ",");
    }

    free(inputCopy);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"\n");
        return 1;
    }

    const char *input = argv[1];
    if (strlen(input) == 0 || input[0] == ' ') {
        printf("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"\n");
        return 1;
    }

    int *arr = malloc(100 * sizeof(int));
    int n = 0;

    parseInput(input, &arr, &n);

    if (n < 2) {
        printf("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"\n");
        free(arr);
        return 1;
    }

    global_sorted = malloc(n * sizeof(int));
    global_total = n;

    pthread_t *threads = malloc(n * sizeof(pthread_t));

    for (int i = 0; i < n; i++) {
        ThreadPayload *payload = malloc(sizeof(ThreadPayload));
        payload->number = arr[i];
        pthread_create(&threads[i], NULL, sortNumber, (void *) payload);
    }

    for (int i = 0; i < n; i++) {
        pthread_join(threads[i], NULL);
    }

    for (int i = 0; i < n; i++) {
        printf("%d%s", global_sorted[i], (i < n - 1) ? ", " : "");
    }
    printf("\n");

    free(arr);
    free(threads);
    free(global_sorted);

    return 0;
}

```

{% endraw %}

Sleep Sort in [C](https://sampleprograms.io/languages/c) was written by:

- Maximillian Naza

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).