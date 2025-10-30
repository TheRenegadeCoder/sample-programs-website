---
authors:
- Brendan V
date: 2025-10-30
featured-image: capitalize-in-every-language.jpg
last-modified: 2025-10-30
layout: default
tags:
- capitalize
- coffeescript
title: Capitalize in Coffeescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/coffeescript/how-to-implement-the-solution.md
- sources/programs/capitalize/coffeescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Coffeescript](https://sampleprograms.io/languages/coffeescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```coffeescript
Usage = "Usage: please provide a string"

capitalize = (arg) ->
    charList = []
    for char, i in arg
        if i == 0
            charList.push(char.toUpperCase())
        else
            charList.push(char)
    return charList.join("")

main = () ->
    args = process.argv[2]
    if args
        capitalize(args)
    else 
        return Usage

console.log main()
```

{% endraw %}

Capitalize in [Coffeescript](https://sampleprograms.io/languages/coffeescript) was written by:

- Brendan V

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).