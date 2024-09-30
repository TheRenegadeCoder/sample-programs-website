---
authors:
- rzuckerm
- smjalageri
date: 2020-10-19
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-03-19
layout: default
tags:
- pascal
- reverse-string
title: Reverse String in Pascal
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/pascal/how-to-implement-the-solution.md
- sources/programs/reverse-string/pascal/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Pascal](https://sampleprograms.io/languages/pascal) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pascal
program reversestring(input, output, stdErr);
(*Accept a String from Command Line, Reverse it & Print it*)
var
  i, j: Integer;
   buf, result: String;
begin
  buf := paramStr(1);
  setlength(result,length(buf));
  i:=1; 
  j:=length(buf);
  while (i<=j) do
    begin
      result[i]:=buf[j-i+1];
      inc(i);
    end;
    writeln(result);
end.

```

{% endraw %}

Reverse String in [Pascal](https://sampleprograms.io/languages/pascal) was written by:

- rzuckerm
- smjalageri

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).