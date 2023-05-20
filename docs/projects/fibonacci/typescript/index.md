---
title: Fibonacci in Typescript
layout: default
date: 2018-10-12
featured-image: fibonacci-in-every-language.jpg
last-modified: 2018-10-12

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
function fibonacci(num: number) {

  let n = Number(num);
  let elementOne: number = 0;
  let elementTwo: number = 1;
  let result: number = 0;

  for (let i: number = 1; i <= n; i++) {
    result = elementOne + elementTwo;
    elementOne = elementTwo;
    elementTwo = result;
    console.log(`${i}: ${elementOne}`);
  }

}

let num_str = (process.argv.length >= 3) ? process.argv[2] : ""
let num: number = parseInt(num_str);
if (isNaN(num)) {
  console.log("Usage: please input the count of fibonacci numbers to output")
  process.exit(0)
}

fibonacci(num);
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Chris Thomas
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 15 2023 16:26:37. The solution was first committed on Oct 12 2018 10:16:37. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).