---
authors:
- Jeremy Griffith
- Jeremy Grifski
- rzuckerm
date: 2018-04-10
featured-image: hello-world-in-scala.jpg
last-modified: 2023-05-15
layout: default
tags:
- hello-world
- scala
title: Hello World in Scala
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/scala/how-to-implement-the-solution.md
- sources/programs/hello-world/scala/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Scala](https://sampleprograms.io/languages/scala) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scala
object HelloWorld extends App {
  println("Hello, World!")
}

```

{% endraw %}

Hello World in [Scala](https://sampleprograms.io/languages/scala) was written by:

- Jeremy Griffith

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Up first, we have the `class` definition much like Java. However, 
there are two interesting keywords here: `object` and `extends`.

In Java, we would typically define a class using the `class` keyword. 
In fact, we normally even do that in Scala, so what's with this 
`object` keyword? Well, as it turns out, object is used when we want 
to define a singleton.

In object-oriented languages, a singleton is an object which has a 
one and only one policy. In other words, only one instance of the 
object will ever exist. Personally, I've only ever used the singleton 
design pattern to track state in a video game. Beyond that, I would 
consider it an anti-pattern.

That said, singletons are a feature in Scala, and they're typically 
used to define static functions. In other words, singletons can be 
used to generate utility classes that don't need to be instantiated 
to access their functionality.

In addition, singletons in Scala are often used as companion objects, 
but I can't say I totally understand what that is. Let me know in the 
comments.

Anyway, in this case, our singleton also extends App. This allows us 
to bypass the creation of a main method. We could have just as easily 
implemented Hello World in Scala as follows:

```scala
object HelloWorld {
    def main(args: Array[String]): Unit = {
        println("Hello, World!");
    }
}
```

At this point, we have something reminiscent of Java. Of course, the syntax 
is a bit different, but it looks about the same if we squint hard enough.

Finally, the only thing we have left is the print statement which is pretty 
typical at this point. Not much of a surprise there!


## How to Run the Solution

If we want to try the code above, we can use an online Scala compiler. Just 
take the code above and drop it into the editor before hitting run.

Alternatively, we can always try to run the code locally. First, we'll need 
to follow the directions when downloading and installing Scala. Then, we'll 
probably want to get a copy of the solution.

With the heavy lifting out of the way, we should be able to simply run the 
following commands from the command line:

```shell
scalac hello-world.scala
scala hello-world
```

As we can see, Scala can be executed in pretty much the same way as Java. If 
all goes well, the last command should print the "Hello, World!" string.
