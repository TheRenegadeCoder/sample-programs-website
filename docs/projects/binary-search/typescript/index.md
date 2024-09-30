---
authors:
- Vipin Yadav
date: 2023-10-07
featured-image: binary-search-in-every-language.jpg
last-modified: 2023-10-07
layout: default
tags:
- binary-search
- typescript
title: Binary Search in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/typescript/how-to-implement-the-solution.md
- sources/programs/binary-search/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
const error_msg: string = "Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")";
if (process.argv.length != 4) {
    console.log(error_msg);
    process.exit(1);
}

let list_str: string = process.argv[2]
let target: number = parseInt(process.argv[3]);

if (isNaN(target) || list_str.length == 0) {
    console.log(error_msg);
    process.exit(1);
}
let list: number[] = list_str.split(",").map((x: string) => parseInt(x));
// check if list is sorted
for (let i: number = 1; i < list.length; i++) {
    if (list[i] < list[i - 1]) {
        console.log(error_msg);
        process.exit(1);
    }
}
let found: boolean = false;
let low: number = 0;
let high: number = list.length - 1;
while (low <= high) {
    let mid: number = Math.floor((low + high) / 2);
    if (list[mid] == target) {
        found = true;
        break;
    }
    if (list[mid] < target) {
        low = mid + 1;
    } else {
        high = mid - 1;
    }
}
console.log(found ? "true" : "false");
```

{% endraw %}

Binary Search in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).