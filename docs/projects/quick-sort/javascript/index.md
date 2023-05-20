---
title: Quick Sort in Javascript
layout: default
date: 2019-10-16
featured-image: quick-sort-in-every-language.jpg
last-modified: 2019-10-16

---

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
/**
 * Quick sort algorithm
 *
 * @param {Integer array} arr
 */

const quickSort = (arr, start, end) => {
  if(start < end) {
    let pivot = partition(arr, start, end)
    quickSort(arr, start, pivot - 1)
    quickSort(arr, pivot + 1, end)
  } 
}

const partition = (arr, start, end) => { 
  let pivot = end
  let i = start - 1
  let j = start
  while (j < pivot) {
    if (arr[j] > arr[pivot]) {
      j++
    } else {
      i++
      swap(arr, j, i)
      j++
    }
  }
  swap(arr, i + 1, pivot)
  return i + 1
}

const swap = (arr, first, second) => {
  let temp = arr[first]
  arr[first] = arr[second]
  arr[second] = temp
}

const main = (input) => {
    /**
     * If the string matches the format `"[number], [number], (... [number])"`,
     * we have a valid input.
     */
    const inputValidation = /^"?(\d+,\s*){2,}\d+(,"?|"?)$/gm;

    if (inputValidation.test(input) == true) {
        // valid input
        let arr;

        /**
         * Format string to be quicksorted.
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

        // apply quicksort and output result
        quickSort(arr, 0, arr.length - 1)
        console.log(arr)
    }
    else {
        // invalid input
        console.log(usage);
    }
}

const usage = `Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"`;

if (process.argv.length > 2) {
    const input = process.argv[2];
    main(input);
}
else {
    console.log(usage);
}
```

{% endraw %}

[Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Gurmeet
- Gurmeet Singh

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 18 2019 23:18:28. The solution was first committed on Oct 16 2019 15:49:03. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).