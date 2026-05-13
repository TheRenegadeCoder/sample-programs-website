---
authors:
- Ștefan-Iulian Alecu
date: 2025-07-29
featured-image: minimum-spanning-tree-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- minimum-spanning-tree
title: Minimum Spanning Tree in C#
title1: Minimum Spanning
title2: Tree in C#
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
﻿if (args is not [var input] || !TryParseMatrix(input.AsSpan(), out var matrix, out int n))
    return ExitWithUsage();

int weight = MinimumSpanningTreeWeight(matrix, n);
if (weight < 0)
    return ExitWithUsage();

Console.WriteLine(weight);
return 0;

static int MinimumSpanningTreeWeight(List<int> matrix, int n)
{
    var inMst = new bool[n];
    var minEdge = new int[n];

    Array.Fill(minEdge, int.MaxValue);

    minEdge[0] = 0;

    int total = 0;

    for (int added = 0; added < n; added++)
    {
        int bestWeight = int.MaxValue;
        int u = -1;

        for (int i = 0; i < n; i++)
        {
            if (!inMst[i] && minEdge[i] < bestWeight)
            {
                bestWeight = minEdge[i];
                u = i;
            }
        }

        if (u < 0)
            return -1;

        inMst[u] = true;
        total += bestWeight;

        int row = u * n;

        for (int v = 0; v < n; v++)
        {
            int w = matrix[row + v];

            if (w != 0 && !inMst[v] && w < minEdge[v])
                minEdge[v] = w;
        }
    }

    return total;
}

static bool TryParseMatrix(ReadOnlySpan<char> view, out List<int> numbers, out int dimension)
{
    numbers = null!;
    dimension = 0;

    if (view.IsWhiteSpace())
        return false;

    int expected = view.Count(',') + 1;
    if (expected < 4) return false;

    var list = new List<int>(expected);

    while (!view.IsEmpty)
    {
        int i = view.IndexOf(',');
        var token = i >= 0 ? view[..i] : view;

        view = i >= 0 ? view[(i + 1)..] : [];

        if (!int.TryParse(token, out int v))
            return false;

        list.Add(v);
    }

    int d = (int)Math.Sqrt(list.Count);
    if (d * d != list.Count)
        return false;

    numbers = list;
    dimension = d;
    return true;
}

static int ExitWithUsage()
{
    Console.Error.WriteLine("""Usage: please provide a comma-separated list of integers""");
    return 1;
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