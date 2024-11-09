---
authors:
- brittLiban
date: 2024-11-09
featured-image: longest-word-in-every-language.jpg
last-modified: 2024-11-09
layout: default
tags:
- julia
- longest-word
title: Longest Word in Julia
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/julia/how-to-implement-the-solution.md
- sources/programs/longest-word/julia/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Julia](https://sampleprograms.io/languages/julia) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```julia
function longest_word_length(text::String)
    # Split on exactly the specified whitespace characters: space, tab, newline, carriage return
    words = split(text, r"[ \t\n\r]+")
    
    # Find the maximum length of the words array
    return maximum(length.(words))
end

# Command-line argument handling
if length(ARGS) == 0 || strip(ARGS[1]) == ""
    println("Usage: please provide a string")
    exit(1)
end

input_string = ARGS[1]
println(longest_word_length(input_string))

```

{% endraw %}

Longest Word in [Julia](https://sampleprograms.io/languages/julia) was written by:

- brittLiban

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).