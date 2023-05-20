---
title: Even Odd in C#
layout: default
date: 2018-12-28
featured-image: even-odd-in-every-language.jpg
last-modified: 2018-12-28

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;

namespace SamplePrograms
{
    public class EvenOdd
    {
        public static void Main(string[] args)
        {
            try
            {
                int n = int.Parse(args[0]);
                var result = n % 2 == 0 ? "Even" : "Odd";
                Console.WriteLine(result);
            }
            catch
            {
                Console.WriteLine("Usage: please input a number");
                Environment.Exit(1);
            }
        }
    }
}
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).