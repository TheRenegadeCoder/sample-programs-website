---
authors:
- Ryan Mills
date: 2025-10-29
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2025-10-29
layout: default
tags:
- coffeescript
- remove-all-whitespace
title: Remove All Whitespace in Coffeescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/coffeescript/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/coffeescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Coffeescript](https://sampleprograms.io/languages/coffeescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```coffeescript

removeAllWhitespace = (inputString) ->
    return usage() if not inputString
    words = inputString.split(/[\s]+/)
    finalString = ''
    for word in words
        finalString += word
    return finalString
usage = () ->
    "Usage: please provide a string"

main = () ->
    args = process.argv
    return removeAllWhitespace(args[2])

console.log main()

```

{% endraw %}

Remove All Whitespace in [Coffeescript](https://sampleprograms.io/languages/coffeescript) was written by:

- Ryan Mills

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).