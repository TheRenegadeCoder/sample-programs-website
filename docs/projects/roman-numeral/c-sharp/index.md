---
authors:
- Parker Johansen
- Ștefan-Iulian Alecu
date: 2018-10-21
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- roman-numeral
title: Roman Numeral in C#
title1: Roman Numeral
title2: in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/c-sharp/how-to-implement-the-solution.md
- sources/programs/roman-numeral/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](/projects/roman-numeral) in [C#](/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
if (args is not [var input])
    return ExitWith("Usage: please provide a string of roman numerals");

if (!TryRomanToInt(input.AsSpan().Trim(), out int value))
    return ExitWith("Error: invalid string of roman numerals");

Console.WriteLine(value);
return 0;

static bool TryRomanToInt(ReadOnlySpan<char> roman, out int result)
{
    result = 0;
    if (roman.Length == 0)
        return true;

    int prev = 0;

    for (int i = roman.Length - 1; i >= 0; i--)
    {
        if (!TryGetValue(roman[i], out int current))
            return false;

        if (current < prev)
            result -= current;
        else
            result += current;

        prev = current;
    }

    return true;
}

static bool TryGetValue(char c, out int value)
{
    value = char.ToUpper(c) switch
    {
        'I' => 1,
        'V' => 5,
        'X' => 10,
        'L' => 50,
        'C' => 100,
        'D' => 500,
        'M' => 1000,
        _ => 0
    };

    return value != 0;
}

static int ExitWith(string message)
{
    Console.WriteLine(message);
    return 1;
}
```

{% endraw %}

Roman Numeral in [C#](/languages/c-sharp) was written by:

- Parker Johansen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).