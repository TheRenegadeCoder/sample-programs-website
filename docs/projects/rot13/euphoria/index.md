---
authors:
- rzuckerm
date: 2023-02-17
featured-image: rot13-in-every-language.jpg
last-modified: 2023-02-24
layout: default
tags:
- euphoria
- rot13
title: Rot13 in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/euphoria/how-to-implement-the-solution.md
- sources/programs/rot13/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e
include std/text.e
include std/utils.e

function rot13(sequence s)
    sequence t = ""
    for n = 1 to length(s)
    do
        -- If A-M or a-m, convert to N-Z or n-z by adding 13 to ASCII code
        -- Else, convert to A-M or a-m by subtracting 13 from ASCII code
        integer offset = 0
        if t_alpha(s[n])
        then
            offset = iif(lower(s[n]) <= 'm', 13, -13)
        end if

        t &= s[n] + offset
    end for

    return t
end function

procedure usage()
    puts(STDOUT, "Usage: please provide a string to encrypt\n")
    abort(0)
end procedure

-- Parse 1st command-line argument
sequence argv = command_line()
if length(argv) < 4 or length(argv[4]) = 0
then
    usage()
end if

-- Encrypt string with ROT13 and display
sequence s = argv[4]
sequence t = rot13(s)
printf(STDOUT, "%s\n", {t})

```

{% endraw %}

Rot13 in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).