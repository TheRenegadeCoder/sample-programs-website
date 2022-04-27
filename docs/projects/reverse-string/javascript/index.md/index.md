# Reverse String in Javascript

## Solution

```Javascript
const reverse = s => s.split('').reverse().join('');

console.log(reverse(process.argv[2]));

```