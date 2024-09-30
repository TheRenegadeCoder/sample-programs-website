---
authors:
- rzuckerm
date: 2023-12-09
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2023-12-09
layout: default
tags:
- bubble-sort
- octave
title: Bubble Sort in Octave
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/octave/how-to-implement-the-solution.md
- sources/programs/bubble-sort/octave/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Octave](https://sampleprograms.io/languages/octave) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```octave
function bubble_sort()
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

    %to keep track of whether any changes have been made on each pass
    flag = 1;

    while flag == 1
        flag = 0;
        for i = 1:array_size-1
            if array(i) > array(i+1)
                temp = array(i+1);
                array(i+1) = array(i);
                array(i) = temp;
                flag = 1;
            end
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

Bubble Sort in [Octave](https://sampleprograms.io/languages/octave) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).