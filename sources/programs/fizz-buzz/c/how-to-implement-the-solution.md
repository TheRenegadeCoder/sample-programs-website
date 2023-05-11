> Write a program that prints the numbers 1 to 100. However, for multiples of three,
> print "Fizz" instead of the number. Meanwhile, for multiples of five, print "Buzz"
> instead of the number. For numbers which are multiples of both three and five,
> print "FizzBuzz"

Now, let us take a look at the code for FizzBuzz in C.

Let's understand this code block by block.

### Main Function

```c
#include <stdio.h>
```

Here, we are including Standard Input/Output header file (`.h` files) using [include directive][1] in order to use **printf()** and **puts()** function later in the program.

```c
int main(void)
{
```

In C, we declare a function using general form:

```
return_type function_name(parameter){
  ...
}
```

So, here we are declaring **main** function with return type integer and void as a parameter, i.e., no input from the user.

### For Loop

```c
for (unsigned int i = 1; i <= 100; i++) {
    ...
}
```

In this block, we first created a **for** loop initializing *i* as an unsigned integer(non-negative integers) as 1 and increasing it by 1 every time the *for loop* iterates. This **for** loop will iterate until the value of *i* is equal to 100.

Before moving onto *if-elseif* statements, we should consider **puts()** and **printf()** functions. **puts()** writes null-terminated string into stdout(standard output - a file descriptor where a process can write output) and adding a newline at the end. **printf()** prints formatted string. In this program, we are using **%u** as a format specifier for unsigned integers.

### Control flow

```c
if (i % 15 == 0) {
    puts("FizzBuzz");
} else if (i % 3 == 0) {
    puts("Fizz");
} else if (i % 5 == 0) {
    puts("Buzz");
} else {
    printf("%u\n", i);
}
```

Now, variable *i* which we initialized in for loop, will check for following conditions:
- If *i* is divisible by 15, **FizzBuzz** is printed. Otherwise,
- if *i* is divisible by 3, **Fizz** is printed.Otherwise,
- If *i* is divisible by 5, **Buzz** is printed. Otherwise,
- That number, i.e., *i* gets printed.

Finally, `return 0;` returns 0 to main program, which indicates zero errors.

[1]: https://en.wikipedia.org/wiki/Include_directive
