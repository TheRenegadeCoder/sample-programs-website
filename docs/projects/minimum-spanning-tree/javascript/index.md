---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-06
featured-image: minimum-spanning-tree-in-every-language.jpg
last-modified: 2026-05-06
layout: default
tags:
- javascript
- minimum-spanning-tree
title: Minimum Spanning Tree in JavaScript
title1: Minimum Spanning
title2: Tree in JavaScript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/minimum-spanning-tree/javascript/how-to-implement-the-solution.md
- sources/programs/minimum-spanning-tree/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Minimum Spanning Tree](https://sampleprograms.io/projects/minimum-spanning-tree) in [JavaScript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
"use strict";

const USAGE = "Usage: please provide a comma-separated list of integers";

const solveMST = (flat, size) => {
  const keys = new Array(size).fill(Infinity);
  const inMST = new Uint8Array(size);

  keys[0] = 0;

  for (let count = 0; count < size; count++) {
    let u = -1;

    for (let v = 0; v < size; v++) {
      if (!inMST[v] && (u === -1 || keys[v] < keys[u])) {
        u = v;
      }
    }

    if (u === -1 || keys[u] === Infinity) break;

    inMST[u] = 1;

    const rowOffset = u * size;
    for (let v = 0; v < size; v++) {
      const weight = flat[rowOffset + v];
      if (weight > 0 && !inMST[v] && weight < keys[v]) {
        keys[v] = weight;
      }
    }
  }

  return keys.reduce((sum, w) => (w === Infinity ? sum : sum + w), 0);
};

const run = () => {
  const [, , input] = process.argv;

  if (!input) {
    console.error(USAGE);
    process.exit(1);
  }

  try {
    const flat = input
      .split(",")
      .filter((x) => x.trim() !== "")
      .map((x) => {
        const val = Number(x);
        if (!Number.isInteger(val)) throw new Error();
        return val;
      });

    const size = Math.sqrt(flat.length);

    if (flat.length === 0 || !Number.isInteger(size)) {
      throw new Error();
    }

    const result = solveMST(flat, size);
    console.log(result);
  } catch {
    console.error(USAGE);
    process.exit(1);
  }
};

run();

```

{% endraw %}

Minimum Spanning Tree in [JavaScript](https://sampleprograms.io/languages/javascript) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).