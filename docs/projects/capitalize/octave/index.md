---
authors:
- rzuckerm
date: 2023-12-09
featured-image: capitalize-in-every-language.jpg
last-modified: 2023-12-09
layout: default
tags:
- capitalize
- octave
title: Capitalize in Octave
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/octave/how-to-implement-the-solution.md
- sources/programs/capitalize/octave/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Octave](https://sampleprograms.io/languages/octave) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```octave
function capitalize()
    usage = 'Usage: please provide a string';
    arg_list = argv();
    nargin = length(arg_list);
    if nargin == 0
        disp(usage);
        return;
    end

    string = arg_list{1};
    if length(string) == 0
        disp(usage);
        return;
    end

    disp(strcat(upper(string(1:1)), string(2:end)));
end

```

{% endraw %}

Capitalize in [Octave](https://sampleprograms.io/languages/octave) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).