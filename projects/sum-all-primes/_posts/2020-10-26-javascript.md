---
title: Sum All Primes in JavaScript
layout: default
date: 2020-10-26
last-modified: 2020-10-26
featured-image:
tags: [sum-all-primes, javascript]
authors:
    - barhouum7
---


In this article, we will writing a program to return the sum of all prime numbers that are less than or equal to a given number in JavaScript.



## How to Implement the Solution

Let's look at the code in detail:

code for [sum-all-primes.js](https://github.com/TheRenegadeCoder/sample-programs/blob/master/archive/j/javascript/sum-all-primes.js):

```javascript
function sumPrimes(num) {
    let i = 1
    let sum = 0
    while (i <= num) {
      if (isPrime(i)) {
        sum += i
      }
      i++
    }
    return sum
  }
  //function to check if a number is prime or not
  function isPrime(x) {
    for (let i = 2; i < x; i++) {
      if (x % i === 0) return false
    }
    return x !== 1 && x !== 0
  }
  //test here
  console.log(sumPrimes(10))
```

## How to Run Solution

If you want to run this program, you can download a copy of [sum-all-primes.js](https://github.com/TheRenegadeCoder/sample-programs/blob/master/archive/j/javascript/sum-all-primes.js).

Next, open it on your text editor, then you could show the result on your console.

Alternatively, copy the solution into an online [JavaScript Interpreter](https://repl.it/languages/javascript) and hit run.

## Further Reading

- Fill out as needed
