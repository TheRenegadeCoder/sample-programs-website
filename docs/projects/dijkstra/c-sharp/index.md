---
authors:
- Ștefan-Iulian Alecu
date: 2025-07-29
featured-image: dijkstra-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- dijkstra
title: Dijkstra in C#
title1: Dijkstra
title2: in C#
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
﻿if (
    args is not [var matrixRaw, var sourceRaw, var destRaw]
    || !int.TryParse(sourceRaw, out int source)
    || !int.TryParse(destRaw, out int dest)
    || !TryParseList(matrixRaw.AsSpan(), out var matrix)
)
    return Usage();

int n = (int)Math.Sqrt(matrix.Count);
if (n * n != matrix.Count || (uint)source >= n || (uint)dest >= n)
    return Usage();

var graph = new List<(int, uint)>[n];
for (int i = 0; i < n; i++)
    graph[i] = [];

for (int u = 0, k = 0; u < n; u++)
    for (int v = 0; v < n; v++, k++)
        if (matrix[k] != 0)
            graph[u].Add((v, (uint)matrix[k]));

uint result = Dijkstra(graph, source, dest);
if (result == uint.MaxValue)
    return Usage();

Console.WriteLine(result);
return 0;

static uint Dijkstra(List<(int to, uint w)>[] graph, int source, int destination)
{
    var dist = new uint[graph.Length];
    Array.Fill(dist, uint.MaxValue);

    var pq = new PriorityQueue<int, uint>();
    pq.Enqueue(source, dist[source] = 0);

    while (pq.TryDequeue(out int u, out uint d))
    {
        if (d != dist[u])
            continue;
        if (u == destination)
            return d;

        foreach (var (v, w) in graph[u])
        {
            uint newDist = d + w;
            if (newDist < dist[v])
                pq.Enqueue(v, dist[v] = newDist);
        }
    }

    return uint.MaxValue;
}

static bool TryParseList(ReadOnlySpan<char> span, out List<int> numbers)
{
    numbers = new(span.Count(',') + 1);

    while (!span.IsEmpty)
    {
        int comma = span.IndexOf(',');
        var token = comma >= 0 ? span[..comma] : span;

        span = comma >= 0 ? span[(comma + 1)..] : [];

        if (!int.TryParse(token, out int n) || n < 0)
            return false;

        numbers.Add(n);
    }

    return true;
}

static int Usage()
{
    Console.Error.WriteLine(
        "Usage: please provide three inputs: a serialized matrix, a source node and a destination node"
    );
    return 1;
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