---
authors:
- Raakesh.R
date: 2023-10-22
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2023-10-22
layout: default
tags:
- insertion-sort
- typescript
title: Insertion Sort in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/insertion-sort/typescript/how-to-implement-the-solution.md
- sources/programs/insertion-sort/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
function insertionSort(arr: number[]): number[] {
  const n = arr.length;

  for (let i = 1; i < n; i++) {
    const currentElement = arr[i];
    let j = i - 1;

    while (j >= 0 && arr[j] > currentElement) {
      arr[j + 1] = arr[j];
      j--;
    }

    arr[j + 1] = currentElement;
  }

  return arr;
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
const sortedArray: number[] = insertionSort(list);
console.log(sortedArray.join(", "));
```

{% endraw %}

Insertion Sort in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Raakesh.R

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).