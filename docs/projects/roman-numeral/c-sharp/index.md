---
title: Roman Numeral in C#
layout: default
date: 2018-10-21
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2018-10-21

---

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
using System.Collections.Generic;

namespace SamplePrograms
{
    public class RomanNumeral
    {
        private static readonly Dictionary<char, int> RomanDecMapping = new Dictionary<char, int>()
        {
            ['M'] = 1000,
            ['D'] = 500,
            ['C'] = 100,
            ['L'] = 50,
            ['X'] = 10,
            ['V'] = 5,
            ['I'] = 1,
        };

        private static int RomanToDecimal(string roman, int total=0)
        {
            if (roman.Length < 1)
                return total;
            var romanArray = roman.ToCharArray();
            if (romanArray.Length == 1)
                return total + RomanDecMapping[romanArray[0]];

            var romanVal = RomanDecMapping[romanArray[0]];
            var nextRomanVal = RomanDecMapping[romanArray[1]];
            if (romanVal < nextRomanVal)
                return RomanToDecimal(roman.Substring(1), total - romanVal);

            return RomanToDecimal(roman.Substring(1), total + romanVal);
        }

        public static void Main(string[] args)
        {
            if (args.Length < 1)
            {
                Console.WriteLine("Usage: please provide a string of roman numerals");
                Environment.Exit(1);
            }
            try
            {
                Console.WriteLine(RomanToDecimal(args[0].ToUpper()));
            }
            catch (KeyNotFoundException)
            {
                Console.WriteLine("Error: invalid string of roman numerals");
                Environment.Exit(1);
            }
        }
    }
}
```

{% endraw %}

[Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 01 2019 04:00:30. The solution was first committed on Oct 21 2018 15:22:45. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).