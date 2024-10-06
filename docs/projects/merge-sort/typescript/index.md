---
authors:
- Aaron
date: 2024-10-06
featured-image: merge-sort-in-every-language.jpg
last-modified: 2024-10-06
layout: default
tags:
- merge-sort
- typescript
title: Merge Sort in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/merge-sort/typescript/how-to-implement-the-solution.md
- sources/programs/merge-sort/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript

function DisplayErrorMessage() {
    console.log(
        `Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"`,
    );
    process.exit(1);
}

/**
 * Processes user arguments from CLI, displays usages message and exits if arguments are incorrect
 * @returns user input argument as a list to be merge sorted
 */
function VerifyUserInput(): number[] {
    if (process.argv.length != 3) {
        DisplayErrorMessage();
    }
    // regex string to match requirements
    const regexStr = /^([0-9]+)((,  ?)([0-9]+))+$/;
    const regex = new RegExp(regexStr);
    const user_arg_pos = 2
    const numbers: string = process.argv[user_arg_pos];

    if (numbers.length == 0 || !numbers.match(regex)) {
        DisplayErrorMessage();
    }
    // split numbers into array and parse values
    return numbers.split(",").map((x) => parseInt(x));
}

/**
 * Sorts and merges divided subsets of array.
 * @param array the array to be sorted. Not that this will be updated.
 * @param first the start of the unsorted array
 * @param middle the middle of the unsorted array
 * @param last the end of the unsorted array
 */
function Merge(array: number[], first: number, middle: number, last: number) {
    // initial to "split" arrays
    const fixed_middle = middle + 1
    const fixed_last = last + 1
    const left = array.slice(first, fixed_middle)
    const right = array.slice(fixed_middle, fixed_last)
    const sortedArray = []
    // sort values into sorted array
    var index_left = 0
    var index_right = 0
    while (index_left < left.length) {
        var leftVal = left[index_left]
        if (index_right < right.length && right[index_right] < leftVal) {
            sortedArray.push(right[index_right])
            index_right++
        } else {
            sortedArray.push(leftVal)
            index_left++
        }
    }
    // modify the original array to include the new sorted array
    array.splice(first, sortedArray.length, ...sortedArray)
}

/**
 * Implements the Merge Sort algorithm by dividing the given array into smaller and smaller values
 * then sorting and merging the list
 * 
 * @param numbers the array to be sorted. Note that this will be updated
 * @param first the starting index of the array
 * @param last the ending index of the array
 */
function MergeSort(numbers: number[], first: number, last: number) {
    if (first < last) {
        var middle: number = Math.floor((first + last) / 2)
        MergeSort(numbers, first, middle)
        MergeSort(numbers, middle + 1, last)
        Merge(numbers, first, middle, last)
    }
}

// start program

const numbers: number[] = VerifyUserInput()
const first: number = 0
const last: number = numbers.length - 1
MergeSort(numbers, first, last)
console.log(numbers.join(", "))

```

{% endraw %}

Merge Sort in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Aaron

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).