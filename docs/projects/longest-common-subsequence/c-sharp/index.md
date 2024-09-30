---
authors:
- Parker Johansen
date: 2018-10-28
featured-image: longest-common-subsequence-in-every-language.jpg
last-modified: 2019-03-26
layout: default
tags:
- c-sharp
- longest-common-subsequence
title: Longest Common Subsequence in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-common-subsequence/c-sharp/how-to-implement-the-solution.md
- sources/programs/longest-common-subsequence/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Common Subsequence](https://sampleprograms.io/projects/longest-common-subsequence) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
using System.Collections.Generic;
using System.Linq;

namespace SamplePrograms
{
    public class LongestCommonSubsequence
    {
        private static IEnumerable<string> LCS(IEnumerable<string> list1, IEnumerable<string> list2)
        {
            if (list1.Count() == 0 || list2.Count() == 0)
                return new List<string>();

            if (list1.First().Equals(list2.First()))
                return LCS(list1.Skip(1), list2.Skip(1)).Concat(new List<string>() { list1.First() });

            return Longest(LCS(list1, list2.Skip(1)), LCS(list1.Skip(1), list2));
        }

        private static IEnumerable<string> Longest(params IEnumerable<string>[] lists) =>
            lists.OrderByDescending(l => l.Count()).First();

        public static void Main(string[] args)
        {
            try
            {
                var list1 = args[0].Split(',').Select(i => i.Trim());
                var list2 = args[1].Split(',').Select(i => i.Trim());
                var lcs = LCS(list1, list2).Reverse();
                Console.WriteLine(string.Join(", ", lcs));
            }
            catch
            {
                Console.WriteLine("Usage: please provide two lists in the format \"1, 2, 3, 4, 5\"");
                Environment.Exit(1);
            }
        }
    }
}
```

{% endraw %}

Longest Common Subsequence in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).