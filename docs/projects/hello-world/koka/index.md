---
title: Hello World in Koka
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-koka-featured-image.JPEG
tags: [koka, hello-world]
authors:
  - bassem_mohamed
---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Koka](https://sampleprograms.io/languages/koka) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```koka
fun main() 
{
    println("Hello, World!")
}
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Koka](https://sampleprograms.io/languages/koka) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Now, let's see how we can print a simple "Hello World" in Koka:

```koka
function main()
{
  println("Hello, World!")
}
```

Just like many other programming languages, the main function is the starting
point of the code execution. To print, we use println, a built-in method that
prints a given string or variable to the console.

Like many of the high-level language implementations in this series, this one
wasn't too bad. Wanna try it out? Check out this [online Koka editor][1].


## How to Run the Solution

If you want to run Koka at your local machine, you can always install the Koka
compiler and try the snippet locally. There are no binary releases of Koka though.
You will have to build the compiler yourself. Don't worry! It sounds harder than
it is. All you need to do is install the following programs:

- The [Haskell platform][2] (version 7.4 or later)
- The [NodeJS runtime][3] (version 4.2 LTS or later)
- [Git][4] for version control

Now, you need to [clone the Koka repository][5] to your local environment. Then,
run the following commands at the local repo directory:

```console
npm install
cabal update
cabal install alex
jake
```

jake is the command for building the compiler, and it also runs the Koka
interactive environment where you can play around with Koka.

To actually run the solution, you need to run the following commands:

```console
:l YOUR_FILE.kk
main()
```

There you go! The sky is the limit now. But if you need help, you can check out
the [Koka book][6] and [the documentation][7].
