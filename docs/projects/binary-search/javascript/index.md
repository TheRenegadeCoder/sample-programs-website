---

---

Welcome to the Binary Search in Javascript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Javascript
const [, , array, target] = process.argv;
const error = 'Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")';

const binarySearch = (array, target, start = 0, end = array.length - 1) => {

  const isOrdered = array.every((num, i, arr) => !i || num >= arr[i - 1]);
  if (!isOrdered) return error;

  const middleIndex = Math.floor((start + end) / 2);
  const middleValue = array[middleIndex];
  const newIndexes =
    target < middleValue ? [start, middleIndex - 1] : [middleIndex + 1, end];

  return middleValue === target
    ? true
    : start >= end
        ? false
        : binarySearch(array, target, ...newIndexes);
};

console.log(array && target ? binarySearch(array.split(', '), target) : error);

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.