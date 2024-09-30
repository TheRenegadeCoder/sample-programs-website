---
authors:
- Nadir Fayazov
- rzuckerm
date: 2018-10-11
featured-image: fizz-buzz-in-every-language.png
last-modified: 2023-05-15
layout: default
tags:
- fizz-buzz
- typescript
title: Fizz Buzz in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/typescript/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
let line: string;

for (let i = 1; i <= 100; i++) {
   if (i % 3 == 0 && i % 5 == 0) {
      line = "FizzBuzz";
   } else if (i % 3 == 0) {
      line = "Fizz";
   } else if (i % 5 == 0) {
      line = "Buzz";
   } else {
      line = String(i);
   }
   console.log(line);
}

```

{% endraw %}

Fizz Buzz in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Nadir Fayazov
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).