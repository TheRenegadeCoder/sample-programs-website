---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- josephus-problem
- typescript
title: Josephus Problem in TypeScript
title1: Josephus Problem
title2: in TypeScript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/typescript/how-to-implement-the-solution.md
- sources/programs/josephus-problem/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [TypeScript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
function printUsage(): void {
  console.error(
    "Usage: please input the total number of people and number of people to skip.",
  );
  process.exit(1);
}

function josephus(n: number, k: number): number {
  if (n === 1) return 1;
  return ((josephus(n - 1, k) + k - 1) % n) + 1;
}

function main(): void {
  const n = Number.parseInt(process.argv[2], 10);
  const k = Number.parseInt(process.argv[3], 10);

  if (Number.isNaN(n) || Number.isNaN(k) || n <= 0 || k <= 0) {
    printUsage();
  }

  console.log(josephus(n, k).toString());
}

main();

```

{% endraw %}

Josephus Problem in [TypeScript](https://sampleprograms.io/languages/typescript) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).