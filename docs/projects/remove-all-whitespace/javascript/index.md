---
authors:
- Zia
date: 2025-01-12
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2025-01-12
layout: default
tags:
- javascript
- remove-all-whitespace
title: Remove All Whitespace in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/javascript/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
const die = () => {
  console.log("Usage: please provide a string");
  process.exit(1);
}

if (process.argv.length != 3) {
  die();
}

process.argv[2].length > 0
  ? console.log(process.argv[2].replace(/\s/g, ''))
  : die();

```

{% endraw %}

Remove All Whitespace in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).