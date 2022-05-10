---

title: Josephus Problem in Javascript
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the Josephus Problem in Javascript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).