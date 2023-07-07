---
authors:
- Jeremy Grifski
- Nick Keers
- rzuckerm
date: 2018-08-08
featured-image: hello-world-in-erlang.jpg
last-modified: 2023-05-15
layout: default
tags:
- erlang
- hello-world
title: Hello World in Erlang
---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Erlang](https://sampleprograms.io/languages/erlang) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```erlang
-module(hello_world).
-export([start/0]).

start() ->
   io:format("Hello, World!~n").

```

{% endraw %}

Hello World in [Erlang](https://sampleprograms.io/languages/erlang) was written by:

- Jeremy Grifski
- Nick Keers

This article was written by:

- Jeremy Grifski
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
-export([start/0]).
```

This exports our `start` function, it takes no arguments so we reference the function as `start/0`. The number of arguments is called the "arity" of the function.


Functions in Erlang start with an atom (for now, think of these as just lowercase letters + underscores), then the parameters, followed by an arrow `->`. The following functions are both valid:

```erlang
my_function() ->
  ok.

myfunction() ->
  ok.
```

Our `start` function only does one thing for this simple program, it calls the `format` function from the `io` module to print characters to standard output by default. `io:format()`. The string `"Hello world!~n"` includes the newline control sequence `~n` - you can see a list of control sequences available for use in the documentation for `io:fwrite` [here][1] (scroll down to "Available control sequences").

[1]: https://www.erlang.org/doc/man/io.html#fwrite-1


## How to Run the Solution

To run this example, you need to follow a few steps:

1. Run `erlc hello_world.erl` in your terminal to compile the program to a BEAM file - this results in the file `hello_world.beam`
2. In the same directory, open the erlang shell by typing `erl`.
3. Type `l(hello_world).` - remember to end with a period! This is to *load* a module into the shell
4. Run the start function from the module by calling `hello_world:start().` - you should see `Hello, World!` printed to the shell.
5. To exit the shell type `q().` _or_ Ctrl-C, a (abort).
