---
authors:
- maple-johnson
date: 2025-02-18
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2025-02-18
layout: default
tags:
- c-sharp
- palindromic-number
title: Palindromic Number in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/c-sharp/how-to-implement-the-solution.md
- sources/programs/palindromic-number/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
public class PalindromicNumber
{
    public static void Main(string[] args)
    {

        try
        {
            long verifyInput = long.Parse(args[0]);

            if (verifyInput >= 0)
            {
                Console.WriteLine(palindrome(args[0]));
            }
            else
            {
                Console.WriteLine("Usage: please input a non-negative integer");
            }

        }
        catch
        {
            Console.WriteLine("Usage: please input a non-negative integer");
        }

    }

    public static string palindrome(string numString)
    {
        char[] digits = numString.ToCharArray();

        int backCount = digits.Length - 1;

        for (int i = 0; i < digits.Length; i++)
        {
            if (digits[i] != digits[backCount])
            {
                return "false";
            }
            else
            {
                backCount--;
            }

        }

        return "true";

    }

}
```

{% endraw %}

Palindromic Number in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- maple-johnson

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).