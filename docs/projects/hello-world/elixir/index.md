---
authors:
- Jeremy Grifski
- rzuckerm
date: 2019-05-08
featured-image: hello-world-in-elixir.jpg
last-modified: 2023-05-15
layout: default
tags:
- elixir
- hello-world
title: Hello World in Elixir
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/elixir/how-to-implement-the-solution.md
- sources/programs/hello-world/elixir/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Elixir](https://sampleprograms.io/languages/elixir) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elixir
IO.puts "Hello, World!"

```

{% endraw %}

Hello World in [Elixir](https://sampleprograms.io/languages/elixir) was written by:

- Jeremy Grifski

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Alright, let's get right to it.

As we can see, Hello World in Elixir is just a single line of
code. As usual, let's dig into it a bit.

Up first, we have a reference to the IO module. In Elixir, the `IO`
module is the standard tool for working with standard input and 
output as well as files and other devices. So, it makes sense that 
we'd use it here to gain access to standard output.

Up next, we call the `puts` function of the `IO` module. Like print in 
most languages, `puts` simply writes a value to standard output. In 
fact, we aren't limited to standard output. We can redirect the output 
to other streams such as standard error:

```elixir
IO.puts :stderr, "Uh Oh!"
```

At any rate, `puts`, in our primary example, will simply write "Hello, 
World!" to the user. To be honest, I'm surprised this is only the 
second time we've seen the `puts` keyword in this series, the first being 
Ruby.


## How to Run the Solution

As always, if we want to give the code above a try, we can use an [online Elixir editor][1].
Copy the code into the editor and hit run.

Alternatively, we can run the solution locally if we download the latest 
version of [Elixir][2]. After that, we'll want to get a copy of the solution. 
Assuming Elixir is in our path, all we have to do is run the following 
commands from the command line:

```shell
elixir hello-world.ex
```

If successful, the "Hello, World" string should print to the console.

[1]: https://www.jdoodle.com/execute-elixir-online/
[2]: https://elixir-lang.org/install.html
