---
authors:
- Jeremy Grifski
- Vicrobot
date: 2019-10-22
featured-image: convex-hull-in-every-language.jpg
last-modified: 2022-05-14
layout: default
tags:
- convex-hull
- python
title: Convex Hull in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/convex-hull/python/how-to-implement-the-solution.md
- sources/programs/convex-hull/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Convex Hull](https://sampleprograms.io/projects/convex-hull) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
from math import sqrt
import sys

usage = 'Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")'


def dist(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return sqrt(abs((x2 - x1)**2 + (y2 - y1)**2))


def farthest(point, set_of_points):
    d = [(dist(point, i), i) for i in set_of_points]
    d = list(set(d))
    d = sorted(d, reverse=True)
    return d[0][1]


def orient(point1, point2, point3):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    val = ((x2-x1) * (y3-y1)) - ((y2 - y1) * (x3-x1))
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def next_hurdle(setofpoints, pivot, final_list):
    z = setofpoints
    final_list = final_list[1:]
    k = []
    for i in z:
        if i in final_list:
            continue
        bool1 = 1
        for j in z:
            if orient(pivot, i, j) == 1:
                bool1 = 0
                break
        if bool1 == 1:
            k.append(i)
    return farthest(pivot, k)


def foo(z):
    final_list = []
    topmost = [(i, j) for i, j in z if j == max(Y)]
    v1 = sorted(topmost)[0]
    final_list.append(v1)
    next_point = v1[0], v1[1] + 1
    pivot = v1
    while next_point != v1:
        next_point = next_hurdle(z, pivot, final_list)
        pivot = next_point
        final_list.append(next_point)
    return final_list


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(usage)
        sys.exit()

    X = [i.strip() for i in sys.argv[1].split(',') if i]
    Y = [i.strip() for i in sys.argv[2].split(',') if i]

    if len(X) != len(Y) or len(X) < 3 or not all(x.isdigit() for x in X) or not all(y.isdigit() for y in Y):
        print(usage)
        sys.exit()

    X = [int(i) for i in X]
    Y = [int(i) for i in Y]
    Z = list(set((zip(X, Y))))

    convex_polygon_coords = foo(Z)
    for coord in convex_polygon_coords:
        print(coord)

```

{% endraw %}

Convex Hull in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski
- Vicrobot

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).