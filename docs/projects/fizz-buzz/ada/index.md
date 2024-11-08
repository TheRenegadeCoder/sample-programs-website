---
authors:
- Rebecca Riffle
date: 2024-11-08
featured-image: fizz-buzz-in-every-language.png
last-modified: 2024-11-08
layout: default
tags:
- ada
- fizz-buzz
title: Fizz Buzz in Ada
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/ada/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/ada/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Ada](https://sampleprograms.io/languages/ada) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ada
with Text_IO; use Text_IO;

procedure Fizz_Buzz is
    Counter : Integer := 1;
begin
    while Counter < 101
        loop
            if Counter mod 3 = 0 and Counter mod 5 = 0 then
                Put_Line("FizzBuzz");
            elsif Counter mod 3 = 0 then
                Put_Line("Fizz");
            elsif Counter mod 5 = 0 then
                Put_Line("Buzz");
            else
                Put_Line(Integer'Image(Counter));
            end if;
            Counter := Counter + 1;
        end loop;
end Fizz_Buzz;
```

{% endraw %}

Fizz Buzz in [Ada](https://sampleprograms.io/languages/ada) was written by:

- Rebecca Riffle

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).