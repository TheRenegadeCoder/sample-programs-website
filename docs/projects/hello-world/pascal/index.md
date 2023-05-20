---
title: Hello World in Pascal
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-pascal.jpg
tags: [pascal, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program HelloWorld(output);
begin
  writeln('Hello, World!');
end.
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- Jeremy Griffith

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's dig right into Hello World in Pascal.

As usual, we'll tackle this implementation line by line. Up
first, we have the program line which declares the name of
the program and a list of file descriptors.

Up next, we have our main block which is denoted by the `begin`
and `end` keywords. Within this block, we have the print statement.
Of course, the function we use in Pascal is called `writeln`.

Finally, we have a period, also known as a full stop. This
indicates the end of the program.

As an added tidbit, semicolons mark the ends of statements, but 
they are optional on the last statement in a block. In other words, 
we could have removed the semicolon after the writeln command.


## How to Run the Solution

If we want to try any of the Pascal code snippets from this article, 
we can use an [online Pascal compiler][1]. We just need to drop the snippets 
into the online editor and hit run.

Of course, we can always [download and install Pascal locally][2]. While 
we're downloading stuff, we should probably get a copy of the solution.

Assuming Pascal is now in our path, we can navigate to our folder 
containing the solution and run the following commands from the terminal:

```shell
fpc hello-world.p
hello-world.exe  # Windows
./hello-world  # Unix/Linux/Mac
```

Since Pascal is a compiled language, we first need to compile our script. 
After compilation, we'll have an executable we can run. When we run it, the 
"Hello, World!" string should print to the console.

[1]: https://www.onlinegdb.com/online_pascal_compiler
[2]: https://www.freepascal.org/download.html
