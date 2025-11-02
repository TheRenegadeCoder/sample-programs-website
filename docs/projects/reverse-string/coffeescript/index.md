---
authors:
- Brendan Villaraza
date: 2025-11-02
featured-image: reverse-string-in-every-language.jpg
last-modified: 2025-11-02
layout: default
tags:
- coffeescript
- reverse-string
title: Reverse String in Coffeescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/coffeescript/how-to-implement-the-solution.md
- sources/programs/reverse-string/coffeescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Coffeescript](https://sampleprograms.io/languages/coffeescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```coffeescript
reverseString = (arg) ->
    reversed = ""
    if not arg
        return ""
    for char, i in arg
        reversed += arg[arg.length - 1 - i]
    return reversed

main = () ->
    args = process.argv[2]
    return reverseString(args)

console.log(main())
```

{% endraw %}

Reverse String in [Coffeescript](https://sampleprograms.io/languages/coffeescript) was written by:

- Brendan Villaraza

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).