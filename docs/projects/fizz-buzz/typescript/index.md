---
title: Fizz Buzz in Typescript
layout: default
date: 2018-10-11
featured-image: fizz-buzz-in-every-language.png
last-modified: 2018-10-11

---

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

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Nadir Fayazov
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 15 2023 16:26:37. The solution was first committed on Oct 11 2018 20:07:08. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).