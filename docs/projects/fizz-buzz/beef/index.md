---
authors:
- rzuckerm
date: 2024-01-14
featured-image: fizz-buzz-in-every-language.png
last-modified: 2024-01-14
layout: default
tags:
- beef
- fizz-buzz
title: Fizz Buzz in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/beef/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;

namespace FizzBuzz;

class Program
{
    public static int Main(String[] args)
    {
        for (int i in 1...100)
        {
            String line = scope String();
            if ((i % 3) == 0)
            {
                line.Append("Fizz");
            }

            if ((i % 5) == 0)
            {
                line.Append("Buzz");
            }

            if (line.Length == 0)
            {
                i.ToString(line);
            }

            Console.WriteLine(line);
        }
        return 0;
    }
}

```

{% endraw %}

Fizz Buzz in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).