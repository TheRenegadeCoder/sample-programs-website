---

title: Selection Sort in Javascript
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Selection Sort in Javascript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Javascript
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.