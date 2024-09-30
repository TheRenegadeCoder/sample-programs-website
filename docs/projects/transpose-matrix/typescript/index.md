---
authors:
- Vipin Yadav
date: 2023-10-07
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2023-10-07
layout: default
tags:
- transpose-matrix
- typescript
title: Transpose Matrix in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/typescript/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
const error_msg: string = "Usage: please enter the dimension of the matrix and the serialized matrix";
if (process.argv.length != 5) {
    console.log(error_msg);
    process.exit(1);
}
const cols: number = parseInt(process.argv[2]);
const rows: number = parseInt(process.argv[3]);
const list_str: string = process.argv[4];
if (isNaN(cols) || isNaN(rows) || list_str.length == 0) {
    console.log(error_msg);
    process.exit(1);
}
const list: number[] = list_str.split(",").map(function (x: string) { return parseInt(x); });

const matrix: number[][] = [];
for (let i: number = 0; i < rows; i++) {
    matrix.push(list.slice(i * cols, (i + 1) * cols));
}
const transpose: number[][] = [];
for (let i: number = 0; i < cols; i++) {
    transpose.push([]);
    for (let j: number = 0; j < rows; j++) {
        transpose[i].push(matrix[j][i]);
    }
}
console.log(transpose.map(function (x: number[]) { return x.join(", "); }).join(", "));
```

{% endraw %}

Transpose Matrix in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).