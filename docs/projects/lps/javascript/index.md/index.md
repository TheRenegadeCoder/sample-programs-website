---

---

# Lps in Javascript

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.