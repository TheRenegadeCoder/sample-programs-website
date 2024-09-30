---
authors:
- rzuckerm
date: 2023-12-09
featured-image: even-odd-in-every-language.jpg
last-modified: 2023-12-09
layout: default
tags:
- even-odd
- octave
title: Even Odd in Octave
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/octave/how-to-implement-the-solution.md
- sources/programs/even-odd/octave/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Octave](https://sampleprograms.io/languages/octave) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```octave
function even_odd()
    usage = 'Usage: please input a number';
    arg_list = argv();
    nargin = length(arg_list);
    if (nargin==0)
        %if there was no input
        disp(usage);
    else
        number = str2num(arg_list{1});
        if length(number) ~= 1 || mod(number, 1) ~= 0
            %check whether input is a number
            %also check if input is an integer
            disp(usage);
        else
            if mod(number, 2) == 0
                disp('Even');
            else
                disp('Odd');
            end
        end
    end
end

```

{% endraw %}

Even Odd in [Octave](https://sampleprograms.io/languages/octave) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).