---
authors:
- rzuckerm
date: 2023-12-09
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2023-12-09
layout: default
tags:
- insertion-sort
- octave
title: Insertion Sort in Octave
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/insertion-sort/octave/how-to-implement-the-solution.md
- sources/programs/insertion-sort/octave/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Octave](https://sampleprograms.io/languages/octave) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```octave
function insertion_sort()
    %input validation
    usage = 'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"';
    arg_list = argv();
    nargin = length(arg_list);
    if  nargin == 0
        %if there was no input
        disp(usage);
        return;
    end

    array_string = arg_list{1};
    array_size = sum(array_string == ',') + 1;
    if array_size < 2
        disp(usage);
        return;
    end

    %build array
    array = str2num(array_string);
    if length(array) ~= array_size || any(mod(array, 1) ~= 0)
        disp(usage);
        return;
    end

    %insertion sort in ascending order
    for i = 2:array_size
        d = i;
        while d > 1 && array(d) < array(d-1)
            temp = array(d);
            array(d) = array(d-1);
            array(d-1) = temp;
            d = d - 1;
        end
    end

    %convert to string
    result_string = num2str(array);

    %replace space with ', '
    result_string = regexprep(result_string, '\s+', ', ');
    disp(result_string);
end

```

{% endraw %}

Insertion Sort in [Octave](https://sampleprograms.io/languages/octave) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).