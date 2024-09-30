---
authors:
- Jeremy Grifski
- rzuckerm
date: 2019-05-07
featured-image: hello-world-in-hack.jpg
last-modified: 2023-08-23
layout: default
tags:
- hack
- hello-world
title: Hello World in Hack
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/hack/how-to-implement-the-solution.md
- sources/programs/hello-world/hack/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Hack](https://sampleprograms.io/languages/hack) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```hack
<<__EntryPoint>>
function main(): void {
    echo "Hello, World!";
}

```

{% endraw %}

Hello World in [Hack](https://sampleprograms.io/languages/hack) was written by:

- rzuckerm

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

At long last, let's take a stab at Hello World in Hack.

Although Hack is derived from PHP, this code looks quite
different than PHP. The first thing you'll notice is this:

```hack
<<__EntryPoint>>
```

The `<<...>>` is how Hack defines an attribute. The
[`__EntryPoint` attribute][1] defines a top-level function
where execution is started. That function is `main`, but it
does not have to be called `main`. Any function with the
`__EntryPoint` attribute will be considered the top-level
function.

Next, the `main` function is defined. For this sample program,
there are no command-line arguments to process, so no arguments are
needed. The function does not return anything, so the return type
is `void`.

Finally, there is the `echo` statement, which is exactly the same
as Hello World in PHP. However, I will point out that you can't mix
HTML with Hack like you can with PHP, so that's one of the biggest 
syntactic differences. Otherwise, both languages perform a similar 
function: backend web development.

[1]: https://docs.hhvm.com/hack/attributes/predefined-attributes#__entrypoint


## How to Run the Solution

If we want to try this code, we can use an [online Hack compiler][2].

Alternatively, we can download the Hack Virtual Machine to run
Hack code locally. From there, I recommend reading up on
[how to get started with Hack][3]. Getting everything up and running is
bit out of scope of this article.

[2]: https://www.jdoodle.com/execute-hack-online/
[3]: https://docs.hhvm.com/hack/getting-started/getting-started
