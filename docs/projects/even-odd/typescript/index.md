---
authors:
- Vipin Yadav
date: 2023-10-02
featured-image: even-odd-in-every-language.jpg
last-modified: 2023-10-02
layout: default
tags:
- even-odd
- typescript
title: Even Odd in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/typescript/how-to-implement-the-solution.md
- sources/programs/even-odd/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
const error_msg: string = "Usage: please input a number"
let num_str:string = (process.argv.length == 3) ? process.argv[2] : "";
let num:number = parseInt(num_str);
if (isNaN(num)) {
    console.log(error_msg);
    process.exit(1);
}
let is_even:boolean = (num % 2 == 0);
console.log(is_even ? "Even" : "Odd");
```

{% endraw %}

Even Odd in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).