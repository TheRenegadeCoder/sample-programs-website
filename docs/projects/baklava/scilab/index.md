---
authors:
- rzuckerm
date: 2024-10-02
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-02
layout: default
tags:
- baklava
- scilab
title: Baklava in Scilab
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/scilab/how-to-implement-the-solution.md
- sources/programs/baklava/scilab/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Scilab](https://sampleprograms.io/languages/scilab) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scilab
function [result] = strRepeat(n, s)
    result = ''
    for i = 1:n
        result = result + s
    end
endfunction

for i = -10:10
    numSpaces = abs(i)
    mprintf('%s%s\n', strRepeat(numSpaces, ' '), strRepeat(21 - 2 * numSpaces, '*'))
end

```

{% endraw %}

Baklava in [Scilab](https://sampleprograms.io/languages/scilab) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).