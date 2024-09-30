---
authors:
- rzuckerm
date: 2023-12-09
featured-image: factorial-in-every-language.jpg
last-modified: 2023-12-09
layout: default
tags:
- factorial
- octave
title: Factorial in Octave
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/octave/how-to-implement-the-solution.md
- sources/programs/factorial/octave/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Octave](https://sampleprograms.io/languages/octave) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```octave
function factorial()
    usage = 'Usage: please input a non-negative integer';
    arg_list = argv();
    nargin = length(arg_list);
    if nargin == 0
        disp(usage);
        return;
    end

    n = str2num(arg_list{1});
    if length(n) ~= 1 || mod(n, 1) ~= 0 || n < 0
        disp(usage);
        return;
    end

    x = 1;
    for i = 1:n
        x = x * i;
    end

    disp(x);
end

```

{% endraw %}

Factorial in [Octave](https://sampleprograms.io/languages/octave) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).