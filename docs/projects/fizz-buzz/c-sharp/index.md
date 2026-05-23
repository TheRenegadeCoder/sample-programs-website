---
authors:
- Jeremy Grifski
- Ștefan-Iulian Alecu
date: 2018-08-14
featured-image: fizz-buzz-in-every-language.png
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- fizz-buzz
title: Fizz Buzz in C#
title1: Fizz Buzz
title2: in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/c-sharp/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](/projects/fizz-buzz) in [C#](/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
for (int i = 1; i <= 100; i++)
{
    string s = "";

    if (i % 3 == 0) s += "Fizz";
    if (i % 5 == 0) s += "Buzz";

    Console.WriteLine(s.Length > 0 ? s : i);
}
```

{% endraw %}

Fizz Buzz in [C#](/languages/c-sharp) was written by:

- Jeremy Grifski
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).