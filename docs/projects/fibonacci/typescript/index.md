---
authors:
- Chris Thomas
- rzuckerm
date: 2018-10-12
featured-image: fibonacci-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- fibonacci
- typescript
title: Fibonacci in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/typescript/how-to-implement-the-solution.md
- sources/programs/fibonacci/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
function fibonacci(num: number) {

  let n = Number(num);
  let elementOne: number = 0;
  let elementTwo: number = 1;
  let result: number = 0;

  for (let i: number = 1; i <= n; i++) {
    result = elementOne + elementTwo;
    elementOne = elementTwo;
    elementTwo = result;
    console.log(`${i}: ${elementOne}`);
  }

}

let num_str = (process.argv.length >= 3) ? process.argv[2] : ""
let num: number = parseInt(num_str);
if (isNaN(num)) {
  console.log("Usage: please input the count of fibonacci numbers to output")
  process.exit(0)
}

fibonacci(num);

```

{% endraw %}

Fibonacci in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Chris Thomas
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).