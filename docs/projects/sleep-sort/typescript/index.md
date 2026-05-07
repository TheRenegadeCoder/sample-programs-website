---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- sleep-sort
- typescript
title: Sleep Sort in TypeScript
title1: Sleep Sort in
title2: TypeScript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/sleep-sort/typescript/how-to-implement-the-solution.md
- sources/programs/sleep-sort/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [TypeScript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
function printUsage(): void {
  console.log(
    'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"',
  );
  process.exit(1);
}

function sleepSort(arr: number[]): void {
  const sorted: number[] = [];

  function sleepSortHelper(item: number): void {
    setTimeout(() => {
      sorted.push(item);

      if (sorted.length === arr.length) {
        console.log(sorted.join(", "));
      }
    }, item * 1000);
  }

  arr.forEach((item) => {
    if (item < 0) {
      printUsage();
    }
    sleepSortHelper(item);
  });
}

function parseInput(input: string): number[] {
  return input
    .split(",")
    .map((s) => s.trim())
    .map((s) => Number.parseInt(s, 10));
}

function isValid(arr: number[]): boolean {
  return arr.length >= 2 && !arr.some((n) => Number.isNaN(n));
}

function main(): void {
  const input = process.argv[2];

  if (!input) {
    printUsage();
  }

  const numbers = parseInput(input);

  if (!isValid(numbers)) {
    printUsage();
  }

  sleepSort(numbers);
}

main();

```

{% endraw %}

Sleep Sort in [TypeScript](https://sampleprograms.io/languages/typescript) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).