---

title: Hello World in Scheme
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-scheme-featured-image.JPEG
tags: [scheme, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the Hello World in Scheme page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Scheme
(display "Hello, World!")
```

{% endraw %}

## How to Implement the Solution

At long last, here's an implementation of Hello World in Scheme:

```scheme
(display "Hello, World!")
```
If you checked out the tutorial on Hello World in Lisp, then this should be easy. First things first, we have the *display* function. The *display* function works exactly as you would expect. It takes some input and displays it to the user.

As a result, it's natural to expect that the input in this case is Hello World. All we do is pass the Hello World string to display, and we're done.


## How to Run the Solution

As usual, we can give it a go with an [online Scheme interpreter][1]. Just drop the code above into the editor and hit run.

Alternatively, we can download [CHICKEN Scheme][2] and a copy of the solution. Assuming CHICKEN Scheme is on our path, we can run the following from a command line:

```bash
csi -s hello-world.scm
```
That will run the Scheme file as a script which will quickly print the "Hello, World!" string.
