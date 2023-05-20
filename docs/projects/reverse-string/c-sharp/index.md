---
title: Reverse String in C#
layout: default
date: 2018-04-25
featured-image: reverse-string-in-every-language.jpg
last-modified: 2018-04-25

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;

namespace SamplePrograms
{
    public class ReverseString
    {
        public static string Reverse(string input)
        {
            var charArray = input.ToCharArray();
            Array.Reverse(charArray);
            return new string(charArray);
        }

        public static void Main(string[] args)
        {
            if (args.Length > 0)
            {
                System.Console.WriteLine(Reverse(args[0]));
            }
        }
    }
}
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- ildoc
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Jul 03 2018 11:06:29. The solution was first committed on Apr 25 2018 14:55:06. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).