---

title: Even Odd in Javascript
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Even Odd in Javascript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).