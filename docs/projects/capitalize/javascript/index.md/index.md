---

---

# Capitalize in Javascript

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.