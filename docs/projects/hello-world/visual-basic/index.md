---
authors:
- AaronLenoir
- Jeremy Grifski
- rzuckerm
date: 2018-05-04
featured-image: hello-world-in-visual-basic.jpg
last-modified: 2023-05-15
layout: default
tags:
- hello-world
- visual-basic
title: Hello World in Visual Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/visual-basic/how-to-implement-the-solution.md
- sources/programs/hello-world/visual-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Visual Basic](https://sampleprograms.io/languages/visual-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```visual_basic
Public Module HelloWorld
  Public Sub Main()
    System.Console.WriteLine("Hello, World!")
  End Sub
End Module

```

{% endraw %}

Hello World in [Visual Basic](https://sampleprograms.io/languages/visual-basic) was written by:

- AaronLenoir
- Jeremy Grifski

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's dive right into Hello World in Visual Basic .NET.

As we can see, VB.NET is a structured language. In other words, there's a very 
strong focus on code blocks and control flow structures.

Our first code block is the module declaration. In this case, we've declared a 
public module called `HelloWorld`. If other libraries needed access to this module, 
they could simply import it by name.

Next, we have our typical `main` function declaration. Of course, in VB.NET, we 
call them subroutines rather than functions, as indicated by the `Sub` keyword.

Finally, we have our print line. Much like languages like Java, we have to string 
together a few references before we can actually write to the console. In other 
words, we have to call `WriteLine` after we get a reference to the standard output 
class from the `System` namespace.


## How to Run the Solution

With our solution implemented, we should probably give it a run. Perhaps the easiest 
way to run the solution is to copy it into an [online VB.NET compiler][1].

Alternatively, we can run the solution using Microsoft's very own Visual Studio. 
Of course, I'm not sure of it's support on platforms beyond Windows. Don't forget 
to grab a copy of the [Hello World in Visual Basic .NET][2] solution.

[1]: https://www.jdoodle.com/compile-vb-dot-net-online/
[2]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/v/visual-basic/hello-world.vb
