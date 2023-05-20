---
title: Palindromic Number in Javascript
layout: default
date: 2021-11-01
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2021-11-01

---

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
const isPalindromic = (number) => {
    if (number <= 1) {
        console.log("Usage: please input a non-negative integer");
        process.exit(1);
    }

    let reverse_number = 0, temp = number;
    while (temp > 0) {
        reverse_number = (reverse_number * 10) + (temp % 10);
        temp = Math.floor(temp / 10);
    }

    if (reverse_number == number)
        return true;
    else
        return false;

};

const input = process.argv[2];
let number = Number(input)

if (input !== '' && Number.isInteger(number) && number >= 0) {
    isPalindromic(input) ? console.log("true") : console.log("false");
} else {
    console.log("Usage: please input a non-negative integer")
}
```

{% endraw %}

[Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Jeremy Grifski
- smjalageri

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 11 2022 01:31:51. The solution was first committed on Nov 01 2021 09:28:10. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).