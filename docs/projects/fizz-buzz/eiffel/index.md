---
authors:
- Zia
date: 2025-01-19
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-19
layout: default
tags:
- eiffel
- fizz-buzz
title: Fizz Buzz in Eiffel
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/eiffel/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/eiffel/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Eiffel](https://sampleprograms.io/languages/eiffel) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```eiffel
class
    fizz_buzz

create
    make

feature
    make
        do
            across 1 |..| 100 as i
            loop
                if i.item \\ 15 = 0 then io.put_string("FizzBuzz")
                elseif i.item \\ 5 = 0 then io.put_string("Buzz")
                elseif i.item \\ 3 = 0 then io.put_string("Fizz")
                else io.put_integer(i.item)
                end
                
                io.put_new_line
            end
        end
    end

```

{% endraw %}

Fizz Buzz in [Eiffel](https://sampleprograms.io/languages/eiffel) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).