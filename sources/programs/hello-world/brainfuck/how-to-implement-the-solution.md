If you're unfamiliar with Brainfuck, this might not really look like a
"Hello World" example to you. It might even look a little intimidating.
Granted, the syntax might not be the most verbose, but fear not! I'm sure it
will start making sense once we break it down.

For starters, let's reindent it a little bit:

```brainfuck
>++++++++[<+++++++++>-]<.
>++++[<+++++++>-]<+.
+++++++..
+++.
>>++++++[<+++++++>-]<++.
------------.
>++++++[<+++++++++>-]<+.
<.
+++.
------.
--------.
>>>++++[<++++++++>-]<+.
```

Well, that's already looking slightly better. Remember, the `.` operator writes
the current cell value to the output, so we've inserted a line break for every
character that gets printed.

Let's look at it line by line:

```brainfuck
>++++++++[<+++++++++>-]<.
```

We can see that we immediately move one cell to the right and increment that
cell's value eight times. This gives us, you guessed it, the value 8 in cell 1.

Then we start a loop, in which we move left (back to cell 0), add nine to that
cell, move right again, and subtract one from the value of cell 1. Remember that
the loop runs until the cell value is zero, so this would run 8 times, adding 9
to cell 0 every time. So we can already see that the value of cell 0 at this
point is 72, which corresponds to the uppercase letter 'H' in the [ASCII table][2].

So, we got our first character printed. Let's look at the second line:

```brainfuck
>++++[<+++++++>-]<+.
```

You might immediately notice that this line looks quite similar to the last one.
That might be because it does pretty much exactly the same thing. The only
difference is in the numbers. It adds the value 28 (4 times 7) to cell 0,
and then adds one more at the end of the loop, giving us a value of 101, or
a lowercase 'e'.

This is basically how the entire program works. It's just a matter of choosing
the right path in order to get from one value to the next by only using simple
addition, subtraction, and loops.

[2]: https://www.asciitable.com/
