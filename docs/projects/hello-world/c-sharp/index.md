---
authors:
- ildoc
- Jeremy Griffith
- Jeremy Grifski
- rzuckerm
date: 2018-03-21
featured-image: hello-world-in-c-sharp.jpg
last-modified: 2023-05-15
layout: default
tags:
- c-sharp
- hello-world
title: Hello World in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/c-sharp/how-to-implement-the-solution.md
- sources/programs/hello-world/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
namespace SamplePrograms
{
    public class HelloWorld
    {
        static void Main()
        {
            System.Console.WriteLine("Hello, World!");
        }
    }
}

```

{% endraw %}

Hello World in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- ildoc
- Jeremy Griffith
- Jeremy Grifski

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Now, we can implement Hello World in C# in a couple of ways. For simplicity,
I'll share the minimalist approach but be aware that there are more complete ways
to do this.

If you read the Hello World in Java tutorial, then this probably looks very
similar. In fact, C# shares a lot of the same look and feel as Java. With that
being the case, I'll only highlight the major pieces here.

Before we can print, we have to create a class. Inside our class, we declare
the `main` method. Inside our `main` method, we run our print command. The syntax
and core libraries are a little different, but it feels eerily similar to Java.


## How to Run the Solution

Perhaps the easiest way to run this solution would be to open up an [online C# compiler][1].
Just copy the code from above and drop it into the editor before
hitting run.

Alternatively, we can download Visual Studio or Mono to run C# locally. Of
course, we'll want a copy of the solution as well. Refer to the manual of the
various tools to run C#.

As far as I know, there aren't any easy ways to run C# code from the command
line, but I imagine it can be done.

[1]: https://www.programiz.com/csharp-programming/online-compiler/
