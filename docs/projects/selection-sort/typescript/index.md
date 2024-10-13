---
authors:
- Meet Thakur
date: 2024-10-13
featured-image: selection-sort-in-every-language.jpg
last-modified: 2024-10-13
layout: default
tags:
- selection-sort
- typescript
title: Selection Sort in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/selection-sort/typescript/how-to-implement-the-solution.md
- sources/programs/selection-sort/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
function selectionSort(arr: number[]): number[] {
    const n = arr.length;

    for (let i = 0; i < n - 1; i++) {
        let minIndex = i;

        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }

        if (minIndex !== i) {
            const temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }

    return arr;
}

function displayUsage() {
    console.log('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
}

const args = process.argv.slice(2);

if (args.length === 0) {
    displayUsage();
    process.exit(1);
}

const inputString = args.join(' ');
if (inputString.trim() === '') {
    displayUsage();
    process.exit(1);
}

if (args.length === 1 && !args[0].includes(',')) {
    displayUsage();
    process.exit(1);
}

const numbers = inputString.split(',').map(arg => parseFloat(arg.trim())).filter(num => !isNaN(num));

if (numbers.length < 2) {
    displayUsage();
    process.exit(1);
}

const sortedNumbers = selectionSort(numbers);

console.log(sortedNumbers.join(', '));

```

{% endraw %}

Selection Sort in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Meet Thakur

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).