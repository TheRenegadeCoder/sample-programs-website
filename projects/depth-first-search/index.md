---
title: Depth First Search in Every Language
layout: default
date: 2020-10-02
last-modified: 2020-10-02
featured-image: 
tags: [depth-first-search]
authors:
  - the_renegade_coder, mowies
---

In this article, we lay out all the requirements for a depth first search program.

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

![Visualization of depth first search][1]

## Requirements

For the purposes of this project, we'll assume that the search space is a tree represented 
as nested arrays filled with integers.
Specifically, we'll accept two inputs on the command line: the tree of integers and the integer to find:

```shell
./depth-first-search.lang "[1, [4, 5], 11, [12, [13, 65, [77]]]]" "4"
```

If successful, the script should return `true`. Otherwise, the script should return `false`. 
If any user input errors occur, the script should output the following usage message:
`Usage: please provide a tree in a nested list structure ("[1, [4, 5], 11, [12, [13, 65, [77]]]]") 
and the integer to find ("11")`.

## Testing

| Description | Tree Input | Target Integer Input | Output |
|-------------|------------|---------------|--------|
| No Input    |            |               | error\* |
| Missing Input: Tree | `""` | `4` | error\* |
| Missing Input: Target | `"[1, [3, 5, [2, 4]]]"` | `""` | error\* |
| Sample Input: First True | `[1, [3, 5, [7]]]` | `1` | `true` |
| Sample Input: Last True | `[1, [3, 5, [7]]]` | `7` | `true` |
| Sample Input: Middle True | `[1, [3, 5, [7]]]` | `5` | `true` |
| Sample Input: One True | `[5]` | `5` | `true` |
| Sample Input: One False | `[5]` | `7` | `false` |
| Sample Input: Many False | `[1, [3, 5, [7]]]` | `2` | `false` |

\*The error string to print: `Usage: please provide a tree in a nested list structure ("[1, [4, 5], 11, [12, [13, 65, 
[77]]]]") and the integer to find ("11")`

## Articles

{% include article_list.md collection=site.categories.depth-first-search %}

## Further Reading

- Fill out as needed

[1]: https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif
