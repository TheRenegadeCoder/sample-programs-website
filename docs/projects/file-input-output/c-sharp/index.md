---
title: File Input Output in C#
layout: default
date: 2018-12-28
featured-image: file-input-output-in-every-language.jpg
last-modified: 2018-12-28

---

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

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

[File Input Output](https://sampleprograms.io/projects/file-input-output) in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).