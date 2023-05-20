---
title: Hello World in Lisp
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-lisp.jpg
tags: [lisp, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Lisp](https://sampleprograms.io/languages/lisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lisp
(format t "Hello, World!")
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Lisp](https://sampleprograms.io/languages/lisp) was written by:

- Jeremy Griffith

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Unfortunately, Lisp has many flavors which means the following implementation 
of Hello World will likely only be applicable to handful of those flavors:

That said, I'm happy to dig into this implementation of Hello World in Lisp.

First things first, we have the `format` keyword. In Common Lisp, `forma`t is 
basically the equivalent to `printf` in C. It basically takes some string and 
outputs it to some destination.

That brings us to this mysterious letter `t`. According to gigamonkeys, `t` is 
actually the destination of the output. More specifically, `t` indicates standard 
output. Another option is `NIL` which causes the string to be returned.

Finally, we have our Hello World string. This is obviously what gets printed 
to standard output.


## How to Run the Solution

If we want to try it ourselves, we can copy the code above into an
[online Common Lisp compiler][1]. The one I linked is in CLISP, but it gets the job done.

Alternatively, as mentioned before, we can download a copy of
[Steel Bank Common Lisp][2] as well as a [copy of the solution][3].
Assuming SBCL is in the path, we can run a lisp file like a script as follows:

```console
sbcl --script hello-world.lsp
```

And, that should produce the "Hello, World!" string on the command line.

[1]: https://ideone.com/l/common-lisp-clisp
[2]: https://www.sbcl.org/platform-table.html
[3]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/l/lisp/hello-world.lsp
