---

title: Capitalize in Javascript
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Capitalize in Javascript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Javascript
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).