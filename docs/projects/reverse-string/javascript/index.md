---
title: Reverse a String in JavaScript
layout: default
last-modified: 2020-05-02
featured-imaged: reverse-string-in-every-language.jpg
tags: [javascript, reverse-string]
authors:
  - herrfugbaum

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
const reverse = s => s.split('').reverse().join('');

if (process.argv.length > 2) {
    console.log(reverse(process.argv[2]));
}
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- rzuckerm
- Trever Shick

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 19 2023 22:24:49. The solution was first committed on May 06 2018 09:06:55. As a result, documentation below may be outdated.

## How to Implement the Solution

Let's look at the code in detail.

```java
const reverse = s => s.split('').reverse().join('');
```

First there is a function declaration `reverse` which takes one parameter `s`.
The `reverse` function returns a method chain of the `s` parameter. It assumes that the parameter is of type string. A string in JavaScript offers numerous methods, like `.toLowerCase()`, which would mutate a string to all lowercase letters.

Another method of the `String` object is the `split` method which you can see above.
`split()` takes two optional parameters, a seperator and a limit. In the `reverse` function it is used with an empty string `''` as a seperator. This has the effect of splitting the string at _every_ character. The return value of the `split` method is, and this makes the beauty of this solution, an array, which has it's own methods built in.

If you call the `reverse` function above, for example with `'hello'`, the `split` method would return `['h', 'e', 'l', 'l', 'o']`. Since this is an array you can immediately use one of the various array methods available in JavaScript. Luckily the language helps us a lot here, since it already has a method `.reverse()` to reverse an array.

Now we are at the second chained method and our hypothetical output would look like this `['o', 'l', 'l', 'e', 'h']`. We are just one step ahead of our solution.

All we need to do now is to somehow get back to a string. One of the array methods JavaScript offers us is the `.join()` method. It, kind of, is the opposite of the `split` method as it brings an array back together, based on an optional `seperator` parameter, and returns a string. Like the `split` method an empty string as a parameter means that it will execute on every value in the array. Since we have single characters as values it will simply concatenate them together to our string.

Now, let's look at the rest of the code:

```java
if (process.argv.length > 2) {
    console.log(reverse(process.argv[2]));
}
```

`process.argv` contains the command-line arguments. We make sure there are enough. If so, we call our `reverse` function with
the first one (`process.argv[2]`, since the first two, `process.argv[0]` and `process.argv[1]` can be ignored). Then,
`console.log` displays the reversed string returned from the `reverse` method.

Now our solution is complete.


## How to Run the Solution

To run this example you can simply open the dev tools of your browser (F12) in most cases and navigate to the `console` tab.
There you can paste in the code snippet from above.

Alternatively you can paste the code into an [online Javascript interpreter](https://onecompiler.com/javascript).
