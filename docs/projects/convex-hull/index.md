---
title: Convex Hull in Every Language
layout: default
date: 2018-11-01
last-modified: 2022-05-18
featured-image: convex-hull-in-every-language.jpg
tags: [convex-hull]
authors:
  - the_renegade_coder

---

Welcome to the Convex Hull page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Suppose you have a set of points in the plane. The **convex hull** of this set is the smallest
convex polygon that contains all the points.

A good way to visualize the problem is this: Imagine each point is a nail sticking out of the plane,
and you stretch a rubber band around them and let it go. The band will contract and assume a shape
that encloses the nails. This shape is the convex hull.

Note that all vertices of the convex hull are points in the original set. So the convex hull is really
a subset of points from the original set, and there may be points that lie inside the polygon but are
not vertices of the convex hull.


## Requirements

Write a program that receives two command line arguments: strings in the form `x1, x2, x3 ...` and
`y1, y2, y3 ...` respectively, where `(xi, yi)` are the coordinates of the i-th point of the set.

Your program should be able to parse these lists into some internal representation in your choice
language (ideally an array). From there, the program should compute the convex hull of the set of points,
and output a list in the form

    (x1, y1)
    (x2, y2)
    ...

where `(xj, yj)` are the coordinates of the j-th vertex of the convex hull.

There are many algorithms to solve this problem. You may implement any of them.
Check this [great document by Jeff Erickson][2] for more details about the
problem and the different algorithms to solve it.

[2]: https://jeffe.cs.illinois.edu/pubs/pdf/convex.pdf


## Testing

Every project in the [Sample Programs repo](https://github.com/TheRenegadeCoder/sample-programs) should be tested.
In this section, we specify the set of tests specific to Convex Hull.
In order to keep things simple, we split up the testing as follows:

- Convex Hull Valid Tests
- Convex Hull Invalid Tests

### Convex Hull Valid Tests

| Description | Input X | Input Y | Output |
| ----------- | ------- | ------- | ------ |
| Sample Input: Triangle | "100, 180, 240" | "220, 120, 20" | "(100, 220)"<br>"(240, 20)"<br>"(180, 120)" |
| Sample Input: Pentagon | "100, 140, 320, 480, 280" | "240, 60, 40, 200, 300" | "(100, 240)"<br>"(140, 60)"<br>"(320, 40)"<br>"(480, 200)"<br>"(280, 300)" |
| Sample Input: Cluster | "260, 280, 300, 320, 600, 360, 20, 240" | "160, 100, 180, 140, 160, 320, 200, 0" | "(20, 200)"<br>"(240, 0)"<br>"(600, 160)"<br>"(360, 320)" |

### Convex Hull Invalid Tests

| Description | Input X | Input Y |
| ----------- | ------- | ------- |
| No Input |  |  |
| Missing Y | "100, 180, 240" |  |
| Invalid Shape | "100, 180" | "240, 300" |
| Different Cardinality | "100, 180, 240" | "240, 60, 40, 200, 300" |
| Invalid Integers | "100, 1A0, 240" | "220, 120, 20" |

All of these tests should output the following:

```
Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")
```


## Articles

- [Convex Hull in Algol68](https://sampleprograms.io/projects/convex-hull/algol68)
- [Convex Hull in Euphoria](https://sampleprograms.io/projects/convex-hull/euphoria)
- [Convex Hull in Java](https://sampleprograms.io/projects/convex-hull/java)
- [Convex Hull in Mathematica](https://sampleprograms.io/projects/convex-hull/mathematica)
- [Convex Hull in Php](https://sampleprograms.io/projects/convex-hull/php)
- [Convex Hull in Python](https://sampleprograms.io/projects/convex-hull/python)
- [Convex Hull in Rust](https://sampleprograms.io/projects/convex-hull/rust)

***

<nav class="project-nav">

<div id="prev" markdown="1">

[<-- Previous Project (Capitalize)](https://sampleprograms.io/projects/capitalize)

</div>

<div id="next" markdown="1">

[Next Project (Depth First Search) -->](https://sampleprograms.io/projects/depth-first-search)

</div>

</nav>