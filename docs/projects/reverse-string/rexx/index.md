---
authors:
- Emily Menken
date: 2025-02-17
featured-image: reverse-string-in-every-language.jpg
last-modified: 2025-02-17
layout: default
tags:
- reverse-string
- rexx
title: Reverse String in Rexx
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/rexx/how-to-implement-the-solution.md
- sources/programs/reverse-string/rexx/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Rexx](https://sampleprograms.io/languages/rexx) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rexx
/* Reverse-String */

parse arg inputString
if inputString = "" then exit  /* exits right away if there is no input! */

say reverseString(inputString)
exit

reverseString:
parse arg str
length = length(str)
reversed = ""

do i = length to 1 by -1
reversed = reversed || substr(str, i, 1)
end

return reversed 
/* Req: Hello, World   Expected Res: dlroW ,olleH */

```

{% endraw %}

Reverse String in [Rexx](https://sampleprograms.io/languages/rexx) was written by:

- Emily Menken

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).