---

title: Duplicate Char Counter in Javascript
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Duplicate Char Counter in Javascript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Javascript
const string = process.argv[2];
if (!string) return console.log("Please provide a string.");

chars_counter = {};

for (const char of string) {
    if (!chars_counter[char]) chars_counter[char] = 0;
    chars_counter[char] += 1;
}

for (const char_count of Object.entries(chars_counter)) {
    if (char_count[1] >= 2) {
        console.log(
            `Character: ${char_count[0]}, Occurrences: ${char_count[1]}`
        );
    }
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.