---
title: Prime Number in C  
layout: default  
date: 2021-10-26
last-modified: 2021-10-26
featured-imaged: prime-number-in-every-language.jpg
tags: [c, prime-number]  
authors:
- shubhragupta-code

---

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <stdlib.h>

void prime_number(int number)
{
    if (number < 0) {
        printf("Usage: please input a non-negative integer\n");
        return;
    } else if (number == 0 || number == 1) {
        printf("Composite\n");
        return;
    }

    for (int i = 2; i < number; i++) {
        if (number % i == 0) {
            printf("Composite\n");
            return;
        }
    }
    printf("Prime\n");
}

int is_int(char *str)
{
    if (str[0] > '9' || str[0] < '0')
            return (1);
    for (int i = 0; str[i]; i++) {
        if (str[i] > '9' || str[i] < '0')
            return (1);
    }
    return (0);
}

int main(int ac, char **av)
{
    if (ac != 2 || is_int(av[1]) != 0) {
        printf("Usage: please input a non-negative integer\n");
        return (1);
    }
    prime_number(atoi(av[1]));
    return (0);
}
```

{% endraw %}

[Prime Number](https://sampleprograms.io/projects/prime-number) in [C](https://sampleprograms.io/languages/c) was written by:

- Matias

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's understand this code block by block in the order of execution.

```c
#include <stdio.h>
#include <stdlib.h>
```

In the first two lines, we are including header files using [include directive][8] to utilize some functions defined in header files later in the program.
Here, Standard Input/Output header file (*\<stdio.h\>*) is called to use **printf()** function, C Standard Library (*\<stdlib.h\>*) to use **atoi()** function.

Before we move onto the control flow, let's look on the functions which we called from header files.
**[atoi()][2]** converts argument string into an integer. **[printf()][4]** prints formatted string as output.

Next is,

int main(int ac, char **av)
{
    if (ac != 2 || is_int(av[1]) != 0) {
        printf("Usage: please input a non-negative integer\n");
        return (1);
    }
    prime_number(atoi(av[1]));
    return (0);
}
```

In C, we declare a function using general form:

```
return_type function_name(parameter){
  ...
}
```

So, we are declaring main function with return_type integer and **ac** and **av** as parameters to access command line arguments.
**ac** and **av** are variables which main function will get when run in command-line. **ac** stores argument count while **av** stores array of strings that are arguments. This should be kept in mind that all command-line arguments are stored as strings.

**av[0]** represents first argument which always is equal to name of our program. If we type the following command in terminal:

```console
./prime-number 2
```

Here, `./prime-number` represents **av[0]** and `2` represents **av[1]**.

In the main function, if statement checks if **ac** is not equal to 2 or value returned by **is_int()** function is not equal to 0, if so it prints **Usage: please input a non-negative integer** and program gets stopped with an exit code of 1. Otherwise **prime_number()** gets called.

Now, we will see what happens in **is_int** function.

```c
int is_int(char *str) {
    if (str[0] > '9' || str[0] < '0')
            return (1);
    for (int i = 0; str[i]; i++) {
        if (str[i] > '9' || str[i] < '0')
            return (1);
    }
    return (0);
}
```

In this function, if the ASCII value of first character of the string is greater than '9' or less than '0', control goes to the next part and this function returns an exit value of 1. Otherwise every character of the string get checked with the above condition. If this is true, control goes to the next part and this function returns an exit value of 1.
Now, if none of the two conditions is true, the function exits with the return value of 0 indicating zero error.

Moving to the next block:

```c
void prime_number(int number) {
    if (number < 0) {
        printf("Usage: please input a non-negative integer\n");
        return;
    } else if (number == 0 || number == 1) {
        printf("Composite\n");
        return;
    }

    for (int i = 2; i < number; i++) {
        if (number % i == 0) {
            printf("Composite\n");
            return;
        }
    }
    printf("Prime\n");
}

```
In this function, it is checked if number is not less than 0. If so, **Usage: please input a non-negative integer** gets printed and function returns.
If number is equal to 0 or equal to 1, **Composite** is printed and function returns.
Otherwise, control goes to the for loop which checks if the number is divisible by any other number. If so, **Composite** gets printed and function returns. Else if the function is still on, then it prints **Prime**.

[8]: https://en.wikipedia.org/wiki/Include_directive
[2]: https://man7.org/linux/man-pages/man3/atoi.3.html
[4]: https://man7.org/linux/man-pages/man3/printf.3.html


## How to Run the Solution

```console
gcc -o prime-number prime-number.c
./prime-number
```
Another handy option is to compile and run using online C Compiler such as [OnlineGDB][5], [Repl][6]

[5]: https://www.onlinegdb.com/
[6]: https://replit.com/languages/c
