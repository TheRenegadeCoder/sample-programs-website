---
title: Hello World in C#
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-c-sharp.jpg
tags: [c-sharp, hello-world]
authors:
  - the_renegade_coder

---

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

[Hello World](https://sampleprograms.io/projects/hello-world) in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- ildoc
- Jeremy Griffith
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Jul 24 2018 10:04:46. The solution was first committed on Mar 21 2018 00:11:57. As a result, documentation below may be outdated.

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
