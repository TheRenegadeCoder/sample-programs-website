---

title: Fizz Buzz in Typescript
layout: default
date: 2022-04-28
last-modified: 2022-06-12

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
let line: string;

for (let i = 0; i <= 100; i++) {
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

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).