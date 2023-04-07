---
title: Hello World in Wren
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-wren-featured-image.JPEG
tags: [wren, hello-world]
authors:
  - the_renegade_coder
---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Wren](https://sampleprograms.io/languages/wren) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```wren
System.print("Hello, World!")
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Wren](https://sampleprograms.io/languages/wren) was written by:

- Jeremy Griffith

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

At any rate, let's get right to our implementation of Hello 
World in Wren:

```wren
System.print("Hello, World!")
```

And, that's it! Personally, I'm getting hints of Java and 
Python here just in terms of syntax.

At any rate, let's break it down. Obviously, we only have 
one line, but it's at least a little more interesting than 
most scripting languages.

For starters, we have the built-in System class. This class 
comes with the core module along with a few other goodies like 
String, Sequence, Fiber, and Bool.

Now, one of the functions of System is print. Obviously, print 
writes text to standard output. But, I find Wren's print 
functionality particularly interesting because it's similar to 
Java. In fact, it accepts any object as input. If the input is 
not a String, print will convert it to a String using the 
toString functionality, a method available to all objects.

So, basically we call the static method print of the System class 
which prints the input to the user. How cool is that?


## How to Run the Solution

Normally, at this point, I would share an example of how to run 
the solution on your machine. Unfortunately, Wren is rather new 
and a little clunky to get running. That said, I won't leave you 
hanging, There are some directions for Mac and Linux users on the 
Wren website.

Alternatively, you can use the online Wren editor. Just copy the 
code from above into the editor and hit run.
