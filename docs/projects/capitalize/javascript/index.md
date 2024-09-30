---
authors:
- Daniel Luna
- Jeremy Grifski
date: 2019-03-31
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-26
layout: default
tags:
- capitalize
- javascript
title: Capitalize in Javascript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/javascript/how-to-implement-the-solution.md
- sources/programs/capitalize/javascript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
function capitalize(stringToCapitalize) {
    return stringToCapitalize[0].toUpperCase() + stringToCapitalize.slice(1);
}

function main() {
    if (process.argv.length == 3 && process.argv[2].length > 0) {
        let input = process.argv[2];
        console.log(capitalize(input)); 
    } else {
        console.log("Usage: please provide a string");
    }
}

main();

```

{% endraw %}

Capitalize in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Daniel Luna
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).