At any rate, here’s the implementation of Hello World in Google Apps Script:

```
function helloWorld() {
  Logger.log("Hello, World!");
}
```

Unlike many languages, Google Apps Script code doesn’t need a main function. In fact, all we have to do is define a function. Google handles what we want to do with the script at runtime.

With that in mind, we can see that we’ve defined a helloWorld function with syntax similar to [JavaScript][1]. In other words, we have a function definition which encloses a code block with braces.

Inside the code block, we have our typical print call. In this case, we leverage the Logger to do our printing. Then we pass our “Hello, World!” string to the log function, and call it a day.
