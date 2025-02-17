---
authors:
- RJ Fredrick Rico
date: 2025-02-17
featured-image: fibonacci-in-every-language.jpg
last-modified: 2025-02-17
layout: default
tags:
- fibonacci
- moonscript
title: Fibonacci in Moonscript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/moonscript/how-to-implement-the-solution.md
- sources/programs/fibonacci/moonscript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Moonscript](https://sampleprograms.io/languages/moonscript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```moonscript
-- fibonacci function
fibonacci = (n) ->
    -- set up a, b, for i until n, print "i: n" then update a & b as the fibonacci sequence
    a, b = 1, 1
    for i = 1, n
        print "#{i}: #{a}"
        a, b = b, a + b

-- main
-- check if arg params are numbers and are greater than 0
if arg[1] and tonumber(arg[1]) ~= nil and tonumber(arg[1]) >= 0
    fibonacci tonumber(arg[1])
-- else, return usage error msg
else   
    print "Usage: please input the count of fibonacci numbers to output"
    
```

{% endraw %}

Fibonacci in [Moonscript](https://sampleprograms.io/languages/moonscript) was written by:

- RJ Fredrick Rico

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).