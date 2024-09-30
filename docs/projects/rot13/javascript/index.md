---
authors:
- mericleac
date: 2019-10-22
featured-image: rot13-in-every-language.jpg
last-modified: 2019-10-22
layout: default
tags:
- javascript
- rot13
title: Rot13 in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/javascript/how-to-implement-the-solution.md
- sources/programs/rot13/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
const lower = "abcdefghijklmnopqrstuvwxyz";
const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

const rotateChar = (char) => {
    if (lower.includes(char)) {
        const newIdx = (lower.indexOf(char) + 13) % lower.length;
        return lower[newIdx];
    }
    if (upper.includes(char)) {
        const newIdx = (upper.indexOf(char) + 13) % upper.length;
        return upper[newIdx];
    }
    return char;
}

const rotate13 = (string) => {
    const stringArray = string.split("");
    const rotatedBy13 = stringArray.map((char) => rotateChar(char));
    return rotatedBy13.join("");
}

const exit = () => {
    console.log('Usage: please provide a string to encrypt');
    process.exit();
}

const main = (input) => {
    try {
        input.length > 0 ? console.log(rotate13(input)): exit();
    } catch {
        exit();
    }
}

main(process.argv[2]);

```

{% endraw %}

Rot13 in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- mericleac

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).