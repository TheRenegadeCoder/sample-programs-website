---
authors:
- rzuckerm
date: 2024-01-18
featured-image: quine-in-every-language.jpg
last-modified: 2024-01-18
layout: default
tags:
- beef
- quine
title: Quine in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quine/beef/how-to-implement-the-solution.md
- sources/programs/quine/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;
namespace Quine;
class Program
{
    public static int Main(String[] args)
    {
        String s = """
using System;
namespace Quine;
class Program
{{
    public static int Main(String[] args)
    {{
        String s = {1}{1}{1}
{0}
{1}{1}{1};
        Console.WriteLine(s, s, '"');
        return 0;
    }}
}}
""";
        Console.WriteLine(s, s, '"');
        return 0;
    }
}

```

{% endraw %}

Quine in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).