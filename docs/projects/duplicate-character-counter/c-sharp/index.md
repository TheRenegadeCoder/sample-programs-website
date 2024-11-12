---
authors:
- Huma Homidov
date: 2024-11-12
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2024-11-12
layout: default
tags:
- c-sharp
- duplicate-character-counter
title: Duplicate Character Counter in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/c-sharp/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
using System.Collections.Generic;

public class DuplicateCharacterCounter
{
    public static void Main(string[] args)
    {
        if (args.Length == 0 || string.IsNullOrEmpty(args[0]))
        {
            Console.WriteLine("Usage: please provide a string");
            return;
        }

        string input = args[0];

        Dictionary<char, int> countMap = new Dictionary<char, int>();

        foreach (char c in input)
        {
            if (countMap.ContainsKey(c))
                countMap[c]++;
            else
                countMap[c] = 1;
        }

        string result = "";

        foreach (char c in input)
        {
            if (countMap[c] > 1)
            {
                result += $"{c}: {countMap[c]}\n";
                countMap[c] = 0;
            }
        }

        Console.WriteLine(string.IsNullOrEmpty(result) ? "No duplicate characters" : result.Trim());
    }
}
```

{% endraw %}

Duplicate Character Counter in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Huma Homidov

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).