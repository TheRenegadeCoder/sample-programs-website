---

title: Hello World in Pascal
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-pascal-featured-image.JPEG
tags: [pascal, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the Hello World in Pascal page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Pascal
program HelloWorld(output);
begin
  writeln('Hello, World!');
end.

```

## How to Implement the Solution

There�s no time to waste! Let�s dig right into Hello World 
in Pascal:

```pascal
program HelloWorld(output);
begin
  writeln('Hello, World!');
end.
```

As usual, we�ll tackle this implementation line by line. Up 
first, we have the program line which declares the name of 
the program and a list of file descriptors.

Up next, we have our main block which is denoted by the begin 
and end keywords. Within this block, we have the print statement. 
Of course, the function we use in Pascal is called writeln.

Finally, we have a period, also known as a full stop. This 
indicates the end of the program.

As an added tidbit, semicolons mark the ends of statements, but 
they are optional on the last statement in a block. In other words, 
we could have removed the semicolon after the writeln command.


## How to Run the Solution

If we want to try any of the Pascal code snippets from this article, 
we can use an online Pascal compiler. We just need to drop the snippets 
into the online editor and hit run.

Of course, we can always download and install Pascal locally. While 
we�re downloading stuff, we should probably get a copy of the solution.

Assuming Pascal is now in our path, we can navigate to our folder 
containing the solution and run the following commands from the terminal:

```shell
fpc hello-world.p
hello-world.exe  # Windows
./hello-world  # Unix/Linux/Mac
```

Since Pascal is a compiled language, we first need to compile our script. 
After compilation, we�ll have an executable we can run. When we run it, the 
�Hello, World!� string should print to the console.
