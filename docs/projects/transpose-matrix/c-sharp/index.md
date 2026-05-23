---
authors:
- Ștefan-Iulian Alecu
date: 2025-07-29
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- transpose-matrix
title: Transpose Matrix in C#
title1: Transpose
title2: Matrix in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/c-sharp/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](/projects/transpose-matrix) in [C#](/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
﻿using System.Runtime.InteropServices;

if (args is not [var colsRaw, var rowsRaw, var matrixRaw]
    || !int.TryParse(colsRaw, out int cols)
    || !int.TryParse(rowsRaw, out int rows)
    || cols <= 0 || rows <= 0
    || !TryParseMatrix(matrixRaw.AsSpan(), cols, rows, out var matrix)
)
{
    return ExitWithUsage();
}

Console.WriteLine(string.Join(", ", Transpose(matrix, cols, rows)));
return 0;

static List<int> Transpose(List<int> m, int cols, int rows)
{
    var o = new List<int>(m.Count);
    for (int i = 0; i < m.Count; i++) o.Add(0);

    var src = CollectionsMarshal.AsSpan(m);
    var dst = CollectionsMarshal.AsSpan(o);

    for (int r = 0; r < rows; r++)
    for (int c = 0; c < cols; c++)
        dst[c * rows + r] = src[r * cols + c];

    return o;
}

static bool TryParseMatrix(ReadOnlySpan<char> view, int cols, int rows, out List<int> numbers)
{
    numbers = new(cols * rows);

    if (view.IsWhiteSpace())
        return false;

    int expected = cols * rows;
    int count = 0;

    while (!view.IsEmpty)
    {
        int i = view.IndexOf(',');
        var token = i >= 0 ? view[..i] : view;

        view = i >= 0 ? view[(i + 1)..] : [];

        if (!int.TryParse(token, out int v))
            return false;

        numbers.Add(v);

        if (++count > expected)
            return false;
    }

    return count == expected;
}

static int ExitWithUsage()
{
    Console.Error.WriteLine(
        """Usage: please enter the dimension of the matrix and the serialized matrix"""
    );
    return 1;
}

```

{% endraw %}

Transpose Matrix in [C#](/languages/c-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).