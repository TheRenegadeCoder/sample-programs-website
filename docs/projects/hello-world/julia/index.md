---
title: Hello World in Julia
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-julia.jpg
tags: [julia, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Julia](https://sampleprograms.io/languages/julia) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```julia
println("Hello, World!")
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Julia](https://sampleprograms.io/languages/julia) was written by:

- Jeremy Griffith

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
