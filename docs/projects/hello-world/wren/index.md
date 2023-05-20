---
title: Hello World in Wren
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-wren.jpg
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

Personally, I'm getting hints of Java and
Python here just in terms of syntax.

At any rate, let's break it down. Obviously, we only have
one line, but it's at least a little more interesting than
most scripting languages.

For starters, we have the built-in `System` class. This class
comes with the core module along with a few other goodies like
`String`, `Sequence`, `Fiber`, and `Bool`.

Now, one of the functions of `System` is `print`. Obviously, `print`
writes text to standard output. But, I find Wren's `print`
functionality particularly interesting because it's similar to
Java. In fact, it accepts any object as input. If the input is
not a `String`, `print` will convert it to a `String` using the
`toString` functionality, a method available to all objects.

So, basically we call the static method print of the `System` class
which prints the input to the user. How cool is that?


## How to Run the Solution

You can [download a copy of Wren][1] to your local machine, grab a copy of
[Hello World in Wren][2], and then run this:

```
wren_cli hello-world.wren
```

Alternatively, you can use an [online Wren interpreter][3].

[1]: https://github.com/wren-lang/wren-cli/releases
[2]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/w/wren/hello-world.wren
[3]: https://wren.io/try/
