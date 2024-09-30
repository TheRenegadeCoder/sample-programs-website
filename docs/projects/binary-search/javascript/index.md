---
authors:
- izexi
date: 2020-10-23
featured-image: binary-search-in-every-language.jpg
last-modified: 2020-10-23
layout: default
tags:
- binary-search
- javascript
title: Binary Search in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/javascript/how-to-implement-the-solution.md
- sources/programs/binary-search/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
const [, , array, target] = process.argv;
const error = 'Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")';

const binarySearch = (array, target, start = 0, end = array.length - 1) => {

  const isOrdered = array.every((num, i, arr) => !i || num >= arr[i - 1]);
  if (!isOrdered) return error;

  const middleIndex = Math.floor((start + end) / 2);
  const middleValue = array[middleIndex];
  const newIndexes =
    target < middleValue ? [start, middleIndex - 1] : [middleIndex + 1, end];

  return middleValue === target
    ? true
    : start >= end
        ? false
        : binarySearch(array, target, ...newIndexes);
};

console.log(array && target ? binarySearch(array.split(', '), target) : error);

```

{% endraw %}

Binary Search in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- izexi

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).