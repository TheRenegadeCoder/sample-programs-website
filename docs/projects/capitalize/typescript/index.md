---
title: Capitalize in Typescript
layout: default
date: 2019-10-03
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-03

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
if (process.argv.length < 3 || process.argv[2].length < 1) {
    console.log("Usage: please provide a string")
    process.exit(0)
}

let myStr: string = process.argv[2];

const capitalize = (str: string) => str[0].toUpperCase() + str.slice(1);

console.log(capitalize(myStr));
```

{% endraw %}

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Ray
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 15 2023 16:26:37. The solution was first committed on Oct 03 2019 20:58:01. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).