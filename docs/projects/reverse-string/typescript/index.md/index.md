# Reverse String in Typescript

## Solution

```Typescript
let myString: string = "Hello World";

const reverse = ( str: string = "no string was provided" ) => str.split("").reverse().join("");

console.log(reverse(myString));

```