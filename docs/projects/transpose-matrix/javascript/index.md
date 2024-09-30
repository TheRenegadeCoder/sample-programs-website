---
authors:
- Vipin Yadav
date: 2023-10-07
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2023-10-07
layout: default
tags:
- javascript
- transpose-matrix
title: Transpose Matrix in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/javascript/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
var error_msg = "Usage: please enter the dimension of the matrix and the serialized matrix";
if (process.argv.length != 5) {
    console.log(error_msg);
    process.exit(1);
}
var cols = parseInt(process.argv[2]);
var rows = parseInt(process.argv[3]);
var list_str = process.argv[4];
if (isNaN(cols) || isNaN(rows) || list_str.length == 0) {
    console.log(error_msg);
    process.exit(1);
}
var list = list_str.split(",").map(function (x) { return parseInt(x); });
var matrix = [];
for (var i = 0; i < rows; i++) {
    matrix.push(list.slice(i * cols, (i + 1) * cols));
}
var transpose = [];
for (var i = 0; i < cols; i++) {
    transpose.push([]);
    for (var j = 0; j < rows; j++) {
        transpose[i].push(matrix[j][i]);
    }
}
console.log(transpose.map(function (x) { return x.join(", "); }).join(", "));

```

{% endraw %}

Transpose Matrix in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).