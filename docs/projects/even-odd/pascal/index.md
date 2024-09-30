---
authors:
- smjalageri
date: 2020-10-18
featured-image: even-odd-in-every-language.jpg
last-modified: 2020-10-18
layout: default
tags:
- even-odd
- pascal
title: Even Odd in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/pascal/how-to-implement-the-solution.md
- sources/programs/even-odd/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program a1(input, output, stdErr);
(* Read Number from commandline, print  Even or Odd *)
var
 buf: String;
 a, check:integer;
begin    
  buf:= paramStr(1);
    Val(buf, a, check) ;
    if check <> 0
    then
    writeln('Usage: please input a number')
    else
    begin
        if( (a mod 2) = 0) then
            begin
            writeln('Even'); 
            end         
        else
            begin
            writeln('Odd'); 
            end
    end
end.

```

{% endraw %}

Even Odd in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- smjalageri

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).