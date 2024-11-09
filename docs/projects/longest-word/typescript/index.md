---
authors:
- TiaMarieG
date: 2024-11-09
featured-image: longest-word-in-every-language.jpg
last-modified: 2024-11-09
layout: default
tags:
- longest-word
- typescript
title: Longest Word in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/typescript/how-to-implement-the-solution.md
- sources/programs/longest-word/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
if (process.argv.length < 3 || process.argv[2].length < 1) {
    console.log("Usage: please provide a string")
    process.exit(0)
}

let testString: string = process.argv[2].replace(/\n|\t|\r/g, " ");

const separatedWords: string[] = testString.split(' ');

let longestWord: string = "";
let wordLength: number = 0;

for (let word of separatedWords) {
    if (word.length > longestWord.length) {
        longestWord = word;
        wordLength = word.length;
    }
}

console.log(wordLength);

```

{% endraw %}

Longest Word in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- TiaMarieG

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).