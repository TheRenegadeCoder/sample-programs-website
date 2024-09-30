---
authors:
- Jeremy Grifski
- Renato Ramos Nascimento
date: 2019-10-11
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-26
layout: default
tags:
- c-sharp
- capitalize
title: Capitalize in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/c-sharp/how-to-implement-the-solution.md
- sources/programs/capitalize/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
using System.Linq;

namespace SamplePrograms
{
    class Program
    {
        static void Main(string[] args)
        {
            if (!args.Any() || args[0] == "")
            {
                Console.WriteLine("Usage: please provide a string");
                return;
            }
            string input = args[0];
            string output = input.First().ToString().ToUpper() + input.Substring(1);
            Console.WriteLine(output);
        }
    }
}

```

{% endraw %}

Capitalize in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Jeremy Grifski
- Renato Ramos Nascimento

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).