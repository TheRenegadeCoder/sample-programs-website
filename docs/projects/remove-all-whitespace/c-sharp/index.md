---
authors:
- Jeremy Grifski
- Ștefan-Iulian Alecu
date: 2024-11-11
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- remove-all-whitespace
title: Remove All Whitespace in C#
title1: Remove All
title2: Whitespace in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/c-sharp/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [C#](https://sampleprograms.io/languages/c-sharp)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
if (args is not [var input] || string.IsNullOrEmpty(input))
    return ExitWithError();

RemoveWhitespace(input.AsSpan());
return 0;

static void RemoveWhitespace(ReadOnlySpan<char> input)
{
    char[] buffer = new char[input.Length];
    int j = 0;

    foreach (char c in input)
    {
        if (!char.IsWhiteSpace(c))
            buffer[j++] = c;
    }

    Console.WriteLine(new string(buffer, 0, j));
}

static int ExitWithError()
{
    Console.WriteLine("Usage: please provide a string");
    return 1;
}
```

{% endraw %}

Remove All Whitespace in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Jeremy Grifski
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).