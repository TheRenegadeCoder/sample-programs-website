---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- maximum-array-rotation
- typescript
title: Maximum Array Rotation in TypeScript
title1: Maximum Array Rotation
title2: in TypeScript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/typescript/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [TypeScript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
function printUsage(): void {
  console.error('Usage: please provide a list of integers (e.g. "8, 3, 1, 2")');
  process.exit(1);
}

function parse(input: string): number[] {
  return input
    .split(",")
    .map((s) => s.trim())
    .filter((s) => s.length > 0)
    .map((s) => Number(s));
}

function maxArrayRotation(arr: number[]): number {
  const n = arr.length;
  if (n === 0) return 0;

  let totalSum = 0;
  let currentSum = 0;

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
}

function main(): void {
  const input = process.argv[2];

  if (!input) {
    printUsage();
  }

  const arr = parse(input);

  if (arr.length === 0 || arr.some((n) => Number.isNaN(n))) {
    printUsage();
  }

  console.log(maxArrayRotation(arr));
}

main();

```

{% endraw %}

Maximum Array Rotation in [TypeScript](https://sampleprograms.io/languages/typescript) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).