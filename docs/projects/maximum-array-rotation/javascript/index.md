---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-06
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2026-05-06
layout: default
tags:
- javascript
- maximum-array-rotation
title: Maximum Array Rotation in JavaScript
title1: Maximum Array Rotation
title2: in JavaScript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/javascript/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [JavaScript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
"use strict";

const USAGE = 'Usage: please provide a list of integers (e.g. "8, 3, 1, 2")';

const parse = (s) =>
  s
    .split(",")
    .filter((x) => x.trim() !== "")
    .map((x) => Number(x.trim()));

const maxArrayRotation = (arr) => {
  const n = arr.length;
  if (n === 0) return 0;

  let currentSum = 0;
  let totalSum = 0;

  for (let i = 0; i < n; i++) {
    totalSum += arr[i];
    currentSum += i * arr[i];
  }

  let maxSum = currentSum;

  for (let k = 1; k < n; k++) {
    const droppedValue = arr[n - k];
    currentSum = currentSum + totalSum - n * droppedValue;

    if (currentSum > maxSum) {
      maxSum = currentSum;
    }
  }

  return maxSum;
};

const run = () => {
  const [, , input] = process.argv;

  if (!input) {
    console.error(USAGE);
    process.exit(1);
  }

  const arr = parse(input);

  if (arr.length === 0 || arr.some(Number.isNaN)) {
    console.error(USAGE);
    process.exit(1);
  }

  console.log(maxArrayRotation(arr));
};

run();

```

{% endraw %}

Maximum Array Rotation in [JavaScript](https://sampleprograms.io/languages/javascript) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).