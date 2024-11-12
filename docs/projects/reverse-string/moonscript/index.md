---
authors:
- dannymccarragher
date: 2024-11-12
featured-image: reverse-string-in-every-language.jpg
last-modified: 2024-11-12
layout: default
tags:
- moonscript
- reverse-string
title: Reverse String in Moonscript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/moonscript/how-to-implement-the-solution.md
- sources/programs/reverse-string/moonscript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Moonscript](https://sampleprograms.io/languages/moonscript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```moonscript
-- Function to reverse a string
reverse_string = (str) ->
    if str == '' then return ''
    
    result = ''

    for i = #str, 1, -1
        result = result .. str\sub(i, i)

    return result

-- Main executable section

if not arg or #arg == 0
    print ''
else
    input_str = arg[1]  
    reversed_str = reverse_string(input_str)
    print reversed_str
    

```

{% endraw %}

Reverse String in [Moonscript](https://sampleprograms.io/languages/moonscript) was written by:

- dannymccarragher

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).