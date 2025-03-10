---
authors:
- Maximillian Naza
date: 2025-01-18
featured-image: depth-first-search-in-every-language.jpg
last-modified: 2025-01-18
layout: default
tags:
- c
- depth-first-search
title: Depth First Search in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/depth-first-search/c/how-to-implement-the-solution.md
- sources/programs/depth-first-search/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Depth First Search](https://sampleprograms.io/projects/depth-first-search) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

#define MAX_NODES 100

int adjacency_matrix[MAX_NODES][MAX_NODES];
int vertex_values[MAX_NODES];
int num_nodes;
bool visited[MAX_NODES];

bool dfs(int node, int target) {
    if (vertex_values[node] == target) {
        return true;
    }
    visited[node] = true;
    for (int i = 0; i < num_nodes; i++) {
        if (adjacency_matrix[node][i] && !visited[i]) {
            if (dfs(i, target)) {
                return true;
            }
        }
    }
    return false;
}

bool depth_first_search(int target) {
    memset(visited, 0, sizeof(visited));
    for (int i = 0; i < num_nodes; i++) {
        if (!visited[i] && dfs(i, target)) {
            return true;
        }
    }
    return false;
}

void parse_matrix(char* input) {
    char* token = strtok(input, ", ");
    int i = 0, j = 0;
    while (token != NULL) {
        adjacency_matrix[i][j] = atoi(token);
        j++;
        if (j == num_nodes) {
            i++;
            j = 0;
        }
        token = strtok(NULL, ", ");
    }
}

void parse_values(char* input) {
    char* token = strtok(input, ", ");
    int i = 0;
    while (token != NULL) {
        vertex_values[i++] = atoi(token);
        token = strtok(NULL, ", ");
    }
}

int main(int argc, char* argv[]) {
    if (argc != 4 || !*argv[1] || !*argv[2] || !*argv[3]) {
        printf("Usage: please provide a tree in an adjacency matrix form (\"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0\") together with a list of vertex values (\"1, 3, 5, 2, 4\") and the integer to find (\"4\")");
        return 1;
    }

    char* matrix_str = argv[1];
    char* values_str = argv[2];
    int target = atoi(argv[3]);

    int total_elements = 1;
    for (char* p = matrix_str; *p; p++) {
        if (*p == ',') total_elements++;
    }

    num_nodes = (int)sqrt(total_elements);

    parse_matrix(matrix_str);
    parse_values(values_str);

    bool result = depth_first_search(target);
    printf(result ? "true\n" : "false\n");

    return 0;
}


```

{% endraw %}

Depth First Search in [C](https://sampleprograms.io/languages/c) was written by:

- Maximillian Naza

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).