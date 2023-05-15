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
