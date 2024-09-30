---
authors:
- Meet Thakur
date: 2023-10-01
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2023-10-01
layout: default
tags:
- palindromic-number
- typescript
title: Palindromic Number in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/typescript/how-to-implement-the-solution.md
- sources/programs/palindromic-number/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
function isPalindrome(num: number): boolean {
    const numStr = num.toString();
    const reversedNumStr = numStr.split('').reverse().join('');
    return numStr === reversedNumStr;
}

if (process.argv.length !== 3) {
    console.log("Usage: please input a non-negative integer");
} else {
    const input = process.argv[2];
    const numberToCheck = parseFloat(input);

    if (!isNaN(numberToCheck) && Number.isInteger(numberToCheck) && numberToCheck >= 0) {
        if (isPalindrome(numberToCheck)) {
            console.log("true");
        } else {
            console.log("false");
        }
    } else {
        console.log("Usage: please input a non-negative integer");
    }
}

```

{% endraw %}

Palindromic Number in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Meet Thakur

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).