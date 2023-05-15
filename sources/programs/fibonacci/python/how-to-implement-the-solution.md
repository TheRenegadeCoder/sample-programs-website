Now, we will consider this code block by block on the order of execution.

```python
if __name__ == "__main__":
    main(sys.argv[1:])
```

This code checks if the `main` module is run. If it is, it then passes control to `main` function passing argument string provided by the user.  

```python
def main(args):
    try:
        fibonacci(int(args[0]))
    except (IndexError, ValueError):
        print("Usage: please input the count of fibonacci numbers to output")
        sys.exit(1)
```

This main function was invoked earlier with argument string. Next line invokes `fibonacci()` function. If the function raises [`IndexError`][1] *(Raised when a sequence subscript is out of range)* or [`ValueError`][2] *(Raised for an non-integer value)*, it prints correct usage pattern. And program exits with exit status `1` which specifies abnormal termination.  

```python
def fibonacci(n):
    fib = fibs()
    for i in range(1, n + 1):
        print(f'{i}: {next(fib)}')

def fibs():
    first = 1
    second = 1
    yield first
    yield second
    while True:
        new = first + second
        yield new
        first = second
        second = new
```

In `fibonacci()` function, function `fibs()` is called. In `fibs()`, [`yield`][3] function returns generator which iterates to store and get values. Value of `first` and `second` are initially stored in generator as 1 and 2. In the while loop, values of fibonacci sequence is added using rule `third_num = first_num + second_num`. Control goes back to `fibonacci()` which prints values returned by `next()` which returns next item in iterator. This sequence is repeated till the user specified input times.

[1]: https://docs.python.org/3/library/exceptions.html#IndexError
[2]: https://docs.python.org/3/library/exceptions.html#ValueError
[3]: https://docs.python.org/3/reference/simple_stmts.html#the-yield-statement
