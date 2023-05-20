---
title: Fizz Buzz in Befunge
layout: default
last-modified: 2020-08-30
featured-image: fizz-buzz-in-befunge.jpg
tags: [befunge, fizz-buzz]
authors:
  - stuin

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Befunge](https://sampleprograms.io/languages/befunge) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```befunge
1 >  :3%   v            
   v  \0   _ "zziF",,,,v
   v  \1               <
   > :5%   v            
   v _v#\  _ "zzuB",,,,v
   v  >:.  v $\        <
   v       <           @
   > :25*  ::,  *1-`   |
  ^        +1          <
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Befunge](https://sampleprograms.io/languages/befunge) was written by:

- Stuart

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Befunge, like many other esoteric languages, has a very unique look to it, and is very complex at first glance. Each operation is denoted by a single character, and the file can be traversed in four directions. If you have not read about it before, do that first, starting here: [The Befunge Programming Language][1].

The Fizz-Buzz problem itself is here:

    If a number is divisible by 3, print the word 'Fizz' instead of the number.
    If the number is divisible by 5, print the word 'Buzz' instead of the number.
    Finally, if the number is divisible by both 3 and 5, print 'FizzBuzz' instead
    of the number. Otherwise, just print the number.

Don't worry if the code looks confusing, we will break it down and go over the different sections.

### First set

The first section to look at will handle the Fizz statement, and adds a boolean value to the stack for use later.

```
1 >  :3%   v
   v  \0   _ "zziF",,,,v
   v  \1               <
```

The program starts at the top left corner, meaning that the stack will start with a 1, and then cross over the top line, running the characters `:3%`.

- `:` will make a copy of the top value, which will count the current iteration.
- `3` will push a 3 on top of the stack.
- `%` will run modulus on the top two values, returning the remainder of x / 3.

The pointer then moves down onto the `_`, which will run as an if statement, moving right if the top or the stack is 0, and left if it is anything else. Combined with the previous statements, it will move right whenever the initial value is divisible by 3, pushing `zziF` to the stack and printing it out in the proper order.

In both cases, the instruction pointer then returns to the left, adding either a 1 to the stack after printing Fizz, or a 0 if nothing was printed. Each `\` then swaps the top two values, putting this indicator value below the current run count.

### Second set

The second section of code is very similar, intended to handle the Buzz part of the program.

```
   > :5%   v
   v _v#\  _ "zzuB",,,,v
   v  >:.  v $\        <
   v       <
```

Like the previous section, `:5%` will calculate the remainder of x / 5, and the `_` will send the pointer left or right accordingly.

- If the value is divisible by 5, the program will print out `Buzz` and head to the downward arrow at the center, `\$` deleting the 0 or 1 value that was stored earlier.
- If the current iteration is not divisible, `\` will switch that number with the binary value stored in the first set, and `#` will jump straight to the `_` statement at the start of the second line. This checks the previous boolean, and in the case that nothing has been printed out so far, directs the instruction pointer to `:.`, printing out the run count as a numerical value.

### Cleanup

The final section handles the new line and sets up the next loop of the program.

```
   v               @
   > :25* ::, *1-` |
  ^        +1      <
```

The middle line has three main statements. `:25*` copies the current value and pushes 2 * 5 to the stack. `::,` makes 2 more copies of 10, then prints out one of them as a newline. Finally, `*1-'` multiplies the 10s together, subtracts 1 from it to get 99, then pushes 1 if the current iteration is larger.

At the end, `|` checks for a zero on top of the stack, sending the pointer downward if it is found. If there is a 1 and the current iteration is > 99, then the `@` symbol is activated instead, ending the program.

If the counter has not yet reached 100, `1+` adds 1 to it, and the pointer is sent back to the beginning of the loop.

[1]: https://esolangs.org/wiki/Befunge


## How to Run the Solution

Because of the particular design of the language, it is recommended to use a Befunge interpreter. It is a lot easier to learn and play around with when you can step through and see what the pointer is doing.

- [Befunge Playground][2]
- [jsFunge IDE][3]
- [Befunge-93 Interpreter][4]

If you do want to use a compiler, here is another option:

- [BefunUtils][6]

[2]: https://www.bedroomlan.org/tools/befunge-playground/#prog=hello,mode=edit
[3]: https://befunge.flogisoft.com/
[4]: http://qiao.github.io/javascript-playground/visual-befunge93-interpreter/
[6]: https://github.com/Mikescher/BefunUtils
