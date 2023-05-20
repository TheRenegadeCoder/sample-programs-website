---
title: Linear Search in Javascript
layout: default
date: 2020-10-01
featured-image: linear-search-in-every-language.jpg
last-modified: 2020-10-01

---

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
function LinSearch(arr = [], valToSearch) {
    let check = false;
    if (arr.length == 0) return check
    if(valToSearch==='') return check
    else {
        for (i = 0; i < arr.length; i++) {
            if (arr[i] == valToSearch){
                check = true
                return check
            }
        }
        return check
    }
}

sanitizeArray = (list) => {
    return list.split(',').map(e => {
       _e = parseInt(e.replace(" ",""));
       if (!_e){ throw new Error();}
       return _e;
    });
 }

const exit = () => {
     const usage = 'Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")';
     console.log(usage)
     process.exit();
 }
 
const main = (input, key) => {
    try {
        arr = sanitizeArray(input);
        arr.length < 1 || key == undefined ? exit() : console.log(LinSearch(arr, key));
    } catch(err) {
        exit();
    }
}

main(process.argv[2], process.argv[3])
```

{% endraw %}

[Linear Search](https://sampleprograms.io/projects/linear-search) in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Jeremy Grifski
- NameerWaqas
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Jan 29 2023 21:43:56. The solution was first committed on Oct 01 2020 13:30:39. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).