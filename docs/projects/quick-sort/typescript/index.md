---
authors:
- Raakesh.R
date: 2023-10-21
featured-image: quick-sort-in-every-language.jpg
last-modified: 2023-10-21
layout: default
tags:
- quick-sort
- typescript
title: Quick Sort in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quick-sort/typescript/how-to-implement-the-solution.md
- sources/programs/quick-sort/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
function quickSort(arr: number[]): number[] {
  if (arr.length <= 1) {
    return arr;
  }

  const pivot = arr[0];
  const left = [];
  const right = [];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }

  return [...quickSort(left), pivot, ...quickSort(right)];
}

const error_msg: string =
  'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"';

if (process.argv.length != 3) {
  console.log(error_msg);
  process.exit(1);
}

let list_str: string = process.argv[2];

if (list_str.length == 0) {
  console.log(error_msg);
  process.exit(1);
}
let list: number[] = list_str.split(",").map((x: string) => parseInt(x));
if (list.length < 2) {
  console.log(error_msg);
  process.exit(1);
}
const sortedArray: number[] = quickSort(list);
console.log(sortedArray.join(", "));

```

{% endraw %}

Quick Sort in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Raakesh.R

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).