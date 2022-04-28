# Fibonacci in Javascript

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Javascript
function fibonacci(num) {
    let n = Number(num);
    let first = 0;
    let second = 1;
    let result = 0;
    for (let i = 1; i <= n; i++) {
    	result = first + second;
    	first = second;
    	second = result;
        console.log(i + ": " + first);
    }
}

num = process.argv[2];

if (num && !isNaN(num)) {
    fibonacci(num);
} else {
    console.log("Usage: please input the count of fibonacci numbers to output")
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.