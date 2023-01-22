---

title: Fibonacci in Typescript
layout: default
date: 2022-04-28
last-modified: 2023-01-22

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
    console.log(`Index: ${i}: ${elementOne}`);
  }

}

fibonacci(process.argv[2]);
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Chris Thomas

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 12 2018 11:24:37. The solution was first committed on Oct 12 2018 10:16:37. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).