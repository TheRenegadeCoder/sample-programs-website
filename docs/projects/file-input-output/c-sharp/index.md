---
authors:
- Parker Johansen
- Ștefan-Iulian Alecu
date: 2018-12-28
featured-image: file-input-output-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- file-input-output
title: File Input Output in C#
title1: File Input
title2: Output in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/c-sharp/how-to-implement-the-solution.md
- sources/programs/file-input-output/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](/projects/file-input-output) in [C#](/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System.IO;

const string Path = "output.txt";
const string Content = """
line 1
line 2
line 3
""";

try
{
    File.WriteAllText(Path, Content);
    Console.WriteLine(File.ReadAllText(Path));
}
catch (IOException ex)
{
    Console.WriteLine($"IO error: {ex.Message}");
}
```

{% endraw %}

File Input Output in [C#](/languages/c-sharp) was written by:

- Parker Johansen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).