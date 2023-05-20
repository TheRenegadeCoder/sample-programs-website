---
title: Hello World in R
layout: default
last-modified: 2020-10-15
featured-image: hello-world-in-r.jpg
tags: [r, hello-world]
authors:
  - alexandra_woerner

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [R](https://sampleprograms.io/languages/r) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```r
cat("Hello, World!")
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [R](https://sampleprograms.io/languages/r) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Fortunately, this task can be solved in a concise one-liner.

You can see the string "Hello, World!" as the argument of the function `cat`.
This function does all the work. If you are familiar with Bash, you may already
know the `cat` tool which prints the content of one or several files.

Analogously, you can pass one or several strings to the `cat` function which prints
the input to the standard output. The function allows an optional argument `sep`
that represents the separator to use when you pass multiple strings. As a
consequence, the following is an equivalent alternative to the solution above:

```r
cat("Hello", "World!", sep=", ")
```

In this call, "Hello" and "World!" are glued together by placing the specified
separator ", " between the two strings, resulting in the desired output
"Hello, World!".

Now, we know what we need to produce the output. The next section explains how
we can also see the output of our program.


## How to Run the Solution

In order to run the solution we need an [R compiler][3] first. Furthermore, we need
a copy of Hello World in [R][1]. From within the directory in which we saved the copy,
we run the following command on the command line:

```console
Rscript hello-world.R        # Linux/Unix
R.exe hello-world.R          # Windows
```

Alternatively, you can try an [online compiler][4] if you want to save the time
required for installing the R environment locally.

[3]: https://cran.r-project.org/
[4]: https://www.mycompiler.io/new/r
