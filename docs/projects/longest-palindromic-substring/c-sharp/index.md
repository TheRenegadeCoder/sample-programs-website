---
authors:
- Maxwell Maslov
date: 2024-11-08
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2024-11-08
layout: default
tags:
- c-sharp
- longest-palindromic-substring
title: Longest Palindromic Substring in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/c-sharp/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
using System.Text.RegularExpressions;

namespace SamplePrograms
{
    public class LongestPalindromicSubstring
    {
        public static void Main(string[] args)
        {
            string input = string.Join(" ", args);
            Console.WriteLine(LongestPalindrome(input));
        }

        public static string LongestPalindrome(string input)
        {
            if (string.IsNullOrEmpty(input) || !ContainsPalindrome(input))
            {
                return "Usage: please provide a string that contains at least one palindrome";
            }

            int start = 0;
            int end = 0;

            for (int i = 0; i < input.Length; i++)
            {
                int lengthOne = ExpandAroundCenter(input, i, i);
                int lengthTwo = ExpandAroundCenter(input, i, i + 1);
                int length = Math.Max(lengthOne, lengthTwo);

                if (length > end - start)
                {
                    start = i - (length - 1) / 2;
                    end = i + length / 2;
                }
            }
            return input.Substring(start, end - start + 1);
        }

        private static int ExpandAroundCenter(string input, int left, int right)
        {
            while (left >= 0 && right < input.Length && input[left] == input[right])
            {
                left--;
                right++;
            }
            return right - left - 1;
        }

        private static bool ContainsPalindrome(string input)
        {
            string[] words = input.Split(' ');
            foreach (string word in words)
            {
                if (word.Length > 1 && word == Reverse(word))
                {
                    return true;
                }
            }
            
            string cleanedInput = input.Replace(" ", "");
            return cleanedInput.Length > 1 && cleanedInput == Reverse(cleanedInput);
        }

        private static string Reverse(string input)
        {
            char[] charArray = input.ToCharArray();
            Array.Reverse(charArray);
            return new string(charArray);
        }
    }
}
```

{% endraw %}

Longest Palindromic Substring in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Maxwell Maslov

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).