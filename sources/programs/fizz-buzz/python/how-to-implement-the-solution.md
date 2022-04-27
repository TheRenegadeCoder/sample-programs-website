Let’s start by looking at the complete Fizz Buzz algorithm in Python:

```python
for i in range(1, 101):
    line = ''
    if i % 3 == 0:
        line += "Fizz"
    if i % 5 == 0:
        line += "Buzz"
    if not line:
        line += str(i)
    print(line)
```

Before we dig into the code too much, let’s take a look at the rules:

If a number is divisible by 3, print the word ‘Fizz’ instead of the number.
If the number is divisible by 5, print the word ‘Buzz’ instead of the number.
Finally, if the number is divisible by both 3 and 5, print ‘FizzBuzz’ instead of
the number. Otherwise, just print the number.

You can test for divisibility using the modulo operator.  The modulo operator
divides two numbers and yields the remainder, so i modulo j is 0 if i is
divisible by j. In Python, this is written as i % j.  Then, it’s a simple matter
of checking whether i % 3 == 0 or i % 5 == 0.

### Code Style

You’ll notice first how everything is properly indented. This is not just good
code style, Python actually enforces it.  There’s no need to declare variables
as Python is what’s called a weakly typed language. That means it can figure out
what type a variable should be on the fly.

### The Loop

In the very first line, we’ll notice a loop:

```python
for i in range(1, 101):
```

Here, we loop through all the numbers from 1 to 100.

### Control Flow

From there, we set the variable line to an empty string and begin our testing:

```python
line = ''
if i % 3 == 0:
    line += "Fizz"
if i % 5 == 0:
    line += "Buzz"
if not line:
    line += str(i)
```

If the number is divisible by 3, as explained above, we add the word “Fizz” to
the empty string.  If it’s divisible by 5, we add the word “Buzz”. Notice the
efficiency here. We don’t need and because by simply adding “Buzz”, we meet the
requirement for the case where the number is divisible by 3 and 5, or just 5.  
Then we add i to the empty string if the string is still empty.

Notice that an empty string returns false.  This is a concept called falsey.  
In a weakly typed language, like Python and JavaScript, values such as 0,
undefined, null, and '' all return false when they’re used in logical comparisons.

### Printing

Finally, we print the result of line on every iteration:

```python
print(line)
```

Since we declare an empty string at every iteration, we don’t have to worry about
line containing any junk from the previous iteration.
