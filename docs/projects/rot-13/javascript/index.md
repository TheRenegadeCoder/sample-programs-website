---

---

Welcome to the Rot 13 in Javascript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Javascript
const lower = "abcdefghijklmnopqrstuvwxyz";
const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

const rotateChar = (char) => {
    if (lower.includes(char)) {
        const newIdx = (lower.indexOf(char) + 13) % lower.length;
        return lower[newIdx];
    }
    if (upper.includes(char)) {
        const newIdx = (upper.indexOf(char) + 13) % upper.length;
        return upper[newIdx];
    }
    return char;
}

const rotate13 = (string) => {
    const stringArray = string.split("");
    const rotatedBy13 = stringArray.map((char) => rotateChar(char));
    return rotatedBy13.join("");
}

const exit = () => {
    console.log('Usage: please provide a string to encrypt');
    process.exit();
}

const main = (input) => {
    try {
        input.length > 0 ? console.log(rotate13(input)): exit();
    } catch {
        exit();
    }
}

main(process.argv[2]);

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.