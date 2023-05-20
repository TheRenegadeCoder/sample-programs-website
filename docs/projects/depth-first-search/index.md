---
title: Depth First Search in Every Language
layout: default
date: 2020-10-02
last-modified: 2022-05-18
featured-image: depth-first-search-in-every-language.jpg
tags: [depth-first-search]
authors:
  - mowies
  - the_renegade_coder

---

Welcome to the Depth First Search page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Depth first search is a type of graph search algorithm. It is often used on trees 
(which are special types of graphs).
It takes linear time to traverse a graph and find a given vertex, specifically O(num_vertices + num_edges).
This search algorithm is often used by web crawlers or in machine learning tasks.
There, the graph that should be traversed is often too big to be do it in a single run.
In such cases, the algorithm can be limited in different ways, for example by limiting depth or visited nodes.

The algorithm traverses the graph one node after the other, but takes priority in going deeper into 
the graph opposed to going broader first. This means, that it visits further children of children before visiting
potential siblings of them.


## Requirements

For the purposes of this project, we'll assume that the search space is a tree represented 
as an adjacency matrix together with a list of the vertex values in the tree.
Specifically, we'll accept three inputs on the command line: the tree adjacency matrix, the list of vertex
values (as integers) and the vertex value to find:

```console
./depth-first-search.lang "0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0" "2, 3, 6, 77, 44, 46, 1, 321, 5" "5"
```

Here we've chosen to represent the graph as a serialized list of integers. Since
the input string represents a square matrix, we should be able to take the
square root of the length to determine where the rows are in the string. In this
case, we have 81 values, so we must have 9 nodes.
If we reformat the input string as a matrix, we'll notice that the values in the
matrix represent the edges between vertices. Taking the vertex values into account as well, the resulting matrix
could look something like the following:

| Mapping | 2   | 3   | 6   | 77  | 44  | 46  | 1   | 321 | 5   |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2       | 0   | 1   | 1   | 1   | 0   | 0   | 0   | 0   | 0   |
| 3       | 1   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 0   |
| 6       | 1   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 0   |
| 77      | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   |
| 44      | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| 46      | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| 1       | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   |
| 321     | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   |
| 5       | 0   | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 0   |

This matrix will result in a tree that looks like this:

```console
            2
         /  |   \
       3    6    77
    /  |   / \     \
  44  46  1  321    5
```

If successful, the script should return `true`. Otherwise, the script should return `false`. 
If any user input errors occur, the script should output the following usage message:
`Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")`.


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Depth First Search.
In order to keep things simple, we split up the testing as follows:

- Depth First Search Valid Tests
- Depth First Search Invalid Tests

### Depth First Search Valid Tests

| Description | Tree Input | Vertex Values | Target Integer Input | Output |
| ----------- | ---------- | ------------- | -------------------- | ------ |
| Sample Input: First True | "0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" | "1, 3, 5, 2, 4" | "1" | "true" |
| Sample Input: Last True | "0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" | "1, 3, 5, 2, 4" | "4" | "true" |
| Sample Input: Middle True | "0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" | "1, 3, 5, 2, 4" | "5" | "true" |
| Sample Input: One True | "0" | "1" | "1" | "true" |
| Sample Input: One False | "0" | "1" | "6" | "false" |
| Sample Input: Many False | "0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" | "1, 3, 5, 2, 4" | "7" | "false" |

### Depth First Search Invalid Tests

| Description | Tree Input | Vertex Values | Target Integer Input |
| ----------- | ---------- | ------------- | -------------------- |
| No Input |  |  |  |
| Missing Input: Tree | "" | "1, 3, 5, 2, 4" | "4" |
| Missing Input: Vertex Values | "0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" | "" | "1" |
| Missing Input: Target | "0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" | "1, 3, 5, 2, 4" | "" |

All of these tests should output the following:

```
Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")
```


## Articles

- [Depth First Search in Algol68](https://sampleprograms.io/projects/depth-first-search/algol68)
- [Depth First Search in C++](https://sampleprograms.io/projects/depth-first-search/c-plus-plus)
- [Depth First Search in Euphoria](https://sampleprograms.io/projects/depth-first-search/euphoria)
- [Depth First Search in Mathematica](https://sampleprograms.io/projects/depth-first-search/mathematica)
- [Depth First Search in Php](https://sampleprograms.io/projects/depth-first-search/php)
- [Depth First Search in Python](https://sampleprograms.io/projects/depth-first-search/python)
- [Depth First Search in Rust](https://sampleprograms.io/projects/depth-first-search/rust)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Convex Hull)](https://sampleprograms.io/projects/convex-hull)

</div>

<div id="next" markdown="1">

[Next Project (Dijkstra) -->](https://sampleprograms.io/projects/dijkstra)

</div>

</nav>