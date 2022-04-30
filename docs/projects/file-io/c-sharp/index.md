---

title: File Io in C#
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the File Io in C# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```c#
using System;
using System.IO;

namespace SamplePrograms
{
    public class FileIO
    {
        public static void Write() =>
            File.WriteAllText("output.txt", "file contents");

        public static string Read() =>
            File.ReadAllText("output.txt");

        public static void Main(string[] args)
        {
            Write();
            Console.WriteLine(Read());
        }
    }
}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).