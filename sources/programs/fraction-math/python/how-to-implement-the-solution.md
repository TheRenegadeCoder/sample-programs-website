Let's first take a look at the solution.

### Imports

In our sample, we import three standard library utilities:

```python
import operator
import sys
from fractions import Fraction
```

Here, we have imported `sys` for taking arguments from console. `operator` are to perform artithmatic and relational operation. `Fraction` class provide various methods for working with fractions.

### Mapping operator

```python
d = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "==": lambda x, y: int(operator.eq(x, y)),
    "<": lambda x, y: int(operator.lt(x, y)),
    ">": lambda x, y: int(operator.gt(x, y)),
    "<=": lambda x, y: int(operator.le(x, y)),
    ">=": lambda x, y: int(operator.ge(x, y)),
    "!=": lambda x, y: int(operator.ne(x, y)),
}
```

Here, we are mapping operator entered in the string to actual operator method so that `Fraction class` can perform that.

### Check number of arguments

Our `main` function takes arguments as parameter.

```python
def main(args):
    if len(args) != 3:
        print("Usage: ./fraction-math operand1 operator operand2")
        sys.exit(1)
```

Here, we check if number of arguments entered are three, if it's not then print `Usage: python fraction.py operand1 operator operand2` on console and exit.

### Perform operation

```python
    else:
        try:
            o1 = Fraction(args[0])
        except ValueError:
            print(f"Invalid operand: {args[0]}")
        try:
            o2 = Fraction(args[2])
        except ValueError:
            print(f"Invalid operand: {args[2]}")
        try:
            print(d[args[1]](o1, o2))
        except KeyError:
            print(f"Invalid operator: {args[1]}")
```

Now, we check if we can convert entered `args` into `Fraction` type if we can't then we print `Invalid operand: (entered operand)` on console. After that we check if operator is valid and if it's not then we print `Invalid operator: (entered operator)` on console. If everything is good then it prints desired output on console

### Taking arguments from console

```python
if __name__ == "__main__":
    main(sys.argv[1:])
```

Here, `sys.argv` contains arguments passed from the console. We know that first argument is name of file itself.
so, all we need is arguments that are passed after that. We then give it to the `main` function.
