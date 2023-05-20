---
title: Hello World in Scheme
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-scheme.jpg
tags: [scheme, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Scheme](https://sampleprograms.io/languages/scheme) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scheme
(display "Hello, World!")
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Scheme](https://sampleprograms.io/languages/scheme) was written by:

- Jeremy Griffith

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

If you checked out the tutorial on Hello World in Lisp, then this should be easy. First things first, we have the *display* function. The *display* function works exactly as you would expect. It takes some input and displays it to the user.

As a result, it's natural to expect that the input in this case is Hello World. All we do is pass the Hello World string to display, and we're done.


## How to Run the Solution

As usual, we can give it a go with an [online Scheme interpreter][1]. Just drop the code above into the editor and hit run.

Alternatively, we can download [CHICKEN Scheme][2] and a copy of the solution. Assuming CHICKEN Scheme is on our path, we can run the following from a command line:

```bash
csi -s hello-world.scm
```
That will run the Scheme file as a script which will quickly print the "Hello, World!" string.

[1]: https://www.jdoodle.com/execute-scheme-online/
[2]: https://call-cc.org/
