---
title: Longest Word in JavaScript
layout: default
date: 2020-10-26
last-modified: 2020-10-26
featured-image:
tags: [longest-word-in-string, javascript]
authors:
    - barhouum7
---


In this article, we will writing a program to find the length of the longest word in the provided sentence in JavaScript.



## How to Implement the Solution

Let's look at the code in detail:

code for [longest_wordLength_in_string.js](https://github.com/TheRenegadeCoder/sample-programs/blob/master/archive/j/javascript/longest_wordLength_in_string.js):

```javascript
function findLongestWordLength(str) {
  const words = str.split(' ');
  // console.log(words)
  var maxLength = 0;

  for (var i = 0; i < words.length; i++) {
    if (words[i].length > maxLength) {
      maxLength = words[i].length;
    }
  }

  return maxLength;
}

console.log(findLongestWordLength("The quick brown fox jumped over the lazy dog"))
```

## How to Run Solution

If you want to run this program, you can download a copy of [longest_wordLength_in_string.js](https://github.com/TheRenegadeCoder/sample-programs/blob/master/archive/j/javascript/longest_wordLength_in_string.js).

Next, open it on your text editor, then you could show the result on your console.

Alternatively, copy the solution into an online [JavaScript Interpreter](https://repl.it/languages/javascript) and hit run.

## Further Reading

- Fill out as needed
