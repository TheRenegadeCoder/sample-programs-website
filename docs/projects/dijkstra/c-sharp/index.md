---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-29
featured-image: dijkstra-in-every-language.jpg
last-modified: 2025-07-29
layout: default
tags:
- c-sharp
- dijkstra
title: Dijkstra in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/dijkstra/c-sharp/how-to-implement-the-solution.md
- sources/programs/dijkstra/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Dijkstra](https://sampleprograms.io/projects/dijkstra) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
﻿using System;
using System.Collections.Generic;
using System.Linq;

public static class Program
{
    private const int INF = 0x3F3F3F3F;

    private static void ShowUsage()
    {
        Console.Error.WriteLine("Usage: please provide three inputs: a serialized matrix, a source node and a destination node");
        Environment.Exit(1);
    }

    private static List<int> ParseIntegerList(string input)
    {
        if (string.IsNullOrWhiteSpace(input))
            ShowUsage();

        var list = input
            .Split(',', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(s =>
            {
                if (!int.TryParse(s, out var val) || val < 0)
                    ShowUsage();
                return val;
            })
            .ToList();

        if (list.Count == 0)
            ShowUsage();

        return list;
    }

    private static int GetMatrixDimension(List<int> matrix)
    {
        var length = matrix.Count;
        var dimension = (int)Math.Sqrt(length);
        return (dimension * dimension == length && dimension > 0) ? dimension : -1;
    }

    private static int Dijkstra(List<int> matrix, int dimension, int source, int destination)
    {
        var dist = Enumerable.Repeat(INF, dimension).ToArray();
        var visited = new bool[dimension];

        dist[source] = 0;

        for (int _ = 0; _ < dimension; _++)
        {
            int minDist = INF;
            int minIndex = -1;

            for (int j = 0; j < dimension; j++)
            {
                if (!visited[j] && dist[j] < minDist)
                {
                    minDist = dist[j];
                    minIndex = j;
                }
            }

            if (minIndex == -1)
                break;

            if (minIndex == destination)
                return dist[minIndex];

            visited[minIndex] = true;

            for (int j = 0; j < dimension; j++)
            {
                int weight = matrix[minIndex * dimension + j];
                if (!visited[j] && weight > 0 && dist[minIndex] + weight < dist[j])
                {
                    dist[j] = dist[minIndex] + weight;
                }
            }
        }

        return dist[destination] == INF ? -1 : dist[destination];
    }

    public static int Main(string[] args)
    {
        if (args.Length != 3)
        {
            ShowUsage();
        }

        var matrixStr = args[0].Trim();
        var sourceStr = args[1].Trim();
        var destinationStr = args[2].Trim();

        if (string.IsNullOrEmpty(matrixStr) || string.IsNullOrEmpty(sourceStr) || string.IsNullOrEmpty(destinationStr))
            ShowUsage();

        var matrix = ParseIntegerList(matrixStr);
        int dimension = GetMatrixDimension(matrix);


        bool sourceParsed = int.TryParse(sourceStr, out int source);
        bool destinationParsed = int.TryParse(destinationStr, out int destination);

        if (dimension == -1 || !sourceParsed || !destinationParsed ||
            source < 0 || source >= dimension ||
            destination < 0 || destination >= dimension)
        {
            ShowUsage();
        }

        int shortestDistance = Dijkstra(matrix, dimension, source, destination);

        if (shortestDistance == -1)
            ShowUsage();

        Console.WriteLine(shortestDistance);
        return 0;
    }
}

```

{% endraw %}

Dijkstra in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).