---
authors:
- Jeremy Grifski
date: 2024-11-11
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2024-11-11
layout: default
tags:
- c-sharp
- remove-all-whitespace
title: Remove All Whitespace in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/c-sharp/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
using System.Linq;

class CSharp
{

    public static void ExitWithError()
    {
        Console.WriteLine("Usage: please provide a string");
        Environment.Exit(1);
    }

    public static void RemoveAllWhitespace(string str) {
        Console.WriteLine(
            new string(
                str
                .Where(c => !Char.IsWhiteSpace(c))
                .ToArray()
            )
        );
    }

    static void Main (string[] args)
    {
        if (!args.Any() || args[0] == "") {
            ExitWithError();
        }
        RemoveAllWhitespace(args[0]);
    }

}

```

{% endraw %}

Remove All Whitespace in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).