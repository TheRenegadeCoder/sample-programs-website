---

title: Lps in Javascript
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Lps in Javascript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Javascript
const [, , input] = process.argv;

const getLongestPalindromic = (string) => {
  if (!string) return;

  let longestPal = '';

  for (let i = 1; i < string.length; i++) {
    for (let j = 0; j < string.length - i; j++) {
      let possiblePal = string.substring(j, j + i + 1).toLowerCase();

      if (
        possiblePal === [...possiblePal].reverse().join('') &&
        possiblePal.length > longestPal.length
      )
        longestPal = possiblePal;
    }
  }

  return longestPal;
};

console.log(
  getLongestPalindromic(input) ||
    'Usage: please provide a string that contains at least one palindrome'
);
```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.