---
title: Fibonacci in JavaScript  
layout: default  
last-modified: 2020-05-02
featured-imaged: fibonacci-in-every-language.jpg
tags: [javascript, fibonacci]  
authors: [Alina1Black]

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
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

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Marius
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 07 2019 00:40:32. The solution was first committed on Oct 04 2018 13:17:58. As a result, documentation below may be outdated.

## How to Implement the Solution

Let's look at the code in detail:  

Here we have a function called `fibonacci` that takes in a numeric value as an argument that corresponds to the amount Fibonacci numbers we want to print in succession.

What `fibonacci`" does is that it starts printing from 1 then each time it just prints the accumulation of the last number it printed (stored in variable named `second`) and the 2nd last number it printed (stored in variable named `first`).

Then we have a variable named `num` which can have a numeric value of `10` since we want to print the first 10 numbers in the Fibonacci sequence. I can also have the value `process.argv[2]` so we can run the command `node fibonacci.js 10` to execute the file with NodeJS and print the first 10 numbers in the Fibonacci sequence.

Then we have a function that verifies that `num` has a positive, numeric value so we can run the function named `fibonacci`, else it just returns an instruction/warning.


## How to Run the Solution

### If you want to run this code in a browser

1. Copy/paste the code provided in a JavaScript file.
2. Give the variable `num` a value of 10 instead of `process.argv[2]`.
3. Link the script in a web page. (example given below)

For example:
If you copy/paste this code in a file named `fibonacci.js` then use copy/paste the following tag in your HTML file:

```html
<script src="fibonacci.js"></script>
```

4. Also make sure that `fibonacci.js` is in the same folder/directory as your HTML file.
5. Just open the webpage in a web browser and look at it's console. The output will be there.

### If you want to run this code with NodeJS

1. Make sure that the variable `num` has a value of `process.argv[2]".
2. Open the Terminal/CMD and move to the directory where you are keeping `fibonacci.js`.
3. Execute the command `node fibonacci.js 10` to execute the file with NodeJS to print the first 10 numbers in the Fibonacci sequence.
