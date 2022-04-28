# Fibonacci in Typescript

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Typescript
function fibonacci(num: number) {

  let n = Number(num);
  let elementOne: number = 0;
  let elementTwo: number = 1;
  let result: number = 0;

  for (let i: number = 1; i <= n; i++) {
    result = elementOne + elementTwo;
    elementOne = elementTwo;
    elementTwo = result;
    console.log(`Index: ${i}: ${elementOne}`);
  }

}

fibonacci(process.argv[2]);

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.