---
authors:
- rzuckerm
date: 2024-01-14
featured-image: reverse-string-in-every-language.jpg
last-modified: 2024-01-14
layout: default
tags:
- beef
- reverse-string
title: Reverse String in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/beef/how-to-implement-the-solution.md
- sources/programs/reverse-string/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;

namespace ReverseString;

class Program
{
    public static void ReverseString(StringView str, ref String reversed)
    {
        reversed.Clear();
        reversed.Reserve(str.Length);
        for (char8 ch in str.Reversed)
        {
            reversed += ch;
        }
    }

    public static int Main(String[] args)
    {
        if (args.Count > 0)
        {
            String reversed = scope String();
            ReverseString(args[0], ref reversed);
            Console.WriteLine(reversed);
        }

        return 0;
    }
}


```

{% endraw %}

Reverse String in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).