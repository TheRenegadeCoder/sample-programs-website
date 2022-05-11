---

title: Capitalize in C#
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Capitalize in C# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
using System.Linq;

namespace SamplePrograms
{
    class Program
    {
        static void Main(string[] args)
        {
            if (!args.Any() || args[0] == "")
            {
                Console.WriteLine("Usage: please provide a string");
                return;
            }
            string input = args[0];
            string output = input.First().ToString().ToUpper() + input.Substring(1);
            Console.WriteLine(output);
        }
    }
}
```

{% endraw %}

Capitalize in C# was written by:

- Jeremy Grifski
- Renato Ramos Nascimento

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 26 2019 21:08:00. The solution was first committed on Oct 11 2019 19:29:17. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).