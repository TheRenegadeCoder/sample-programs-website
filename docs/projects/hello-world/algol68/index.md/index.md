---

title: Hello World in ALGOL 68
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-algol-68.jpg
tags: [algol68, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the Hello World in Algol68 page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Algol68
printf(($gl$, "Hello, World!"))

```

## How to Implement the Solution

Without further ado, let�s implement Hello World in ALGOL 68:

```algol
printf(($gl$, "Hello, World!"))
```

Now, I believe we can actually shorten this implementation to look identical to the 
[Python implementation][1]. But, that wouldn�t be too interesting. Instead, we opted 
to use a *printf* solution to show off a couple of features.

If you�re unfamiliar with *printf*, it�s typically a version of the print function 
which allows for string formatting. Unfortunately, that�s about where the similarities 
end. In ALGOL 68, the syntax for formatting text is about as bizarre as I�ve ever seen. 
Luckily, we have a simple example: `$gl$`.

In this example, everything between the dollar signs is considered a format string. 
In this case, we have two characters: *g* and *l*.

Since we�re formatting strings, one of those tokens will be replaced by our �Hello, World!� 
string. In this case, it�s *g*. As for *l*, that�s actually the newline token � something 
we haven�t paid a lot of attention to in this series. When put together, �Hello, World!� 
will print to the console.

Another interesting bit about this program is the fact that we have double parentheses 
that almost look redundant. But make no mistake, they�re important:

```console
1     printf($gl$, "Hello, World!")
      1                            
a68g: error: 1: incorrect number of arguments for PROC ([] "SIMPLOUT") VOID (detected in particular-program).
```

To be honest, I don�t understand the error. My best guess is *printf* requires an array 
of arguments. Whereas, the *varargs* solution I�m proposing issues the format string 
and �Hello, World!� as separate arguments. Fortunately, [James Jones has a great 
explanation for this][1].


## How to Run the Solution

Perhaps the easiest way to run the solution is to use an [online ALGOL 68 editor][2]. 
If we copy the solution above into the editor, we can hit execute to run it.

Alternatively, we have the option to install an ALGOL 68 interpreter. Apparently, there 
is a limited [ALGOL 68 Genie interpreter][3] which should get the job done. After all, 
it�s the same interpreter the online solution uses. Feel free to leverage the 
[documentation][4].
