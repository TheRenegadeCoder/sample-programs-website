### The Main Function

Breaking down this solution bottom up,

```python
if __name__ == "__main__":
    main(sys.argv[1:])
```

This bit of code checks to see if this is the `main` module run. If it is then it calls the `main`
function and passes user input to it. In this case the user input would be a string like `"XV"` (to convert from roman numeral to decimal number).

```python
def main(args):
    if len(args) < 1:
        exit_with_error('Usage: please provide a string of roman numerals')

    try:
        roman_numeral = sys.argv[1]
        print(roman_to_decimal(roman_numeral))
    except KeyError:
        exit_with_error('Error: invalid string of roman numerals')
```

This is the `main` function of this file. It parses the input, then calls our roman to decimal function
(and it also prints the results). It also deals with any errors raised.

### Throw Errors

```python
def exit_with_error(msg):
    print(msg)
    sys.exit(1)
```

This function prints a message and then exits the script with an error, `sys.exit(1)`.
If any non-zero value is returned then the program didn't complete properly.
This function is called if the user input isn't correct.

### Roman Numeral to Decimal number in Python

```python
def roman_to_decimal(string):
    res = 0
    i = 0

    while i < len(string):

        # Getting value of symbol s[i]
        s1 = value(string[i])

        if i+1 < len(string):

            # Getting value of symbol s[i+1]
            s2 = value(string[i + 1])

            # Comparing both values
            if s1 >= s2:

                # Value of current symbol is greater
                # or equal to the next symbol
                res += s1
                i += 1
            else:

                # Value of current symbol is less than
                # to the next symbol
                res = res + s2 - s1
                i += 2
        else:
            res += s1
            i += 1

    return res
```

Finally we're at the brain of the entire program. This function takes an roman numeral as string
and returns in form of Decimal number (Integer type). This function `roman_to_decimal` call another function called `value`. That function can map the each digit of roman numeral to decimal equivalent:

```python
# This function returns value of each Roman symbol
def value(r):
    return {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }[r]
```

For example, if `XV` is the input:

* First take `res` as zero (`res = 0`) and `i` (useful for accesing characters of input string) as zero (`i = 0`)

* While `i` less than length of input in roman numeral we keep on iterating loop.

* We store respective value of first character of roman numeral (with `value` function) in `s1`.

* Then we check that `i+1` is less than that of length of string or not. We use this because we need to get value of next character of roman numeral into `s2`. If `i+1` is greater than length of string then we take the `res` as `res + s1` (`res += s1`) and increment `i` by 1 and rerurns the result.

* If the value of `s1` is greater than or equal to `s2`, then we update res as `res + s1` (`res += s1`) and increment `i` by 1.

* else we update the value of `res` equal to `res + s2 - s1` (`res = res + s2 - s1`) and increment `i` by 2 (`i += 2`).

* Finally we return the result in variable `res`.
