---
authors:
- "Christoph B\xF6hmwalder"
- rzuckerm
date: 2018-08-28
featured-image: fizz-buzz-in-every-language.png
last-modified: 2023-12-21
layout: default
tags:
- fizz-buzz
- vimscript
title: Fizz Buzz in Vimscript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/vimscript/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/vimscript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Vimscript](https://sampleprograms.io/languages/vimscript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```vimscript
func! FizzBuzz()
    for l:i in range(1, 100)
        if l:i % 15 == 0
            let l:str = 'FizzBuzz'
        elseif l:i % 5 == 0
            let l:str = 'Buzz'
        elseif l:i % 3 == 0
            let l:str = 'Fizz'
        else
            let l:str = l:i
        endif

        echo l:str
    endfor
endfunc

func! Main()
    call FizzBuzz()
endfunc

```

{% endraw %}

Fizz Buzz in [Vimscript](https://sampleprograms.io/languages/vimscript) was written by:

- Christoph Böhmwalder
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).