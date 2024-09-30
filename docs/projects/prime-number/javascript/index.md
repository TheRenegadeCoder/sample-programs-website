---
authors:
- Ganesh Naik
- Jayden Thrasher
date: 2019-10-05
featured-image: prime-number-in-every-language.jpg
last-modified: 2020-10-03
layout: default
tags:
- javascript
- prime-number
title: Prime Number in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/javascript/how-to-implement-the-solution.md
- sources/programs/prime-number/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
const isPrime = (number) => {
    if(number <= 1)
      return false

    for (let i = 2; i <= Math.sqrt(number); i++) {
      if (number % i == 0) {
        return false;
      }
    }
    return number > 1;
  };
  
  const input = process.argv[2];
  let number = Number(input)
  
  if (input !== '' && Number.isInteger(number) && number >= 0) {
    isPrime(input) ? console.log("prime") : console.log("composite");
  } else {
    console.log("Usage: please input a non-negative integer")
  }

```

{% endraw %}

Prime Number in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Ganesh Naik
- Jayden Thrasher

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).