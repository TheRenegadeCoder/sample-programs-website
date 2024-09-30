---
authors:
- Parker Johansen
date: 2018-12-30
featured-image: rot13-in-every-language.jpg
last-modified: 2019-04-06
layout: default
tags:
- c-sharp
- rot13
title: Rot13 in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/c-sharp/how-to-implement-the-solution.md
- sources/programs/rot13/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
using System.Collections.Generic;
using System.Linq;

namespace SamplePrograms
{
    public class Rot13
    {
        static List<char> Lowers = "abcdefghijklmnopqrstuvwxyz".ToCharArray().ToList();
        static List<char> Uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".ToCharArray().ToList();

        public static string Encrypt(string str) =>
            string.Join("", str.ToCharArray().Select(c => Encrypt(c)));

        public static Char Encrypt(char c)
        {
            List<char> ltrs;
            if (char.IsUpper(c))
                ltrs = Uppers;
            else if (char.IsLower(c))
                ltrs = Lowers;
            else
                return c;

            var newIndex = (ltrs.IndexOf(c) + 13) % 26;
            return ltrs[newIndex];

        }

        public static void ExitWithError()
        {
            Console.WriteLine("Usage: please provide a string to encrypt");
            Environment.Exit(1);
        }

        public static void Main(string[] args)
        {
            try
            {
                var str = args[0];
                if (String.IsNullOrEmpty(str))
                    ExitWithError();
                var result = Encrypt(str);
                Console.WriteLine(result);
            }
            catch
            {
                ExitWithError();
            }
        }
    }
}

```

{% endraw %}

Rot13 in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).