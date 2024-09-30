---
authors:
- rzuckerm
date: 2024-02-11
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2024-02-11
layout: default
tags:
- beef
- longest-palindromic-substring
title: Longest Palindromic Substring in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/beef/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;

namespace LongestPalindromicSubstring;

class Program
{
    public static void Usage()
    {
        Console.WriteLine("Usage: please provide a string that contains at least one palindrome");
        Environment.Exit(0);
    }

    // Find longest palindromic string using matching array
    // Source: https://www.geeksforgeeks.org/longest-palindromic-substring-using-dynamic-programming/
    public static void LongestPalindromicSubstring(StringView str, String longest)
    {
        // Convert string to lowercase
        String strLower = scope .(str) .. ToLower();

        // Initialize character match matrix to indicate length 1 strings match
        int n = str.Length;
        bool [,] matches = scope .[n, n];
        for (int i < n)
        {
            matches[i, i] = true;
        }

        // Find all length 2 matches
        int start = 0;
        int maxLen = 1;
        for (int i < (n - 1))
        {
            if (strLower[i] == strLower[i + 1])
            {
                matches[i, i + 1] = true;
                start = i;
                maxLen = 2;
            }
        }

        // Find all length 3 or longer matches
        for (int len in 3...n)
        {
            // Loop through each starting character
            int j = len - 1;
            for (int i in 0...(n - len))
            {
                // If match for one character in from start and end characters
                // and start and end characters match, set match for start and
                // end characters, and update max length
                if (matches[i + 1, j - 1] && strLower[i] == strLower[j])
                {
                    matches[i, j] = true;
                    if (len > maxLen)
                    {
                        start = i;
                        maxLen = len;
                    }
                }

                j++;
            }
        }

        longest.Clear();
        longest.Append(str[start..<(start + maxLen)]);
    }

    public static int Main(String[] args)
    {
        if (args.Count < 1 || args[0].Length < 1)
        {
            Usage();
        }

        String result = scope .();
        LongestPalindromicSubstring(args[0], result);
        if (result.Length < 2)
        {
            Usage();
        }

        Console.WriteLine(result);

        return 0;
    }
}

```

{% endraw %}

Longest Palindromic Substring in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).