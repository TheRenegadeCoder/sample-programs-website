---
authors:
- Jeremy Griffith
- Jeremy Grifski
- rzuckerm
date: 2018-04-11
featured-image: hello-world-in-julia.jpg
last-modified: 2023-05-15
layout: default
tags:
- hello-world
- julia
title: Hello World in Julia
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/julia/how-to-implement-the-solution.md
- sources/programs/hello-world/julia/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Julia](https://sampleprograms.io/languages/julia) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```julia
println("Hello, World!")

```

{% endraw %}

Hello World in [Julia](https://sampleprograms.io/languages/julia) was written by:

- Jeremy Griffith

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

With the background out of the way, let's get right into our 
implementation of Hello World in Julia.

And unsurprisingly, that's it! We can implement Hello World 
in Julia in a single line.

Despite how easy the print functionality seems in Julia, there's 
actually a lot going on. First of all, `println` makes a call to 
print with an added newline character.

The print function handles any sort of IO, so we could theoretically 
pass our string to any IO stream. In this case, we leave the default 
standard output.

Regardless, print makes a call to a function named show. At that 
point, I'm not sure what happens, but I suspect there's some C-level 
call to `printf`.


## How to Run the Solution

With our solution ready, we probably want to run it. Perhaps the easiest
thing to do would be to take advantage of [Julia's online editor][1].
Unfortunately, it appears sign up is required to use it, but it's great
for running some code snippets.

Alternatively, we can [download the latest version of Julia][2]. While we're
at it, we should probably get a copy of the Hello World in Julia solution.
With everything read to go, navigate the command line to the folder
containing the solution. Then, run the following:

```shell
julia hello-world.jl
```

That should execute the script. Don't be afraid to leverage the Julia 
documentation if you get stuck.

[1]: https://www.tutorialspoint.com/execute_julia_online.php
[2]: https://julialang.org/downloads/
