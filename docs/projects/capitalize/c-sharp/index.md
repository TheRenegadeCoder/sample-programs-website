---

title: Capitalize in C#
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Capitalize in C# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).