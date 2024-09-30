---
authors:
- Marius
- Parker Johansen
date: 2018-10-02
featured-image: fibonacci-in-every-language.jpg
last-modified: 2019-04-07
layout: default
tags:
- c-sharp
- fibonacci
title: Fibonacci in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/c-sharp/how-to-implement-the-solution.md
- sources/programs/fibonacci/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;

namespace SamplePrograms
{
    public class Fibonacci
    {
        public static void Main(string[] args)
        {
            try
            {
                int n = int.Parse(args[0]);
                int first = 0;
                int second = 1;
                int result = 0;
                for(int i = 1; i <= n; i++)
                {
                    result = first + second;
                    first = second;
                    second = result;
                    Console.WriteLine(i + ": " + first);
                }
            }
            catch(Exception)
            {
                Console.WriteLine("Usage: please input the count of fibonacci numbers to output");
                Environment.Exit(0);
            }
        }
    }
}

```

{% endraw %}

Fibonacci in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Marius
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).