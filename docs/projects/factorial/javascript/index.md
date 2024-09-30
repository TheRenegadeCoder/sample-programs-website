---
authors:
- Bharath
- Matt Wiley
date: 2019-10-10
featured-image: factorial-in-every-language.jpg
last-modified: 2019-10-16
layout: default
tags:
- factorial
- javascript
title: Factorial in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/javascript/how-to-implement-the-solution.md
- sources/programs/factorial/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
/**
 * Calculate the factorial of a given integer input.
 * 
 * @param {Integer} num 
 */
function factorial(num) {
    let product = 1;
    if ( num > 1 ) {
        for ( let i = 2; i <= num; i++ ) {
            product *= i
        }
    }
    return product
}

/**
 * Executable function
 * 
 * @param {Command line input} input 
 */
function main(input) {
    // Usage text
    const usage = 'Usage: please input a non-negative integer';

    // No input
    if ( !input ) {
        console.log(usage)
        return
    }

    /**
     * If we remove all the integer characters from the input and are left with
     * an empty string, then we have a valid integer.
     */
    const inputValidation = input.replace(/[0-9]/g,'')
    
    if ( inputValidation === '' ) {
        // Valid integer
        const parsedInput = parseInt(input)
        if ( parsedInput < 0 ) {
            console.log(usage)
        }
        else if ( parsedInput > 170 ) {
            console.log(`Input of ${parsedInput} is too large to calculate a factorial for. Max input is 170.`)
        }
        else {
            console.log(factorial(parsedInput))
        }
    }
    else {
        // Anything non integer
        console.log(usage)
    }
    
}

// Run the executable function
const input = process.argv[2]
main(input)
```

{% endraw %}

Factorial in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Bharath
- Matt Wiley

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).