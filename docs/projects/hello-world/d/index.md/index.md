---

title: Hello World in D
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-d-featured-image.JPEG
tags: [d, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the Hello World in D page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```D
import std.stdio;

void main()
{
	writeln("Hello, World!");
}

```

## How to Implement the Solution

At any rate, let�s get to the implementation of Hello World in D:

```d
import std.stdio;
void main()
{
    writeln("Hello, World!");
}
```

At this point, you may be questioning whether or not D is even a new 
language. After all, this Hello World implementation looks a lot like 
C/C++.

Well, then it should come as no surprise the solution is pretty much 
the same. We have basically three main parts: the import statement, 
the main function, and the print function.

Just like C/C++, the first thing we do is import our standard output 
library. In this case, D references std.stdio as opposed to stdio.h 
in C.

Up next, we have our usual main function. At this point in the series, 
we�re pretty use to this syntax.

Finally, we have our typical print function. In this case, we call 
writeln and pass a string to it.


## How to Run the Solution

If we wanted to run our code snippet from above, we can leverage an 
online D compiler.

Alternatively, we can download our own D compiler from the official 
website. Then, we�ll want to get a copy of Hello World in D. After 
that, we can simply run the following:

```shell
rdmd hello-world.d
```

And, that�s it! The string �Hello, World!� should appear in the console.
