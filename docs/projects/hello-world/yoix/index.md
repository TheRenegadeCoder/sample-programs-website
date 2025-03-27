---
authors:
- rzuckerm
date: 2023-06-19
featured-image: hello-world-in-yoix.jpg
last-modified: 2023-06-20
layout: default
tags:
- hello-world
- yoix
title: Hello World in Yoix
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/yoix/how-to-implement-the-solution.md
- sources/programs/hello-world/yoix/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Yoix](https://sampleprograms.io/languages/yoix) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```yoix
import yoix.stdio.printf;

printf("Hello, World!\n");

```

{% endraw %}

Hello World in [Yoix](https://sampleprograms.io/languages/yoix) was written by:

- rzuckerm

This article was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Yoix requires you to import every system function that you use. All the
`import` statements start with `yoix`, followed by the module where the
function is located, followed by the function name. Since `printf` is in
the `stdio` module, the `import` statement is `yoix.stdio.printf`.
The `printf` statement is same as Java, which is not surprising since
[the Yoix interpreter runs in Java][1].

[1]: https://en.wikipedia.org/wiki/Yoix


## How to Run the Solution

You can [download a copy of Yoix JAR file][2] to your local machine, grab a copy of
[Hello World in Yoix][3], and then run this:

```
java -jar yoix.jar hello_world.yx
```

[2]: https://raw.githubusercontent.com/att/yoix/master/yoix.jar
[3]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/y/yoix/hello_world.yx
