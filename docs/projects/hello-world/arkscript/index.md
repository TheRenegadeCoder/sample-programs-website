---
authors:
- Alexandre Plateau
- SuperFola
date: 2020-10-03
featured-image: hello-world-in-every-language.jpg
last-modified: 2024-09-30
layout: default
tags:
- arkscript
- hello-world
title: Hello World in Arkscript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/arkscript/how-to-implement-the-solution.md
- sources/programs/hello-world/arkscript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Arkscript](https://sampleprograms.io/languages/arkscript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```arkscript
(print "Hello, World!")
```

{% endraw %}

Hello World in [Arkscript](https://sampleprograms.io/languages/arkscript) was written by:

- SuperFola

This article was written by:

- Alexandre Plateau

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

ArkScript programs do not require a `main` function as in C or C++. Every expression is executed, thus a single `(print "Hello, World!")` can write to the console.

A modular way to write the program could be as follows:

```arkscript
(let say (fun (to)
  (print (str:format "Hello, {}!" to))))

(say "World")
```

1. The first line, `(let say (fun (to)`, declares a function named `say`, taking a single argument, `to`.
2. On the second line, we have a call to `str:format`: it takes a format string and values to be formatted
    1. This is then wrapped in a call to `print` to write the resulting string to the console
3. On the last line, we call the `say` function with the argument `World`, printing `Hello, World!`



## How to Run the Solution

Using the online playground:

1. Go to [playground.arkscript-lang.dev](https://playground.arkscript-lang.dev/#/pages/ide/ark/hello_world.template)
2. Copy the code you want to run, eg `(print "Hello, World!")`, and paste it in the editor
3. Click the `Run` button

Using the interpreter:

1. Download the [latest release](https://github.com/ArkScript-lang/Ark/releases)
  1. See [the documentation](https://arkscript-lang.dev/tutorials/building.html#from-a-release) in case you need help finding the correct binary & installing it
2. Create a `file.ark` with your code inside
3. Run it using `arkscript file.ark`

Using Docker:

1. Pull `arkscript/nightly:latest`
2. Create a `file.ark` with your code inside
3. Run it using `docker run --rm -v $(pwd):/tmp arkscript/nightly /tmp/file.ark`

