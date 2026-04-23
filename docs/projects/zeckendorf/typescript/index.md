---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-04-24
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-04-24
layout: default
tags:
- typescript
- zeckendorf
title: Zeckendorf in TypeScript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/typescript/how-to-implement-the-solution.md
- sources/programs/zeckendorf/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [TypeScript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
const arg = process.argv[2];

if (process.argv.length !== 3 || !/^\d+$/.test(arg)) {
    console.log("Usage: please input a non-negative integer");
    process.exit(0);
}

let n = parseInt(arg, 10);

if (n === 0) {
    console.log("");
    process.exit(0);
}

let a = 1;
let b = 2;

while (b <= n) {
    [a, b] = [b, a + b];
}

const result: number[] = [];

while (n > 0 && a > 0) {
    if (a <= n) {
        result.push(a);
        n -= a;

        let prevA = b - a;
        let prevPrevA = a - prevA;
        [a, b] = [prevPrevA, prevA];
    } else {
        let prevA = b - a;
        [a, b] = [prevA, a];
    }
}

console.log(result.join(", "));
```

{% endraw %}

Zeckendorf in [TypeScript](https://sampleprograms.io/languages/typescript) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).