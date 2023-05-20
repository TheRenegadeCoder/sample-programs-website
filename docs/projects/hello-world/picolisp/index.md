---
title: Hello World in PicoLisp
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-picolisp.jpg
tags: [picolisp, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Picolisp](https://sampleprograms.io/languages/picolisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```picolisp
(prinl "Hello, World!")
(bye)
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Picolisp](https://sampleprograms.io/languages/picolisp) was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 15 2023 09:32:26. The solution was first committed on May 08 2018 10:27:41. As a result, documentation below may be outdated.

## How to Implement the Solution

Let's break down what's happening. Since PicoLisp is a dialect of
Lisp, we can expect a ton of parentheses. In fact, our solution requires a single
set of parentheses at a minimum.

Inside the parentheses, we have a function call. In this case, the print function
is named `prinl`, and the input is our "Hello, World!" string. When executed, our
string will print to the console. The `bye` function is required to exit the program.


## How to Run the Solution

If we want to run the solution, we can try an [online editor][1]. However, I ran into some 
problems with this particular editor.

Alternatively, if we have access to a Unix, Linux, or Mac machine, we can easily 
[download and install the latest version of PicoLisp][2]. That said, @cess11 has a great 
video proving that this solution works:

[![asciicast](https://asciinema.org/a/HdFjKizOUYKdcyFoG6h4RPhjn.svg)](https://asciinema.org/a/HdFjKizOUYKdcyFoG6h4RPhjn)

And, that's it! If implemented correctly, the solution should print "Hello, World!" to the console.

[1]: https://www.jdoodle.com/execute-picolisp-online/
[2]: https://software-lab.de/down.html
