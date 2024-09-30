---
authors:
- izexi
date: 2020-10-17
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2020-10-26
layout: default
tags:
- javascript
- longest-palindromic-substring
title: Longest Palindromic Substring in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/javascript/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
const [, , input] = process.argv;

const getLongestPalindromic = (string) => {
  if (!string) return;

  let longestPal = '';

  for (let i = 1; i < string.length; i++) {
    for (let j = 0; j < string.length - i; j++) {
      let possiblePal = string.substring(j, j + i + 1).toLowerCase();

      if (
        possiblePal === [...possiblePal].reverse().join('') &&
        possiblePal.length > longestPal.length
      )
        longestPal = possiblePal;
    }
  }

  return longestPal;
};

console.log(
  getLongestPalindromic(input) ||
    'Usage: please provide a string that contains at least one palindrome'
);
```

{% endraw %}

Longest Palindromic Substring in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- izexi

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).