---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: longest-common-subsequence-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- longest-common-subsequence
- typescript
title: Longest Common Subsequence in TypeScript
title1: Longest Common Subsequence
title2: in TypeScript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-common-subsequence/typescript/how-to-implement-the-solution.md
- sources/programs/longest-common-subsequence/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Common Subsequence](https://sampleprograms.io/projects/longest-common-subsequence) in [TypeScript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
"use strict";

function printUsage(): void {
  console.error(
    'Usage: please provide two lists in the format "1, 2, 3, 4, 5"',
  );
  process.exit(1);
}

function parseInput(input: string | undefined): number[] | null {
  if (!input || input.trim() === "") return null;

  const parts = input.split(",").map((s) => s.trim());
  const arr: number[] = [];

  for (const p of parts) {
    if (p === "") return null;

    const val = Number.parseInt(p, 10);
    if (Number.isNaN(val)) return null;

    arr.push(val);
  }

  return arr;
}

function lcs(arr1: number[], arr2: number[]): void {
  const n = arr1.length;
  const m = arr2.length;

  const dp: number[][] = Array.from({ length: n + 1 }, () =>
    Array(m + 1).fill(0),
  );

  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= m; j++) {
      if (arr1[i - 1] === arr2[j - 1]) {
        dp[i][j] = 1 + dp[i - 1][j - 1];
      } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }

  const result: number[] = [];
  let i = n;
  let j = m;

  while (i > 0 && j > 0) {
    if (arr1[i - 1] === arr2[j - 1]) {
      result.push(arr1[i - 1]);
      i--;
      j--;
    } else if (dp[i - 1][j] >= dp[i][j - 1]) {
      i--;
    } else {
      j--;
    }
  }

  result.reverse();
  console.log(result.join(", "));
}

function main(): void {
  const input1 = process.argv[2];
  const input2 = process.argv[3];

  const arr1 = parseInput(input1);
  const arr2 = parseInput(input2);

  if (!arr1 || !arr2) {
    printUsage();
  }

  lcs(arr1!, arr2!);
}

main();

```

{% endraw %}

Longest Common Subsequence in [TypeScript](https://sampleprograms.io/languages/typescript) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).