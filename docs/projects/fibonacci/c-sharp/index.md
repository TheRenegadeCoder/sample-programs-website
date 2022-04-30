---

title: Fibonacci in C#
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Fibonacci in C# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```c#
using System;

namespace SamplePrograms
{
    public class Fibonacci
    {
        public static void Main(string[] args)
        {
            try
            {
                int n = int.Parse(args[0]);
                int first = 0;
                int second = 1;
                int result = 0;
                for(int i = 1; i <= n; i++)
                {
                    result = first + second;
                    first = second;
                    second = result;
                    Console.WriteLine(i + ": " + first);
                }
            }
            catch(Exception)
            {
                Console.WriteLine("Usage: please input the count of fibonacci numbers to output");
                Environment.Exit(0);
            }
        }
    }
}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).