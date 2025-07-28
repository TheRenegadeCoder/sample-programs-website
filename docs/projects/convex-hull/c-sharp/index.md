---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-29
featured-image: convex-hull-in-every-language.jpg
last-modified: 2025-07-29
layout: default
tags:
- c-sharp
- convex-hull
title: Convex Hull in C#
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
﻿using System;
using System.Collections.Generic;
using System.Linq;

public record Point(int X, int Y) : IComparable<Point>
{
    public int CompareTo(Point? other)
         => other is null ? 1 : X != other.X ? X.CompareTo(other.X) : Y.CompareTo(other.Y);

    public override string ToString() => $"({X}, {Y})";

    public static bool operator <(Point left, Point right) => left.CompareTo(right) < 0;
    public static bool operator >(Point left, Point right) => left.CompareTo(right) > 0;
}

public static class ConvexHull
{
    private static void ShowUsage()
    {
        Console.Error.WriteLine("Usage: please provide at least 3 x and y coordinates as separate lists (e.g. \"100, 440, 210\")");
    }

    private static List<int> ParseIntegerList(string input)
    {
        if (string.IsNullOrWhiteSpace(input))
        {
            ShowUsage();
            Environment.Exit(1);
        }

        var list = input
            .Split(',', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(part => int.TryParse(part, out var val)
                ? val
                : throw new ArgumentException($"Invalid integer value: '{part}'"))
            .ToList();

        if (list.Count < 3)
        {
            ShowUsage();
            Environment.Exit(1);
        }

        return list;
    }


    /// <summary>
    /// Calculates the cross product of vectors OA and OB.
    /// Positive result means counter-clockwise turn.
    /// Negative result means clockwise turn.
    /// Zero means points are colinear.
    /// </summary>
    private static long Cross(Point o, Point a, Point b)
    {
        var (ox, oy) = (o.X, o.Y);
        var (ax, ay) = (a.X, a.Y);
        var (bx, by) = (b.X, b.Y);
        return (long)(ax - ox) * (by - oy) - (long)(ay - oy) * (bx - ox);
    }


    /// <summary>
    /// Constructs the convex hull using the Jarvis March algorithm.
    /// </summary>
    private static List<Point> BuildHull(List<Point> points)
    {
        int n = points.Count;
        if (n < 3) return [.. points];

        int startIndex = 0;
        for (int i = 1; i < n; i++)
        {
            if (points[i] < points[startIndex])
                startIndex = i;
        }

        var hull = new List<Point>();
        int currentIndex = startIndex;

        do
        {
            hull.Add(points[currentIndex]);
            int candidateIndex = (currentIndex + 1) % n;

            for (int i = 0; i < n; i++)
            {
                if (Cross(points[currentIndex], points[i], points[candidateIndex]) > 0)
                    candidateIndex = i;
            }

            currentIndex = candidateIndex;

        } while (currentIndex != startIndex);

        return hull;
    }

    public static int Main(string[] args)
    {
        if (args.Length != 2)
        {
            ShowUsage();
            return 1;
        }

        try
        {
            var xCoords = ParseIntegerList(args[0]);
            var yCoords = ParseIntegerList(args[1]);
            if (xCoords.Count != yCoords.Count)
            {
                ShowUsage();
                return 1;
            }

            if (xCoords.Count < 3)
            {
                ShowUsage();
                return 1;
            }

            var points = xCoords.Zip(yCoords, (x, y) => new Point(x, y)).ToList();

            BuildHull(points).ForEach(Console.WriteLine);

            return 0;
        }
        catch
        {
            ShowUsage();
            return 1;
        }
    }
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