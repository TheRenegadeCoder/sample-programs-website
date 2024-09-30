---
authors:
- Antonino Bertulla
date: 2023-10-04
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2023-10-04
layout: default
tags:
- roman-numeral
- typescript
title: Roman Numeral in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/typescript/how-to-implement-the-solution.md
- sources/programs/roman-numeral/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
// Roman Numeral Conversion

const romanNumeralValues = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000
};

function romanNumeralConversion(str?: string) {

  // Check for blank input
  if (str === undefined) {
    return "Usage: please provide a string of roman numerals";
  }

  // Check for empty string
  if (str === "") {
    return 0;
  }

  // Get valid characters
  const validValues = Object.keys(romanNumeralValues)

  // Check for invalid characters
  for (let i = 0; i < str.length; i++) {
    const char = str.charAt(i)
    if (char === undefined || validValues.indexOf(char) === -1) {
      return "Error: invalid string of roman numerals";
    }
  }

  // Calculating result (adding/subtracting)
  // 
  // Note: next will be undefined for the last element, it'll
  // still work though since 'any number' < undefined will
  // be false ... hacky - but works!
  //
  // Note 2: This does not account for wrongly formatted
  // Roman Numerals like IIIIIIIIIX

  let answer = 0;
  for (let i = 0; i < str.length; i++) {
    const curr = romanNumeralValues[str.charAt(i)];
    const next = romanNumeralValues[str.charAt(i+1)];
    if (curr < next) {
      answer -= curr;
    } else {
      answer += curr;
    }
  }

  return answer;
}


// CLI use needs to have node.js installed
// Run like so:
//   node roman-numeral.js IIIIIIXXVXIV


// Process arguments from CLI
const args = process.argv.slice(2);

if (args.length < 1) {
  console.error("Usage: please provide a string of roman numerals");
} else {
  console.info(romanNumeralConversion(args[0]))
}


```

{% endraw %}

Roman Numeral in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Antonino Bertulla

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).