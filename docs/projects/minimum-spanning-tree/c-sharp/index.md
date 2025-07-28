---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-29
featured-image: minimum-spanning-tree-in-every-language.jpg
last-modified: 2025-07-29
layout: default
tags:
- c-sharp
- minimum-spanning-tree
title: Minimum Spanning Tree in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/minimum-spanning-tree/c-sharp/how-to-implement-the-solution.md
- sources/programs/minimum-spanning-tree/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Minimum Spanning Tree](https://sampleprograms.io/projects/minimum-spanning-tree) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
﻿using System;
using System.Collections.Generic;
using System.Linq;

public static class Program
{
    private static void ShowUsage()
    {
        Console.Error.WriteLine("Usage: please provide a comma-separated list of integers");
        Environment.Exit(1);
    }

    private static List<int> ParseIntegerList(string input)
    {
        if (string.IsNullOrWhiteSpace(input))
            ShowUsage();

        var tokens = input
            .Split(',', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);

        if (tokens.Length < 4) // Minimum size for a 2x2 matrix
            ShowUsage();

        var numbers = new List<int>();
        foreach (var token in tokens)
        {
            if (!int.TryParse(token, out int value))
                ShowUsage();

            numbers.Add(value);
        }

        int dim = (int)Math.Sqrt(numbers.Count);
        if (dim * dim != numbers.Count)
            ShowUsage();

        return numbers;
    }

    private static int MinimumSpanningTreeWeight(List<int> adjacencyMatrix, int dimension)
    {
        var includedInMST = new bool[dimension];
        var minEdgeWeight = new int[dimension];

        for (int i = 0; i < dimension; i++)
        {
            minEdgeWeight[i] = int.MaxValue;
            includedInMST[i] = false;
        }

        minEdgeWeight[0] = 0;
        int totalWeight = 0;

        for (int count = 0; count < dimension; count++)
        {
            int currentMinWeight = int.MaxValue;
            int currentNode = -1;

            for (int i = 0; i < dimension; i++)
            {
                if (!includedInMST[i] && minEdgeWeight[i] < currentMinWeight)
                {
                    currentMinWeight = minEdgeWeight[i];
                    currentNode = i;
                }
            }

            if (currentNode == -1)
            {
                ShowUsage();
            }

            includedInMST[currentNode] = true;
            totalWeight += currentMinWeight;

            for (int adjacent = 0; adjacent < dimension; adjacent++)
            {
                int edgeWeight = adjacencyMatrix[currentNode * dimension + adjacent];
                if (!includedInMST[adjacent] && edgeWeight != 0 && edgeWeight < minEdgeWeight[adjacent])
                {
                    minEdgeWeight[adjacent] = edgeWeight;
                }
            }
        }

        return totalWeight;
    }

    public static int Main(string[] args)
    {
        if (args.Length != 1)
            ShowUsage();

        var inputList = ParseIntegerList(args[0]);

        var numbers = ParseIntegerList(args[0]);
        int dimension = (int)Math.Sqrt(numbers.Count);

        int mstWeight = MinimumSpanningTreeWeight(numbers, dimension);

        if (mstWeight == -1)
            ShowUsage();

        Console.WriteLine(mstWeight);

        return 0;
    }
}

```

{% endraw %}

Minimum Spanning Tree in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).