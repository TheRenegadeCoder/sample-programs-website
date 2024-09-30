---
authors:
- rzuckerm
date: 2024-01-18
featured-image: file-input-output-in-every-language.jpg
last-modified: 2024-01-18
layout: default
tags:
- beef
- file-input-output
title: File Input Output in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/beef/how-to-implement-the-solution.md
- sources/programs/file-input-output/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;
using System.IO;

namespace FileInputOutput;

class Program
{
    public static Result<void> WriteFile(StringView filename)
    {
        StreamWriter fs = scope .();
        Try!(fs.Create(filename));
        fs.WriteLine("Hello from Beef!");
        fs.WriteLine("This is line 1");
        fs.WriteLine("This is line 2");
        fs.WriteLine("Goodbye!");
        return .Ok;
    }

    public static Result<void> ReadFile(StringView filename)
    {
        StreamReader fs = scope .();
        Try!(fs.Open(filename));
        String line = scope .();
        while (fs.ReadLine(line) case .Ok)
        {
            Console.WriteLine(line);
            line.Clear();
        }

        return .Ok;
    }

    public static int Main(String[] args)
    {
        String filename = "output.txt";

        if (WriteFile(filename) case .Err)
        {
            Console.WriteLine($"Could not write {filename}");
        }

        if (ReadFile(filename) case .Err)
        {
            Console.WriteLine($"Could not read {filename}");
        }

        return 0;
    }
}

```

{% endraw %}

File Input Output in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).