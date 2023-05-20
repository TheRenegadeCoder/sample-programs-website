---
title: Baklava in C#
layout: default
date: 2018-09-17
featured-image: baklava-in-every-language.jpg
last-modified: 2018-09-17

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;

class CSharp
{

    static void Main (string[] args)
    {

        for (SByte i = 0; i < 10; i++)
            Console.WriteLine (
                new string (' ', (10 - i)) + new string ('*', (i * 2 + 1))
            );

        for (SByte i = 10; -1 < i; i--)
            Console.WriteLine (
                new string (' ', (10 - i)) + new string ('*', (i * 2 + 1))
            );

    }

}
```

{% endraw %}

[Baklava](https://sampleprograms.io/projects/baklava) in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 06 2023 22:50:37. The solution was first committed on Sep 17 2018 16:48:59. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).