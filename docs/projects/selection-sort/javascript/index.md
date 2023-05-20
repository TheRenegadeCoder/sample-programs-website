---
title: Selection Sort in Javascript
layout: default
date: 2019-10-16
featured-image: selection-sort-in-every-language.jpg
last-modified: 2019-10-16

---

Welcome to the [Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
const selectionSort = (list) => {
    // Iterate through the list
    for (let i = 0; i < list.length; i++) {
        // Set a default of the first value
        let min = list[i];
        let minIdx = i;
        // Iterate through the rest of the list
        for (let j = i; j < list.length; j++) {
            if (list[j] < min) {
                // We found a new minimum
                min = list[j];
                minIdx = j;
            }
        }
        // Swap the minimum with the current index
        const temp = list[i];
        list[i] = min;
        list[minIdx] = temp;
    }
    return list
};

const exit = () => {
    console.log('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"');
    process.exit();
}

const main = (input) => {
    try {
        const arr = input.split(", ");
        arr.length <= 1 ? exit() : console.log(selectionSort(arr).join(", "));
    } catch {
        exit();
    }
}

main(process.argv[2])
```

{% endraw %}

[Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- mericleac

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).