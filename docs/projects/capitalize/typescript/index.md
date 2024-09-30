---
authors:
- Ray
- rzuckerm
date: 2019-10-03
featured-image: capitalize-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- capitalize
- typescript
title: Capitalize in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/typescript/how-to-implement-the-solution.md
- sources/programs/capitalize/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
if (process.argv.length < 3 || process.argv[2].length < 1) {
    console.log("Usage: please provide a string")
    process.exit(0)
}

let myStr: string = process.argv[2];

const capitalize = (str: string) => str[0].toUpperCase() + str.slice(1);

console.log(capitalize(myStr));

```

{% endraw %}

Capitalize in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Ray
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).