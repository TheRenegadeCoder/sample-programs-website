---
authors:
- rzuckerm
date: 2023-02-16
featured-image: file-input-output-in-every-language.jpg
last-modified: 2023-02-19
layout: default
tags:
- euphoria
- file-input-output
title: File Input Output in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/euphoria/how-to-implement-the-solution.md
- sources/programs/file-input-output/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e

function write_file(sequence filename)
    integer fn = open(filename, "w")
    if fn < 0
    then
        printf(STDERR, "Cannot open %s for write\n", {filename})
        return FALSE
    end if

    puts(fn, "Hello from Euphoria!\n")
    puts(fn, "This is a line\n")
    puts(fn, "This is another line\n")
    puts(fn, "Goodbye!\n")
    close(fn)
    return TRUE
end function

function read_file(sequence filename)
    integer fn = open(filename, "r")
    if fn < 0
        then
        printf(STDERR, "Cannot open %s for read\n", {filename})
        return FALSE
    end if

    object line
    while 1
    do
        line = gets(fn)
        if atom(line)
        then
            exit
        end if

        puts(STDOUT, line)
    end while

    close(fn)
    return TRUE
end function

constant filename = "output.txt"
if write_file(filename)
then
    read_file(filename)
end if

```

{% endraw %}

File Input Output in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).