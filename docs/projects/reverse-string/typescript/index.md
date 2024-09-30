---
authors:
- Ray
- rzuckerm
date: 2019-10-03
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- reverse-string
- typescript
title: Reverse String in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/typescript/how-to-implement-the-solution.md
- sources/programs/reverse-string/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
let myString: string = (process.argv.length >= 3) ? process.argv[2] : "";

const reverse = (str: string) => str.split("").reverse().join("");

console.log(reverse(myString));

```

{% endraw %}

Reverse String in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Ray
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).