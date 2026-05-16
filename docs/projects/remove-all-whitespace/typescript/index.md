---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- remove-all-whitespace
- typescript
title: Remove All Whitespace in TypeScript
title1: Remove All Whitespace
title2: in TypeScript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/typescript/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [TypeScript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
function printUsage(): void {
  console.log("Usage: please provide a string");
  process.exit(1);
}

function main(): void {
  const input = process.argv[2];

  if (process.argv.length !== 3 || !input || input.length === 0) {
    printUsage();
  }

  const result = input.replace(/\s/g, "");
  console.log(result);
}

main();

```

{% endraw %}

Remove All Whitespace in [TypeScript](https://sampleprograms.io/languages/typescript) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).