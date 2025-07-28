---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-29
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2025-07-29
layout: default
tags:
- c-sharp
- transpose-matrix
title: Transpose Matrix in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/c-sharp/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

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
        Console.Error.WriteLine("Usage: please enter the dimension of the matrix and the serialized matrix");
        Environment.Exit(1);
    }

    private static List<int> ParseIntegerList(string input)
    {
        if (string.IsNullOrWhiteSpace(input))
            ShowUsage();

        var tokens = input
            .Split(',', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);

        var numbers = new List<int>();
        foreach (var token in tokens)
        {
            if (!int.TryParse(token, out int value))
                ShowUsage();

            numbers.Add(value);
        }

        return numbers;
    }

    static List<int> TransposeMatrix(int cols, int rows, List<int> input)
    {
        var result = new List<int>(new int[rows * cols]);

        for (int i = 0; i < rows; ++i)
        {
            for (int j = 0; j < cols; ++j)
            {
                int index = j * rows + i;
                result[index] = input[i * cols + j];
            }
        }

        return result;
    }

    static int Main(string[] args)
    {
        if (args.Length != 3)
            ShowUsage();

        if (!int.TryParse(args[0], out var cols))
            ShowUsage();

        if (!int.TryParse(args[1], out var rows))
            ShowUsage();

        var numbers = ParseIntegerList(args[2]);
        if (numbers.Count != cols * rows)
            ShowUsage();

        var transposed = TransposeMatrix(cols, rows, numbers);
        Console.WriteLine(string.Join(", ", transposed));
        return 0;
    }
}

```

{% endraw %}

Transpose Matrix in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).