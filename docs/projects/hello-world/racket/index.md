---
authors:
- Jeremy Griffith
- Jeremy Grifski
- rzuckerm
date: 2018-04-08
featured-image: hello-world-in-racket.jpg
last-modified: 2023-05-15
layout: default
tags:
- hello-world
- racket
title: Hello World in Racket
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/racket/how-to-implement-the-solution.md
- sources/programs/hello-world/racket/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Racket](https://sampleprograms.io/languages/racket) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```racket
#lang racket/base
"Hello, World!"

```

{% endraw %}

Hello World in [Racket](https://sampleprograms.io/languages/racket) was written by:

- Jeremy Griffith

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's go ahead and dig into our implementation of Hello World in Racket.

Up first, we have this peculiar line that looks kind of like a comment in Python
or an import in C. As it turns out, the `lang` line specifies the language used by
the interpreter. In fact, I already mentioned that there's a module which
provides syntax for static typing in Racket.

In this case, the language we have chosen is `racket/base`. This only provides us
the core Racket functionality. As an alternative, we could have easily specified
racket alone.

Finally, we have our print line. To be honest, we could have used the print
functionality:

```racket
#lang racket/base
(print "Hello, World!)
```

However, I wanted to show that you can implement Hello World without the mess of
parentheses. That's because Racket automatically prints constants. If we had a
slightly more complicated expression:

```racket
#lang racket
+ 2 2
```

We would see the three constants returned to us in their stack order:

```racket
#<procedure:+>
2
2
```

We would need parentheses to actually evaluate this expression.


## How to Run the Solution

At any rate, I think we're done here. If we want to try to run the solution, we
can plug some of this code into an [online Racket interpreter][1].

Alternatively, we can [download the latest version of Racket][2] and [get a copy of
the solution][3]. Assuming Racket is now in the path, we can just run the following
to execute Hello World in Racket:

```shell
racket hello-world.rkt
```

And, that's it. If successful, the "Hello, World!" string should print to the console.

[1]: https://onecompiler.com/racket/
[2]: https://download.racket-lang.org/
[3]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/r/racket/hello-world.rkt
