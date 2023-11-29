---
authors:
- Jeremy Grifski
- rzuckerm
date: 2022-04-28
featured-image: hello-world-in-c-star.jpg
last-modified: 2023-11-29
layout: default
tags:
- c-star
- hello-world
title: Hello World in C*
---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [C\*](https://sampleprograms.io/languages/c-star) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c\*
void main()
{
    println("Hello, World!");
}

```

{% endraw %}

Hello World in [C\*](https://sampleprograms.io/languages/c-star) was written by:

- rzuckerm

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

At long last, here's Hello World in C*.

As we can see, Hello World in C* looks alarmingly similar to C. That said, C*
is a superset of C, so this shouldn't be too much of a surprise. At any rate,
let's dig in.

Up first, we have the `include` statement which pulls in the `stdio` header. With
the standard IO header included, we're able to write to standard output using
`printf`.

Next, we have our usual `main` function declaration which serves as the drop in
function for our program. We should be used to seeing this convention since it's
common in the popular industrial languages like C++ and Java.

Finally, we make a call to `printf` which is a special print function that allows
for string formatting. Of course, all we're going to pass to it is the "Hello,
World!" string. And, that's it!


## How to Run the Solution

Unfortunately, I haven't found a way to execute C* programs. That said, I did
find a handful of open-source C* compilers, so maybe those can help us out:

- <https://github.com/KayvanMazaheri/c-star-compiler>
- <https://github.com/renjithgr/cstar-compiler-Java>

In addition, the [user guide][1] does detail how to compile and run C* programs. But,
again, that information isn't super helpful without the compiler.

If you know of an official compiler, let me know in the comments.

[1]: https://people.csail.mit.edu/bradley/cm5docs/CStarUsersGuide.pdf
