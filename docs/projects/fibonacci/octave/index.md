---
authors:
- rzuckerm
date: 2023-12-09
featured-image: fibonacci-in-every-language.jpg
last-modified: 2023-12-09
layout: default
tags:
- fibonacci
- octave
title: Fibonacci in Octave
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/octave/how-to-implement-the-solution.md
- sources/programs/fibonacci/octave/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Octave](https://sampleprograms.io/languages/octave) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```octave
function fibonacci()
    usage = 'Usage: please input the count of fibonacci numbers to output';
    arg_list = argv();
    nargin = length(arg_list);
    if nargin == 0
        disp(usage);
        return;
    end

    n = str2num(arg_list{1});
    if length(n) ~= 1 || mod(n, 1) ~= 0
        disp(usage);
        return;
    end

    a(1) = 1;
    a(2) = 1;

    for i=1:n
        a(i+2) = a(i+1) + a(i);
        printf('%d: %d\n', i, a(i));
    end
end

```

{% endraw %}

Fibonacci in [Octave](https://sampleprograms.io/languages/octave) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).