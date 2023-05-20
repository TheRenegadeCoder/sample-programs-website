---
title: Hello World in Haskell
layout: default
last-modified: 2021-02-22
featured-image: hello-world-in-haskell.jpg
tags: [haskell, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Haskell](https://sampleprograms.io/languages/haskell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haskell
module Main where

main = putStrLn "Hello, World!"
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Haskell](https://sampleprograms.io/languages/haskell) was written by:

- Jeremy Griffith

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

As usual, let's get right to our implementation of Hello World in Haskell.

First thing we will probably notice is that Haskell syntax is very different
from Lisp and Scheme. Despite all three of those languages being functional,
Haskell seems to have ditched the parentheses. In fact, even function calls
lack parentheses in Haskell. That's a new one for me.

After the syntax, the next thing we should probably look at is that first line.
As usual, we have a module declaration which basically declares this file as
the main file. In other words, execution begins with this module. We saw
something similar in our Hello World in Go article.

Finally, we have our `main` function. For someone who has never played with anything
like Haskell, this syntax is a bit bizarre. In fact, the main function doesn't look
like a function definition at all. At least, it doesn't look like what we've come to
expect from this series.

That said, the `main` function does make a lot of sense if we think about it in terms
of mathematics. After all, math functions follow the exact same form: `f(x) = x`.

At any rate, let's get back to the code. In this final line, we have the `main` keyword
which indicates the entry point to the program. From there, we compute the expression
on the other side of the equals sign. In this case, we have a print function (`putStrLn`) and our
string, and that's it. Pretty simple!


## How to Run the Solution

If we want to run the snippets above, we can use an [online Haskell compiler][1]. All we 
have to do is drop the code into the editor and hit run.

Of course, we can also run the code locally if we just grab a copy of the latest Glasgow 
Haskell Compiler. While we're downloading stuff, we should probably get a copy of the 
solution.

Assuming Haskell is now in the path, we can compile and run our solution using the 
following commands:

```shell
ghc hello-world.hs
hello-world.exe  # Windows
./hello-world  # Unix/Linux/Mac
```

And, that's it! The "Hello, World!" string should print straight to the console.

[1]: https://www.onlinegdb.com/online_haskell_compiler
