# Prime Number in Javascript

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Javascript
const isPrime = (number) => {
    if(number <= 1)
      return false

    for (let i = 2; i <= Math.sqrt(number); i++) {
      if (number % i == 0) {
        return false;
      }
    }
    return number > 1;
  };
  
  const input = process.argv[2];
  let number = Number(input)
  
  if (input !== '' && Number.isInteger(number) && number >= 0) {
    isPrime(input) ? console.log("prime") : console.log("composite");
  } else {
    console.log("Usage: please input a non-negative integer")
  }

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.