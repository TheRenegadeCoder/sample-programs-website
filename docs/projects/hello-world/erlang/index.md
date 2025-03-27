---
authors:
- Jeremy Grifski
- Nick Keers
- rzuckerm
date: 2018-08-08
featured-image: hello-world-in-erlang.jpg
last-modified: 2023-11-21
layout: default
tags:
- erlang
- hello-world
title: Hello World in Erlang
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/erlang/how-to-implement-the-solution.md
- sources/programs/hello-world/erlang/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Erlang](https://sampleprograms.io/languages/erlang) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```erlang
-module(hello_world).
-export([main/1]).

main(_) ->
   io:format("Hello, World!~n").

```

{% endraw %}

Hello World in [Erlang](https://sampleprograms.io/languages/erlang) was written by:

- Jeremy Grifski
- Nick Keers
- rzuckerm

This article was written by:

- Nick Keers
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Erlang looks scary when you first look at it, so we'll show the full program and
then we'll break it down into parts to fully describe it.

### Breaking it down

The first key part of an Erlang program is the `-module().` preprocessor directive:

```erlang
-module(hello_world).
```

Every Erlang file **must** start with this directive or you'll get a compiler error like the following:

```
file.erl:2: no module definition
```

Next, to use functions from the module we've written we have to export them explicitly.

```erlang
-export([main/1]).
```

This exports our `main` function, it takes one argument so we reference the function as `main/1`. The number of arguments is called the "arity" of the function.


Functions in Erlang start with an atom (for now, think of these as just lowercase letters + underscores), then the parameters, followed by an arrow `->`. The following functions are both valid:

```erlang
my_function() ->
  ok.

myfunction() ->
  ok.
```

Our `main` function only does one thing for this simple program, it calls the `format` function from the `io` module to print characters to standard output by default. `io:format()`. The string `"Hello world!~n"` includes the newline control sequence `~n` - you can see a list of control sequences available for use in the documentation for `io:fwrite` [here][1] (scroll down to "Available control sequences").

[1]: https://www.erlang.org/doc/man/io.html#fwrite-1


## How to Run the Solution

To run this example, just run `escript hello_world.erl`.
