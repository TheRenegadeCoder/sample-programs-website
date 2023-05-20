---
title: Even Odd in Javascript
layout: default
date: 2019-10-11
featured-image: even-odd-in-every-language.jpg
last-modified: 2019-10-11

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
const input = process.argv[2] != '' ? Number(process.argv[2]) : null; //coerce the input into a number, ignore empty string
if(!Number.isInteger(input)){ //if there is no input, input = undefined and the statement still prints
    console.log('Usage: please input a number');
} else {
    console.log(input%2 === 0 ? 'Even' : 'Odd');
}
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Manan Gill

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 12 2019 10:08:50. The solution was first committed on Oct 11 2019 16:27:51. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).