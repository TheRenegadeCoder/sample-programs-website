---
authors:
- rzuckerm
- Scott Little
date: 2020-10-04
featured-image: factorial-in-every-language.jpg
last-modified: 2023-05-13
layout: default
tags:
- d
- factorial
title: Factorial in D
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/d/how-to-implement-the-solution.md
- sources/programs/factorial/d/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [D](https://sampleprograms.io/languages/d) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```d
// Factorial program in D
import std.stdio: writeln;
import std.conv: to, ConvException;
import core.stdc.stdlib: exit;

void usage()
{
    writeln("Usage: please input a non-negative integer");
    exit(0);
}

int fac(int a)
{
    if (a <= 1)
    {
        return 1;
    }
    return a*fac(a-1);
}

int main(string[] args)
{
    if (args.length < 2)
    {
        usage();
    }

    int depth;
    try {
        depth = to!int(args[1]);
        if (depth < 0)
        {
            usage();
        }
    }
    catch(ConvException _)
    {
        usage();
    }

    int result = fac(depth);
    writeln(result);
    return 0;
}

```

{% endraw %}

Factorial in [D](https://sampleprograms.io/languages/d) was written by:

- rzuckerm
- Scott Little

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).