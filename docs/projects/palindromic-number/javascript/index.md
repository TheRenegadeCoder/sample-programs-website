---
authors:
- Jeremy Grifski
- smjalageri
date: 2021-11-01
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2022-10-11
layout: default
tags:
- javascript
- palindromic-number
title: Palindromic Number in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/javascript/how-to-implement-the-solution.md
- sources/programs/palindromic-number/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
const isPalindromic = (number) => {
    if (number <= 1) {
        console.log("Usage: please input a non-negative integer");
        process.exit(1);
    }

    let reverse_number = 0, temp = number;
    while (temp > 0) {
        reverse_number = (reverse_number * 10) + (temp % 10);
        temp = Math.floor(temp / 10);
    }

    if (reverse_number == number)
        return true;
    else
        return false;

};

const input = process.argv[2];
let number = Number(input)

if (input !== '' && Number.isInteger(number) && number >= 0) {
    isPalindromic(input) ? console.log("true") : console.log("false");
} else {
    console.log("Usage: please input a non-negative integer")
}

```

{% endraw %}

Palindromic Number in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Jeremy Grifski
- smjalageri

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).