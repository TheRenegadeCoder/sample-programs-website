---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-06
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2026-05-06
layout: default
tags:
- duplicate-character-counter
- javascript
title: Duplicate Character Counter in JavaScript
title1: Duplicate Character
title2: Counter in JavaScript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/javascript/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [JavaScript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
"use strict";

const USAGE = "Usage: please provide a string";

const isAlphaNum = (c) => /^[a-z0-9]$/i.test(c);

const countDuplicates = (str) => {
  const counts = new Map();

  for (const ch of str) {
    if (isAlphaNum(ch)) {
      counts.set(ch, (counts.get(ch) ?? 0) + 1);
    }
  }

  const duplicates = [];

  for (const [ch, count] of counts) {
    if (count > 1) {
      duplicates.push(`${ch}: ${count}`);
    }
  }

  return duplicates.length > 0
    ? duplicates.join("\n")
    : "No duplicate characters";
};

const run = () => {
  const [, , input] = process.argv;

  if (!input) {
    console.error(USAGE);
    process.exit(1);
  }

  console.log(countDuplicates(input));
};

run();

```

{% endraw %}

Duplicate Character Counter in [JavaScript](https://sampleprograms.io/languages/javascript) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).