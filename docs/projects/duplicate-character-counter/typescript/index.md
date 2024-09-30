---
authors:
- Vipin Yadav
date: 2023-10-02
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2023-10-02
layout: default
tags:
- duplicate-character-counter
- typescript
title: Duplicate Character Counter in Typescript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/typescript/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/typescript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Typescript](https://sampleprograms.io/languages/typescript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```typescript
const error_msg: string = "Usage: please provide a string"
let str: string = (process.argv.length == 3) ? process.argv[2] : "";
if (str.length == 0) {
    console.log(error_msg);
    process.exit(1);
}

let hash_map: Map<string, number> = new Map<string, number>();
for (let i = 0; i < str.length; i++) {
    let char: string = str[i];
    let count: number = hash_map.get(char) || 0;
    hash_map.set(char, count + 1);
}
let has_duplicate: boolean = false;
hash_map.forEach((value, key) => {
    if (value > 1) {
        has_duplicate = true;
        console.log(`${key}: ${value}`);
    }
});

if (!has_duplicate) {
    console.log("No duplicate characters");
}

```

{% endraw %}

Duplicate Character Counter in [Typescript](https://sampleprograms.io/languages/typescript) was written by:

- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).