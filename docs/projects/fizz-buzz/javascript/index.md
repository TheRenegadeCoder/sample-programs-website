---
title: FizzBuzz in JavaScript
layout: default
last-modified: 2020-05-02
featured-imaged: fizz-buzz-in-every-language.png
tags: [javascript, fizzbuzz]
authors:
  - herrfugbaum

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Javascript](https://sampleprograms.io/languages/javascript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```javascript
function fizzbuzz(num){
    for(let i=1; i <= num; i++){
      if(i % 15 == 0){
        console.log("FizzBuzz");
      }
      else if(i % 5 == 0){
        console.log("Buzz");
      }
      else if(i % 3 == 0){
        console.log("Fizz");
      }
      else console.log(i);
   }
  }
  
fizzbuzz(100);
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Javascript](https://sampleprograms.io/languages/javascript) was written by:

- Jeremy Grifski
- Juan F Gonzalez

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 22 2021 15:02:49. The solution was first committed on Jul 27 2018 10:37:06. As a result, documentation below may be outdated.

## How to Implement the Solution

FizzBuzz is quite a simple program.
In line 1 the `fizzbuzz` function gets declared. It takes a parameter `num` that determines how far the program should count.
The counting logic takes place in a for-loop in line 2. It starts counting at 1, increases the counter `i` by 1 in every iteration and stops once it reaches `num`.

To understand the main logic of this programm you need to know.

## The modulo (remainder) operator %

>> The remainder operator returns the remainder left over when one operand is divided by a second operand. It always takes the sign of the dividend. ([Mozilla][1])

The trick here is to create a _truthy_ value for the if statements. This is why you can see the `i % 3 == 0` etc. conditionals. If a number is divisible by 3 there will be no remainder, in other words the remainder is true and thus i % 3 == 0 (% 5, % 15) is true in these cases.

Hint: The order of the conditionals matters. If you'd check for example in reverse order, you would print all 3 strings, if the number is divisible by 3 _and_ 5!

Hint: Instead of `i % 15 == 0` you could also write `i % 3 && i % 5`.

Last, but not least, it prints the number via the else clause `else console.log(i);` if none of the conditionals were true.

Extra mile: If you want you can move the conditionals into variables and move them up the scope, right after the second line between the for loop and the first if statement.
For example: `const divisibleBy3 = i % 3`. This way you'd remove the use of [magic numbers][2].

Fun Fact: Despite being a simple programming exercise there is a controversal article about the question [Why can't programmers program?](https://blog.codinghorror.com/why-cant-programmers-program/) that even led to an ["enterprise-class"](https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition) version of this game.

[1]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder
[2]: https://en.wikipedia.org/wiki/Magic_number_(programming)


## How to Run the Solution

### In the Browser

To try out this script just copy it, open the dev tools of your Browser (F12 by default in most cases), head to the `console` tab, paste in the script and press enter to run it.

### Node.js

Download and install `Node.js`.
Save the script in, for example, `index.js` and from the same directory open a console of your choice (cmd, powershell, bash, etc.) and run `node index.js`.
Hint: Depending on your operating system the node binary might be called slightly different for example on some linux distributions, you'd need to type `nodejs index.js` instead.
