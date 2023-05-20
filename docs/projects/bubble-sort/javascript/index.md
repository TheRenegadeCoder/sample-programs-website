---
title: Bubble Sort in Javascript
layout: default
date: 2019-10-12
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2019-10-12

---

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
/**
 * Bubble sort algorithm
 *
 * @param {Integer array} arr
 */

function bubblesort(arr) {
    let swap;

    // repeat while array is unsorted
    do {
        swap = false;

        // iterate array
        for (let index = 0; index < arr.length - 1; index++) {
            // if current item is out of order
            if (arr[index] > arr[index + 1]) {
                // hotswap the current element with the next element
                [arr[index], arr[index + 1]] = [arr[index + 1], arr[index]];

                // flag that list was unordered in this pass
                swap = true;
            }
        }

    } while (swap);

    return arr;
}

/**
 * Executable function
 * 
 * @param {Command line input} input
 */

function main(input) {
    /**
     * If the string matches the format `"[number], [number], (... [number])"`,
     * we have a valid input.
     */
    const inputValidation = /^"?(\d+,\s*){2,}\d+(,"?|"?)$/gm;

    if (inputValidation.test(input) == true) {
        // valid input
        let arr;

        /**
         * Format string to be bubblesorted.
         *  - strip all whitespace and quotations
         *  - split into array at ',' character
         *  - convert all elements to integers
         *  - filter out NaN elements (uncaught text characters or empty elements)
         */
        arr = input.replace(/(\s|"|'|`)/g, '');
        arr = arr.split(',');
        arr = arr.map(function (n) {
            return parseInt(n, 10);
        });
        arr = arr.filter(n => n);

        // apply bubblesort and output result
        arr = bubblesort(arr);

        let str;

        str = arr.toString();
        str = str.replace(/,/g, ', ');

        console.log(str);
    }
    else {
        // invalid input
        console.log(usage);
    }
}

// usage text
const usage = `Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"`;

if (process.argv.length > 2) {
    // run the executable function
    const input = process.argv[2];
    main(input);
}
else {
    console.log(usage);
}
```

{% endraw %}

[Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Zachary Smith

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 17 2019 12:47:05. The solution was first committed on Oct 12 2019 16:23:29. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).