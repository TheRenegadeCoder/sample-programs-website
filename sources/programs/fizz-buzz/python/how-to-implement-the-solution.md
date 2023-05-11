Before we dig into the code too much, let's take a look at the rules:

If a number is divisible by 3, print the word `'Fizz'` instead of the number.
If the number is divisible by 5, print the word `'Buzz'` instead of the number.
Finally, if the number is divisible by both 3 and 5, print `'FizzBuzz'` instead of
the number. Otherwise, just print the number.

You can test for divisibility using the modulo operator.  The modulo operator
divides two numbers and yields the remainder, so i modulo j is 0 if i is
divisible by j. In Python, this is written as i % j.  Then, it's a simple matter
of checking whether i % 3 == 0 or i % 5 == 0.

### Code Style

You'll notice first how everything is properly indented. This is not just good
code style, Python actually enforces it.  There's no need to declare variables
as Python is what's called a weakly typed language. That means it can figure out
what type a variable should be on the fly.

### The Loop

In the very first line, we'll notice a loop:

```python
for n in range(1, 101):
```

Here, we loop through all the numbers from 1 to 100.

### Control Flow

From there, we set the variable line to an empty string and begin our testing:

```python
if n % 3 == 0:
    print("FizzBuzz" if n % 5 == 0 else "Fizz")
    continue
print("Buzz" if n % 5 == 0 else n)
```

If the number is divisible by 3, as explained above, we print the word "Fizz" if the
number is also not divisible by 5; otherwise, we print the word "FizzBuzz". We
skip the rest of the loop with the `continue` statement.

If it's divisible by 5, we print the word "Buzz"; otherwise, we print the number
(`n`).
