---
title: Hello World in Euphoria
layout: default
last-modified: 2023-02-16
featured-image: hello-world-in-euphoria.jpg
tags: [euphoria, hello-world]
authors:
  - rzuckerm

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e

puts(STDOUT, "Hello, World!\n")
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

The syntax of Euphoria is similar to C in some respects but without
braces and semicolons, and the `include` statement does not have
quotes or angle brackets around the file that is being included.

```euphoria
include std/io.e
```

The `std/io.e` include file contains the definitions for standard
I/O file numbers. `STDOUT`, as expected, has the value of `1`. While
it is not necessary to include this, it makes the code more readable
since the intent of `STDOUT` is more obvious than just a hard-coded
value of `1`.

```euphoria
puts(STDOUT, "Hello, World!\n")
```

The `puts` function is similar to the `fputs` function
in C, but the parameters are reversed. The first argument is the file
number. The second argument is the string to output. In C, the first
argument is the string to output, and the second argument is a
`FILE` pointer.


## How to Run the Solution

If you want to run this program, you'll first need to download a
copy of the 
[Euphoria interpreter](https://openeuphoria.org/wiki/view/DownloadEuphoria.wc),
and follow the installation instructions. From there, open a terminal, and
run this command:

```
eui hello_world.eu
```
