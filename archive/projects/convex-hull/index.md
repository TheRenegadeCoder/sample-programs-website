---
title: Convex Hull in Every Language
layout: default
date: 2018-11-01
last-modified: 2020-05-02
featured-image:
tags: [convex-hull]
authors:
---

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

The following table contains various test cases that you can use to
verify the correctness of your solution; please note that different algorithms
could produce the output starting from a different point, and/or in the opposite direction:

| Description           | Input X | Input Y | Output |
|-----------------------|---------|---------|--------|
| X-Ordered triangle    | 100, 180, 240                         | 220, 120, 20                         | (100, 220)<br>(240, 20)<br>(180, 120)                            |
| Pentagon, clockwise   | 100, 140, 320, 480, 280               | 240, 60, 40, 200, 300                | (100, 240)<br>(140, 60)<br>(320, 40)<br>(480, 200)<br>(280, 300) |
| Cluster in center     | 260, 280, 300, 320, 600, 360, 20, 240 | 160, 100, 180, 140, 160, 320, 200, 0 | (20, 200)<br>(240, 0)<br>(600, 160)<br>(360, 320)                |
| Too few values        | 100, 180                              | 240, 60, 40, 200, 300                | Error "Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")" reported                          |
| Different cardinality | 100, 180, 240                         | 240, 60, 40, 200, 300                | Error "Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")" reported                          |
| Missing y             | 100, 180, 240                         |                                      | Error "Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")" reported                          |
| Invalid integer       | 100, 1A0, 240                         | 220, 120, 20                         | Error "Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")" reported                          |


## Articles

{% include article_list.md collection=site.categories.convex-hull %}

## Further Reading

- Fill as needed

[1]: https://upload.wikimedia.org/wikipedia/commons/d/de/ConvexHull.svg
[2]: http://jeffe.cs.illinois.edu/teaching/compgeom/notes/01-convexhull.pdf
