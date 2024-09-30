---
authors:
- Meet Thakur
- rzuckerm
date: 2023-10-05
featured-image: prime-number-in-every-language.jpg
last-modified: 2023-10-21
layout: default
tags:
- prime-number
- typescript
title: Prime Number in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/typescript/how-to-implement-the-solution.md
- sources/programs/prime-number/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
function isPrime(num: number): boolean {
  if (num < 2) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}

function main() {
  if (process.argv.length !== 3) {
    console.log('Usage: please input a non-negative integer');
    return;
  }

  const inputNum = parseFloat(process.argv[2]);

  if (isNaN(inputNum) || inputNum < 0 || inputNum % 1 !== 0) {
    console.log('Usage: please input a non-negative integer');
    return;
  }

  if (isPrime(inputNum)) {
    console.log('prime');
  } else {
    console.log('composite');
  }
}
main();

```

{% endraw %}

Prime Number in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Meet Thakur
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).