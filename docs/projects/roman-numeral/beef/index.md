---
authors:
- rzuckerm
date: 2024-01-22
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2024-01-22
layout: default
tags:
- beef
- roman-numeral
title: Roman Numeral in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/beef/how-to-implement-the-solution.md
- sources/programs/roman-numeral/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;

namespace RomanNumeral;

class Program
{
    public static void Usage()
    {
        Console.WriteLine("Usage: please provide a string of roman numerals");
        Environment.Exit(0);
    }

    public static void Error()
    {
        Console.WriteLine("Error: invalid string of roman numerals");
        Environment.Exit(0);
    }

    public static Result<int> RomanNumeral(StringView str)
    {
        int total = 0;
        int prevDigit = 0;
        for (char8 ch in str)
        {
            int digit = 0;
            switch (ch)
            {
                case 'I': digit = 1;
                case 'V': digit = 5;
                case 'X': digit = 10;
                case 'L': digit = 50;
                case 'C': digit = 100;
                case 'D': digit = 500;
                case 'M': digit = 1000;
                default: return .Err;
            }

            total += digit;

            // If there is a previous digit and digit is greater than previous digit,
            // subtract two times previous digit from total to compensate for addition of
            // previous digit
            if (prevDigit > 0 && digit > prevDigit)
            {
                total -= 2 * prevDigit;
                prevDigit = 0;
            }

            prevDigit = digit;
        }

        return .Ok(total);
    }

    public static int Main(String[] args)
    {
        if (args.Count < 1)
        {
            Usage();
        }

        switch (RomanNumeral(args[0]))
        {
            case .Ok(let result):
                Console.WriteLine(result);
            case .Err:
                Error();
        }

        return 0;
    }
}
```

{% endraw %}

Roman Numeral in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).