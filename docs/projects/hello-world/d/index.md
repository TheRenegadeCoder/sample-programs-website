---
authors:
- Jeremy Grifski
- rzuckerm
- Trever Shick
date: 2018-05-06
featured-image: hello-world-in-d.jpg
last-modified: 2023-05-15
layout: default
tags:
- d
- hello-world
title: Hello World in D
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/d/how-to-implement-the-solution.md
- sources/programs/hello-world/d/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [D](https://sampleprograms.io/languages/d) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```d
import std.stdio;

void main()
{
    writeln("Hello, World!");
}

```

{% endraw %}

Hello World in [D](https://sampleprograms.io/languages/d) was written by:

- rzuckerm
- Trever Shick

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

At any rate, let's get to the implementation of Hello World in D.

At this point, you may be questioning whether or not D is even a new 
language. After all, this Hello World implementation looks a lot like 
C/C++.

Well, then it should come as no surprise the solution is pretty much 
the same. We have basically three main parts: the `import` statement, 
the `main` function, and the print function.

Just like C/C++, the first thing we do is import our standard IO 
library. In this case, D references `std.stdio` as opposed to `stdio.h`
in C.

Up next, we have our usual `main` function. At this point in the series, 
we're pretty use to this syntax.

Finally, we have our typical print function. In this case, we call 
`writeln` and pass a string to it.


## How to Run the Solution

If we wanted to run our code snippet from above, we can leverage an 
[online D compiler][1].

Alternatively, we can download our own D compiler from the official 
website. Then, we'll want to get a copy of Hello World in D. After 
that, we can simply run the following:

```shell
rdmd hello-world.d
```

And, that's it! The string "Hello, World!" should appear in the console.

[1]: https://run.dlang.io/
