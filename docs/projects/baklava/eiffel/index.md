---
authors:
- rzuckerm
date: 2025-01-08
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-08
layout: default
tags:
- baklava
- eiffel
title: Baklava in Eiffel
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/eiffel/how-to-implement-the-solution.md
- sources/programs/baklava/eiffel/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Eiffel](https://sampleprograms.io/languages/eiffel) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```eiffel
class 
    baklava

create
    make

feature

    make
        local
            num_spaces: INTEGER
            num_stars: INTEGER
        do 
            across
                -10 |..| 10 as n
            loop
                num_spaces := n.item.abs
                num_stars := 21 - 2 * num_spaces
                print (repeat_string(" ", num_spaces) + repeat_string("*", num_stars) + "%N")
            end
        end

    repeat_string(s: STRING; n: INTEGER): STRING
        do
            Result := ""
            across
                1 |..| n as x
            loop
                Result := Result + s
            end
        end
end

```

{% endraw %}

Baklava in [Eiffel](https://sampleprograms.io/languages/eiffel) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).