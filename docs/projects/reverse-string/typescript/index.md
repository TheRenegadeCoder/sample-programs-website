---
title: Reverse String in Typescript
layout: default
date: 2019-10-03
featured-image: reverse-string-in-every-language.jpg
last-modified: 2019-10-03

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
let myString: string = (process.argv.length >= 3) ? process.argv[2] : "";

const reverse = (str: string) => str.split("").reverse().join("");

console.log(reverse(myString));
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Ray
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 15 2023 16:26:37. The solution was first committed on Oct 03 2019 20:46:56. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).