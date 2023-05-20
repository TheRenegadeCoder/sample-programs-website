---
title: Josephus Problem in Javascript
layout: default
date: 2021-10-08
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2021-10-08

---

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
const josephus = (n, k) => {
    if (n == 1) return 1;
    else return ((josephus(n - 1, k) + k - 1) % n) + 1;
};

const usage =
    "Usage: please input the total number of people and number of people to skip.";

const n = parseInt(process.argv[2]);
const k = parseInt(process.argv[3]);

if (!n || !k || typeof n !== "number" || typeof k !== "number") {
    return console.log(usage);
}

console.log(josephus(n, k));
```

{% endraw %}

[Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Matteo Planchet

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).