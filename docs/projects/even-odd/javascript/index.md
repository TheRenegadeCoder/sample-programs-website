---
authors:
- Manan Gill
date: 2019-10-11
featured-image: even-odd-in-every-language.jpg
last-modified: 2019-10-12
layout: default
tags:
- even-odd
- javascript
title: Even Odd in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/javascript/how-to-implement-the-solution.md
- sources/programs/even-odd/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
const input = process.argv[2] != '' ? Number(process.argv[2]) : null; //coerce the input into a number, ignore empty string
if(!Number.isInteger(input)){ //if there is no input, input = undefined and the statement still prints
    console.log('Usage: please input a number');
} else {
    console.log(input%2 === 0 ? 'Even' : 'Odd');
}

```

{% endraw %}

Even Odd in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Manan Gill

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).