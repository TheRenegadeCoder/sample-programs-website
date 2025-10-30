---
authors:
- liliann19
date: 2025-10-30
featured-image: reverse-string-in-every-language.jpg
last-modified: 2025-10-30
layout: default
tags:
- nit
- reverse-string
title: Reverse String in Nit
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/nit/how-to-implement-the-solution.md
- sources/programs/reverse-string/nit/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Nit](https://sampleprograms.io/languages/nit) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```nit
if args.length > 0 then
    var word = args[0]
    var reversed = ""
    var i = word.length - 1
    while i >= 0 do 
        reversed += word.chars[i].to_s
        i -= 1
    end
    printn reversed
end
```

{% endraw %}

Reverse String in [Nit](https://sampleprograms.io/languages/nit) was written by:

- liliann19

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).