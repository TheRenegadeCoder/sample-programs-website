---
authors:
- f3liz
date: 2024-11-08
featured-image: longest-word-in-every-language.jpg
last-modified: 2024-11-08
layout: default
tags:
- c-sharp
- longest-word
title: Longest Word in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/c-sharp/how-to-implement-the-solution.md
- sources/programs/longest-word/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
using System.Linq;

public class LongestWord
{
    public static void Main(string[] args)
    {
        // check for empty string or empty input
        if (args.Length == 0 || args[0] == "") {
            Console.WriteLine("Usage: please provide a string");
        } else {
            // stores string from args
            string sentence = args[0];

            // split string by whitespace (these four special characters), removes empty entries
            string[] words = sentence.Split(new[] {' ', '\t', '\n', '\r'}, StringSplitOptions.RemoveEmptyEntries);

            // sort array by length in descending order so longest string is first and returns is to array
            words = words.OrderByDescending(word => word.Length).ToArray();

            // log the length of longest word
            Console.WriteLine(words[0].Length);
        }
    }


}
```

{% endraw %}

Longest Word in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- f3liz

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).