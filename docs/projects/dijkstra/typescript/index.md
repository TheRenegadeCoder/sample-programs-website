---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: dijkstra-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- dijkstra
- typescript
title: Dijkstra in TypeScript
title1: Dijkstra in
title2: TypeScript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/dijkstra/typescript/how-to-implement-the-solution.md
- sources/programs/dijkstra/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Dijkstra](https://sampleprograms.io/projects/dijkstra) in [TypeScript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
function printUsage(): void {
  console.log(
    "Usage: please provide three inputs: a serialized matrix, a source node and a destination node",
  );
}

function parseList(input: string | undefined): number[] | null {
  if (input === undefined) return null;
  if (input.trim() === "") return [];

  const parts = input.split(",").map((s) => s.trim());
  const nums: number[] = [];

  for (const p of parts) {
    if (!/^-?\d+$/.test(p)) return null;
    nums.push(Number(p));
  }

  return nums;
}

function buildMatrix(flat: number[]): number[][] | null {
  const n = Math.sqrt(flat.length);
  if ((n | 0) !== n) return null;

  const size = n | 0;
  const matrix: number[][] = new Array(size);

  for (let i = 0; i < size; i++) {
    const row: number[] = new Array(size);
    for (let j = 0; j < size; j++) {
      row[j] = flat[i * size + j];
    }
    matrix[i] = row;
  }

  return matrix;
}

function dijkstra(matrix: number[][], src: number, dst: number): number {
  const n = matrix.length;
  const dist = new Array(n).fill(Infinity);
  const visited = new Array(n).fill(false);

  dist[src] = 0;

  for (let i = 0; i < n; i++) {
    let u = -1;

    for (let j = 0; j < n; j++) {
      if (!visited[j] && (u === -1 || dist[j] < dist[u])) {
        u = j;
      }
    }

    if (u === -1 || dist[u] === Infinity) break;
    visited[u] = true;

    const row = matrix[u];
    const du = dist[u];

    for (let v = 0; v < n; v++) {
      const w = row[v];
      if (w > 0 && !visited[v]) {
        const alt = du + w;
        if (alt < dist[v]) dist[v] = alt;
      }
    }
  }

  return dist[dst] === Infinity ? -1 : dist[dst];
}

function main(): void {
  const [, , matrixStr, srcStr, dstStr] = process.argv;
  const flat = parseList(matrixStr);
  const srcArr = parseList(srcStr);
  const dstArr = parseList(dstStr);

  if (
    flat === null ||
    srcArr === null ||
    dstArr === null ||
    srcArr.length !== 1 ||
    dstArr.length !== 1
  ) {
    printUsage();
    return;
  }

  if (flat.length === 0) {
    printUsage();
    return;
  }

  const src = srcArr[0];
  const dst = dstArr[0];
  
  const matrix = buildMatrix(flat);
  if (!matrix) {
    printUsage();
    return;
  }

  const n = matrix.length;

  if (src < 0 || dst < 0 || src >= n || dst >= n) {
    printUsage();
    return;
  }

  for (const row of matrix) {
    for (const w of row) {
      if (w < 0) {
        printUsage();
        return;
      }
    }
  }

  const result = dijkstra(matrix, src, dst);
  if (result < 0) {
    printUsage();
    return;
  }

  console.log(result.toString());
}

main();

```

{% endraw %}

Dijkstra in [TypeScript](https://sampleprograms.io/languages/typescript) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).