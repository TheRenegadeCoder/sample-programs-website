---
authors:
- stefanurkal
date: 2024-12-08
featured-image: longest-word-in-every-language.jpg
last-modified: 2024-12-08
layout: default
tags:
- coffeescript
- longest-word
title: Longest Word in Coffeescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/coffeescript/how-to-implement-the-solution.md
- sources/programs/longest-word/coffeescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Coffeescript](https://sampleprograms.io/languages/coffeescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```coffeescript
findLongestWord = (inputString) ->

  return usage() if not inputString

  words = inputString.split(/[" "\n]+/)  # Split the input string into words

  longestWord = ""

  for word in words
    if word.length > longestWord.length
      longestWord = word

  return longestWord.length
    
usage = () ->
    "Usage: please provide a string"
    
main = () ->
    args = process.argv
    return findLongestWord(args[2])
    

console.log main()



```

{% endraw %}

Longest Word in [Coffeescript](https://sampleprograms.io/languages/coffeescript) was written by:

- stefanurkal

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).