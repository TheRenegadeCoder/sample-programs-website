---
authors:
- Parker Johansen
- Ștefan-Iulian Alecu
date: 2018-12-30
featured-image: rot13-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- rot13
title: Rot13 in C#
title1: Rot13
title2: in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/c-sharp/how-to-implement-the-solution.md
- sources/programs/rot13/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [C#](https://sampleprograms.io/languages/c-sharp)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
if (args is not [var input] || string.IsNullOrEmpty(input))
    return ExitWithUsage();

Console.WriteLine(Rot13(input.AsSpan()));
return 0;

static string Rot13(ReadOnlySpan<char> input)
{
    char[] result = new char[input.Length];

    for (int i = 0; i < input.Length; i++)
    {
        char c = input[i];
        result[i] = c switch
        {
            >= 'a' and <= 'z' => (char)('a' + (c - 'a' + 13) % 26),
            >= 'A' and <= 'Z' => (char)('A' + (c - 'A' + 13) % 26),
            _ => c,
        };
    }

    return new string(result);
}

static int ExitWithUsage()
{
    Console.WriteLine("Usage: please provide a string to encrypt");
    return 1;
}

```

{% endraw %}

Rot13 in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).