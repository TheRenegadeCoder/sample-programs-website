---
authors:
- Meet Thakur
date: 2025-10-11
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2025-10-11
layout: default
tags:
- maximum-subarray
- typescript
title: Maximum Subarray in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/typescript/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
function printUsage(): void {
    console.log('Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"');
}

function maxSubarraySum(arr: number[]): number {
    let maxSoFar = Number.MIN_SAFE_INTEGER;
    let maxEndingHere = 0;

    for (let i = 0; i < arr.length; i++) {
        maxEndingHere += arr[i];

        if (maxSoFar < maxEndingHere) {
            maxSoFar = maxEndingHere;
        }

        if (maxEndingHere < 0) {
            maxEndingHere = 0;
        }
    }

    return maxSoFar;
}

function main(): void {
    const args = process.argv.slice(2);

    if (args.length < 1) {
        printUsage();
        process.exit(1);
    }

    // Check if input is empty
    if (args[0].length === 0) {
        printUsage();
        process.exit(1);
    }

    // Parse input string
    const arr = args[0].split(',').map(s => parseInt(s.trim()));

    // If less than two integers were provided
    if (arr.length === 1) {
        console.log(arr[0]);
        return;
    } else if (arr.length < 1) {
        printUsage();
        process.exit(1);
    }

    // Calculate maximum subarray sum
    const result = maxSubarraySum(arr);

    console.log(result);
}

main();

```

{% endraw %}

Maximum Subarray in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Meet Thakur

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).