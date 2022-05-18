---

title: Convex Hull in Every Language
layout: default
date: 2018-11-01
last-modified: 2020-05-02
featured-image:
tags: [convex-hull]
authors:

---

Welcome to the Convex Hull page! Here, you'll find a description of the project as well as a list of sample programs written in various languages.

## Description

Suppose you have a set of points in the plane. The **convex hull** of this set is the smallest
convex polygon that contains all the points.

A good way to visualize the problem is this: Imagine each point is a nail sticking out of the plane,
and you stretch a rubber band around them and let it go. The band will contract and assume a shape
that encloses the nails. This shape is the convex hull.

![Rubber band visualization][1]

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


## Testing

Every project in the Sample Programs repo should be tested. In this section, we specify the set of tests specific to Convex Hull. To keep things simple, we split up testing into two subsets: valid and invalid. Valid tests refer to tests that occur under correct input conditions. Invalid tests refer to tests that occur on bad input (e.g., letters instead of numbers).

### Valid Tests

| Description         | Input X                                   | Input Y                                  | Output                                                           |
| ------------------- | ----------------------------------------- | ---------------------------------------- | ---------------------------------------------------------------- |
| X-Ordered triangle  | `"100, 180, 240"`                         | `"220, 120, 20"`                         | (100, 220)<br>(240, 20)<br>(180, 120)                            |
| Pentagon, clockwise | `"100, 140, 320, 480, 280"`               | `"240, 60, 40, 200, 300"`                | (100, 240)<br>(140, 60)<br>(320, 40)<br>(480, 200)<br>(280, 300) |
| Cluster in center   | `"260, 280, 300, 320, 600, 360, 20, 240"` | `"160, 100, 180, 140, 160, 320, 200, 0"` | (20, 200)<br>(240, 0)<br>(600, 160)<br>(360, 320)                |

**Note**: different algorithms could produce the output starting from a different point, and/or in the opposite direction.


### Invalid Tests

| Description           | Input X           | Input Y                   |
| --------------------- | ----------------- | ------------------------- |
| Too few values        | `"100, 180"`      | `"240, 60, 40, 200, 300"` |
| Different cardinality | `"100, 180, 240"` | `"240, 60, 40, 200, 300"` |
| Missing y             | `"100, 180, 240"` |                           |
| Invalid integer       | `"100, 1A0, 240"` | `"220, 120, 20"`          |

All invalid tests should spit out a usage statement in the following form:

```
Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")
```


## Articles

- [Convex Hull in Java](https://sampleprograms.io/projects/convex-hull/java)
- [Convex Hull in Python](https://sampleprograms.io/projects/convex-hull/python)