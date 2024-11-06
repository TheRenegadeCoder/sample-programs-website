---
authors:
- Ben Mojo
date: 2024-11-06
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2024-11-06
layout: default
tags:
- c-sharp
- josephus-problem
title: Josephus Problem in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/c-sharp/how-to-implement-the-solution.md
- sources/programs/josephus-problem/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;

namespace JosephusProblem
{
    class Program
    {
        const string Usage = "Usage: please input the total number of people and number of people to skip.";

        static void Main(string[] args)
        {
            if (args.Length < 2)
            {
                Console.WriteLine(Usage);
                return;
            }

            if (!int.TryParse(args[0], out int n) || !int.TryParse(args[1], out int k) || n <= 0 || k <= 0)
            {
                Console.WriteLine(Usage);
                return;
            }

            int survivor = FindJosephusPosition(n, k);

            Console.WriteLine(survivor);
        }

        static int FindJosephusPosition(int n, int k)
        {
            int result = 0;

            for (int m = 2; m <= n; m++)
            {
                result = (result + k) % m;
            }

            return result + 1;
        }
    }
}

```

{% endraw %}

Josephus Problem in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Ben Mojo

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).