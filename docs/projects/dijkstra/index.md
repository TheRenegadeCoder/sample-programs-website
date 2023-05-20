---
title: Dijkstra in Every Language
layout: default
date: 2019-10-28
last-modified: 2022-05-18
featured-image: dijkstra-in-every-language.jpg
authors:
  - fuboki10
  - the_renegade_coder

---

Welcome to the Dijkstra page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Dijkstra's algorithm (or Dijkstra's Shortest Path First algorithm, SPF algorithm) 
is an algorithm for finding the shortest paths between nodes in a graph, which 
may represent, for example, road networks. It was conceived by computer scientist 
Edsger W. Dijkstra in 1956 and published three years later.

Dijkstra's algorithm doesn't work for graphs with negative weight edges.

### Algorithm

Below are the detailed steps used in Dijkstra's algorithm to find the shortest path 
from a single source vertex to all other vertices in the given graph.

1. Create a set sptSet (shortest path tree set) that keeps track 
   of vertices included in shortest path tree, i.e., whose minimum 
   distance from source is calculated and finalized. Initially, 
   this set is empty.
2. Assign a distance value to all vertices in the input graph. 
   Initialize all distance values as INFINITE. Assign distance 
   value as 0 for the source vertex so that it is picked first.
3. While sptSet doesn't include all vertices
   1. Pick a vertex u which is not there in sptSet and has minimum distance value.
   2. Include u to sptSet.
   3. Update distance value of all adjacent vertices of u. To update the distance 
   values, iterate through all adjacent vertices. For every adjacent vertex v, if 
   sum of distance value of u (from source) and weight of edge u-v, is less than 
   the distance value of v, then update the  distance value of v.

### Example

Dijkstra's algorithm to find the shortest path between a and b. It picks 
the unvisited vertex with the low distance, calculates the distance through 
it to each unvisited neighbor, and updates the neighbor's distance if smaller. 
Mark visited (set to red) when done with neighbors.

![Dijkstra_Animation](https://user-images.githubusercontent.com/35429211/67672949-a2dcfd80-f981-11e9-862a-96bd0ec9ba83.gif)


## Requirements

```console
./dijkstra.lang "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" "0" "1"
```

Here we've chosen to represent the matrix as a serialized list of integers. Since
the input string represents a square matrix, we should be able to take the
square root of the length to determine where the rows are in the string. In this
case, we have 25 values, so we must have 5 nodes.
If we reformat the input string as a matrix, we'll notice that the values in the
matrix represent the edge weight between each node. For example, we
could reformat our example to look something like the following:

| Mapping | 0   | 1   | 2   | 3   | 4   |
| ------- | --- | --- | --- | --- | --- |
| 0       | 0   | 2   | 0   | 6   | 0   |
| 1       | 2   | 0   | 3   | 8   | 5   |
| 2       | 0   | 3   | 0   | 0   | 7   |
| 3       | 6   | 8   | 0   | 0   | 9   |
| 4       | 0   | 5   | 7   | 9   | 0   |

Then we take the Source and the Destination.

The Output will be the Cost of the Shortest Path from Source to Destination.  


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Dijkstra.
In order to keep things simple, we split up the testing as follows:

- Dijkstra Valid Tests
- Dijkstra Invalid Tests

### Dijkstra Valid Tests

| Description | Matrix | Source | Destination | Output |
| ----------- | ------ | ------ | ----------- | ------ |
| Sample Input: Routine | "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "0" | "1" | "2" |

### Dijkstra Invalid Tests

| Description | Matrix | Source | Destination |
| ----------- | ------ | ------ | ----------- |
| No Input |  |  |  |
| Empty Input | "" | "" | "" |
| Non-Square Input | "1, 0, 3, 0, 5, 1" | "1" | "2" |
| No Destination | "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "0" | "" |
| No Source Or Destination | "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "" | "" |
| Source Or Destination < 0 | "0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "-1" | "2" |
| Weight < 0 | "0, 2, 0, -6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, -6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "1" | "2" |
| Source Or Destination > Number Of Vertices | "0, 2, 0, -6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, -6, 8, 0, 0, 9, 0, 5, 7, 9, 0" | "1" | "10" |
| No Way | "0, 0, 0, 0" | "0" | "1" |

All of these tests should output the following:

```
Usage: please provide three inputs: a serialized matrix, a source node and a destination node
```


## Articles

- [Dijkstra in Algol68](https://sampleprograms.io/projects/dijkstra/algol68)
- [Dijkstra in C++](https://sampleprograms.io/projects/dijkstra/c-plus-plus)
- [Dijkstra in Euphoria](https://sampleprograms.io/projects/dijkstra/euphoria)
- [Dijkstra in Javascript](https://sampleprograms.io/projects/dijkstra/javascript)
- [Dijkstra in Mathematica](https://sampleprograms.io/projects/dijkstra/mathematica)
- [Dijkstra in Php](https://sampleprograms.io/projects/dijkstra/php)
- [Dijkstra in Python](https://sampleprograms.io/projects/dijkstra/python)
- [Dijkstra in Rust](https://sampleprograms.io/projects/dijkstra/rust)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Depth First Search)](https://sampleprograms.io/projects/depth-first-search)

</div>

<div id="next" markdown="1">

[Next Project (Duplicate Character Counter) -->](https://sampleprograms.io/projects/duplicate-character-counter)

</div>

</nav>