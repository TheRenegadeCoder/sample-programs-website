---

title: Even Odd in C  
layout: default  
date: 2020-10-05
featured-image: even-odd-in-every-language-featured-image.JPEG
tags: [c, even-odd]  
authors:
- shubhragupta-code

---

Welcome to the Even Odd in C page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{    
    if (argc == 1 || argv[1][0] == '\0' || (atoi(argv[1]) == 0 && strcmp(argv[1], "0") != 0)) {
        printf("Usage: please input a number\n");
    } else {
        int input = atoi(argv[1]);
        if (input % 2 == 0) {
            printf("Even\n");
        }
        else {
            printf("Odd\n");
        }
    }

    return 0;
}

```

## How to Implement the Solution


```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{    
    if (argc == 1 || argv[1][0] == '\0' || (atoi(argv[1]) == 0 && strcmp(argv[1], "0") != 0)) {
        printf("Usage: please input a number\n");
    } else {
        int input = atoi(argv[1]);
        if (input % 2 == 0) {
            printf("Even\n");
        }
        else {
            printf("Odd\n");
        }
    }

    return 0;
}
```
Let's understand this code block by block.

### Main Function
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
```
In the first three lines, we are including header files using [include directive][8] to utilise some functions defined in header files later in the program.
Here, Standard Input/Output header file(*\<stdio.h\>*) is called to use **printf()** function, C Standard Library(*\<stdlib.h\>*) to use **atoi()** function and *\<string.h\>* to use **strcmp()** function.&nbsp;

In C, we declare a function using general form:
```
return_type function_name(parameter){
  ...
}
```
So, we are declaring main function with return_type integer and **argc** and **argv** as parameters to access command line arguments.
**argc** and **argv** are variables which main function will get when run in command-line. **argc** stores argument count while **argv** stores array of strings that are arguments. This should be kept in mind that all command-line arguments are stored as strings.

**argv[0]** represents first argument which always is equal to name of our program. If we type the following command in terminal:
```console
./even-odd 2
```
Here, ```./even-odd``` represents **argv[0]** and ```2``` represents **argv[1]**.

### Control Flow
Before we move onto the control flow, let's look on the functions which we called from header files.
**[atoi()][2]** converts argument string into an integer. **[strcmp()][3]** compares two strings and **[printf()][4]** prints formatted string as output.  
For the if-else statements, first if condition checks if the argument count is 1 or if the argument provided is only a null string or if the argument is equal to 0(integer). For that it prints correct usage pattern.  
Otherwise the value of **argv[1]** is converted into integer and stored in variable *input*. ```%``` represents modulo operator which gives remainder for integer division. So, in case of ```input % 2```, 0 as remainder shows that *input* is divisible by 2 and non zero remainder shows indivisibility. Thus, prints *Even* or *Odd* depending on *input* for the next if statement.  
Return value is called exit code. So, 0 as exit code represents zero error.


## How to Run the Solution

```console
gcc -o even-odd even-odd.c
./even-odd
```
Another handy option is to compile and run using online C Compiler such as [OnlineGDB][5], [Repl][6]
