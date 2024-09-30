---
authors:
- Eliver L
- EliverLara
date: 2019-10-10
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2019-10-10
layout: default
tags:
- insertion-sort
- javascript
title: Insertion Sort in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/insertion-sort/javascript/how-to-implement-the-solution.md
- sources/programs/insertion-sort/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
const insertionSort =  (arr) => {
    for (let i = 1; i < arr.length; i++){
        let key = arr[i];
        let j = i - 1;
        while (j >= 0  && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    return arr;
}

sanitizeArray = (list) => {
    return list.split(',').map(e => {
       _e = parseInt(e.replace(" ",""));
       if (!_e){ throw new Error();}
       return _e;
    });
 }

 const exit = () => {
     const usage = 'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"';
     console.log(usage)
     process.exit();
 }

const main = (input) => {
    try {
        arr = sanitizeArray(input);
        arr.length <= 1 ? exit() : console.log(insertionSort(arr));
    } catch(err) {
        exit();
    }
}

main(process.argv[2])

```

{% endraw %}

Insertion Sort in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Eliver L
- EliverLara

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).