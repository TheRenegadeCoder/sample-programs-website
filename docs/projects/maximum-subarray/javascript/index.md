---
authors:
- Meet Thakur
date: 2025-10-12
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2025-10-12
layout: default
tags:
- javascript
- maximum-subarray
title: Maximum Subarray in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/javascript/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
function printUsage() {
  console.log(
    'Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"',
  );
}

function maxSubarraySum(arr) {
  let maxSoFar = -Infinity;
  let maxEndingHere = 0;

  for (let num of arr) {
    maxEndingHere += num;

    if (maxSoFar < maxEndingHere) {
      maxSoFar = maxEndingHere;
    }

    if (maxEndingHere < 0) {
      maxEndingHere = 0;
    }
  }

  return maxSoFar;
}

function main() {
  const args = process.argv.slice(2);

  if (args.length < 1 || args[0] === "") {
    printUsage();
    process.exit(1);
  }
  const input = args[0];
  const arr = input.split(",").map((token) => parseInt(token.trim(), 10));

  if (arr.length === 1) {
    console.log(arr[0]);
    return;
  } else if (arr.length === 0) {
    printUsage();
    process.exit(1);
  }
  const result = maxSubarraySum(arr);

  console.log(result);
}

main();

```

{% endraw %}

Maximum Subarray in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Meet Thakur

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).