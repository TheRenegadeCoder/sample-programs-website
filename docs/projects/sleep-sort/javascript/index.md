---
authors:
- Raakesh.R
date: 2023-10-23
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2023-10-23
layout: default
tags:
- javascript
- sleep-sort
title: Sleep Sort in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/sleep-sort/javascript/how-to-implement-the-solution.md
- sources/programs/sleep-sort/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
function sleepSort(arr) {
  const sortedArray = [];

  function sleepSortHelper(item) {
    setTimeout(() => {
      sortedArray.push(item);
      if (sortedArray.length === arr.length) {
        console.log(sortedArray.join(", "));
      }
    }, item*1000);
  }

  arr.forEach((item) => {
    if (item < 0) {
      console.log(error_msg);
      return;
    }
    sleepSortHelper(item);
  });
}

const error_msg =
  'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"';

function sortNumbers(input) {
  const numberList = input.split(",").map((item) => parseInt(item.trim()));

  if (numberList.length < 2) {
    console.log(error_msg);
  } else if (numberList.some(isNaN)) {
    console.log(error_msg);
  } else {
    sleepSort(numberList);
  }
}

const input = process.argv[2];

if (!input) {
  console.log(error_msg);
} else {
  sortNumbers(input);
}

```

{% endraw %}

Sleep Sort in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Raakesh.R

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).