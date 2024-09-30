---
authors:
- smjalageri
date: 2022-10-02
featured-image: capitalize-in-every-language.jpg
last-modified: 2022-10-02
layout: default
tags:
- capitalize
- julia
title: Capitalize in Julia
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/julia/how-to-implement-the-solution.md
- sources/programs/capitalize/julia/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Julia](https://sampleprograms.io/languages/julia) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```julia
#!/usr/bin/julia
# Capitalize first character of the input string
# Function to print Error message
function err()
  println("Usage: please provide a string")
end
# Function to capitalize the input string
function capitalize(n)
  if (length(n) in [0,1])
    err()
  else
    println(uppercasefirst(n))
  end
end

try
  capitalize(ARGS[1])
catch e
  err()
end

```

{% endraw %}

Capitalize in [Julia](https://sampleprograms.io/languages/julia) was written by:

- smjalageri

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).