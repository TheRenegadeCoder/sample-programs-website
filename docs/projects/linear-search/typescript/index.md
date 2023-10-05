---
authors:
- Meet Thakur
date: 2023-10-05
featured-image: linear-search-in-every-language.jpg
last-modified: 2023-10-05
layout: default
tags:
- linear-search
- typescript
title: Linear Search in Typescript
---

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

  const inputNum = parseInt(process.argv[2], 10);

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

Linear Search in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Meet Thakur

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).