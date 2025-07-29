---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-29
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2025-07-29
layout: default
tags:
- base64-encode-decode
- c-sharp
title: Base64 Encode Decode in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/c-sharp/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
﻿using System.Text;

public class Base64EncodeDecode
{
    public static void Usage()
    {
        Console.WriteLine("Usage: please provide a mode and a string to encode/decode");
        Environment.Exit(1);
    }


    private static bool IsValidBase64(string input)
    {
        if (string.IsNullOrWhiteSpace(input) || input.Length % 4 != 0)
            return false;

        foreach (char c in input)
        {
            if (!"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".Contains(c))
                return false;
        }

        int padCount = input.EndsWith("==") ? 2 :
                       input.EndsWith('=') ? 1 : 0;

        int firstPadIndex = input.IndexOf('=');
        return firstPadIndex == -1 || firstPadIndex >= input.Length - padCount;
    }

    public static int Main(string[] args)
    {
        if (args.Length != 2)
        {
            Usage();
            return 1;
        }

        string mode = args[0].ToLowerInvariant();
        string value = args[1];

        if (string.IsNullOrWhiteSpace(mode) || string.IsNullOrWhiteSpace(value))
        {
            Usage();
            return 1;
        }

        try
        {
            string result = mode switch
            {
                "encode" => Convert.ToBase64String(Encoding.UTF8.GetBytes(value)),
                "decode" => IsValidBase64(value)
                            ? Encoding.UTF8.GetString(Convert.FromBase64String(value))
                            : throw new ArgumentException("Input is not valid Base64."),
                _ => throw new ArgumentException("Unknown mode. Use 'encode' or 'decode'.")
            };

            Console.WriteLine(result);
            return 0;
        }
        catch
        {
            Usage();
            return 1;
        }
    }
}

```

{% endraw %}

Base64 Encode Decode in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).