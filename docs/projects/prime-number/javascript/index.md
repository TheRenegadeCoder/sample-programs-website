---

title: Prime Number in Javascript
layout: default
date: 2022-04-28
last-modified: 2022-11-27

---

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
const isPrime = (number) => {
    if(number <= 1)
      return false

    for (let i = 2; i <= Math.sqrt(number); i++) {
      if (number % i == 0) {
        return false;
      }
    }
    return number > 1;
  };
  
  const input = process.argv[2];
  let number = Number(input)
  
  if (input !== '' && Number.isInteger(number) && number >= 0) {
    isPrime(input) ? console.log("prime") : console.log("composite");
  } else {
    console.log("Usage: please input a non-negative integer")
  }
```

{% endraw %}

[Prime Number](https://sampleprograms.io/projects/prime-number) in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Ganesh Naik
- Jayden Thrasher

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 03 2020 23:29:26. The solution was first committed on Oct 05 2019 14:01:08. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).