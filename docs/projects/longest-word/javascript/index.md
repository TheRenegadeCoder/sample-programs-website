---
authors:
- Raakesh.R
date: 2023-10-24
featured-image: longest-word-in-every-language.jpg
last-modified: 2023-10-24
layout: default
tags:
- javascript
- longest-word
title: Longest Word in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/javascript/how-to-implement-the-solution.md
- sources/programs/longest-word/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
const error_msg = "Usage: please provide a string";
if (process.argv.length != 3) {
  console.log(error_msg);
  process.exit(1);
}

const inputString = process.argv[2].replace(/\n|\t|\r/g, " ");
if (inputString.trim().length == 0) {
  console.log(error_msg);
  process.exit(1);
}

const words = inputString.trim().split(" ");

let longestWordLength = 0;

for (const word of words) {
  if (word.length > longestWordLength) {
    longestWordLength = word.length;
  }
}

console.log(longestWordLength);

```

{% endraw %}

Longest Word in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Raakesh.R

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).