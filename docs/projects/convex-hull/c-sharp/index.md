---
authors:
- Ștefan-Iulian Alecu
date: 2025-07-29
featured-image: convex-hull-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- convex-hull
title: Convex Hull in C#
title1: Convex
title2: Hull in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/convex-hull/c-sharp/how-to-implement-the-solution.md
- sources/programs/convex-hull/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Convex Hull](https://sampleprograms.io/projects/convex-hull) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
﻿using System.Runtime.InteropServices;

if (
    args is not [var xInput, var yInput]
    || !TryParsePoints(xInput.AsSpan(), yInput.AsSpan(), out var points)
)
{
    return Usage();
}

points.Sort();

var hull = BuildHull(CollectionsMarshal.AsSpan(points), out int size);
for (int i = 0; i < size; i++)
    Console.WriteLine(hull[i]);

return 0;

static bool TryParsePoints(ReadOnlySpan<char> x, ReadOnlySpan<char> y, out List<Point> points)
{
    points = [];

    if (x.IsWhiteSpace() || y.IsWhiteSpace())
        return false;

    var list = new List<Point>();

    while (true)
    {
        if (!TryNext(ref x, out int xVal) || !TryNext(ref y, out int yVal))
            break;

        points.Add(new(xVal, yVal));
    }

    return x.IsEmpty && y.IsEmpty && points.Count >= 3;

    static bool TryNext(ref ReadOnlySpan<char> span, out int value)
    {
        int comma = span.IndexOf(',');
        var token = comma >= 0 ? span[..comma] : span;
        span = comma >= 0 ? span[(comma + 1)..] : [];
        return int.TryParse(token, out value);
    }
}

static Point[] BuildHull(Span<Point> points, out int size)
{
    int numPoints = points.Length;
    if (numPoints < 3)
    {
        size = numPoints;
        return points.ToArray();
    }

    var hull = new Point[numPoints * 2];
    int h = 0;

    for (int i = 0; i < numPoints; i++)
    {
        var p = points[i];

        while (h > 1 && Cross(hull[h - 2], hull[h - 1], p) <= 0)
            h--;

        hull[h++] = p;
    }

    int lower = h;

    for (int i = numPoints - 2; i >= 0; i--)
    {
        var p = points[i];

        while (h > lower && Cross(hull[h - 2], hull[h - 1], p) <= 0)
            h--;

        hull[h++] = p;
    }

    size = h - 1;
    return hull;

    static long Cross(Point o, Point a, Point b) =>
        (long)(a.X - o.X) * (b.Y - o.Y) - (long)(a.Y - o.Y) * (b.X - o.X);
}

static int Usage()
{
    Console.Error.WriteLine(
        """Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")"""
    );
    return 1;
}

public readonly record struct Point(int X, int Y) : IComparable<Point>
{
    public int CompareTo(Point other) => X != other.X ? X.CompareTo(other.X) : Y.CompareTo(other.Y);

    public override string ToString() => $"({X}, {Y})";
}

```

{% endraw %}

Convex Hull in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).