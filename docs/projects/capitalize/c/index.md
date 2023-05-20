---
title: Capitalize in C  
layout: default  
date: 2021-10-25
last-modified: 2021-10-26
featured-imaged: capitalize-in-every-language.jpg
tags: [c, capitalize]  
authors:
- shubhragupta-code

---

Welcome to the [C](https://sampleprograms.io/languages/c)apitalize in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char *captialize(char str[]) {
    for(int i = 0; i < strlen(str); i++) {
        if(i == 0) {
            str[i] = toupper(str[i]);
        } else {
            continue;
        }
    }
    return str;
}

int main(int argc, char *argv[]) {
    if(argc == 2 && strlen(argv[1]) != 0) {
        printf("%s\n", captialize(argv[1]));
    } else if(argc > 2) {
        printf("Use quotes around multiple strings.\n");
    } else {
        printf("Usage: please provide a string\n");
    }

    return 0;
}
```

{% endraw %}

[C](https://sampleprograms.io/languages/c)apitalize in [C](https://sampleprograms.io/languages/c) was written by:

- Jeremy Grifski
- Softizo

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 26 2019 21:04:13. The solution was first committed on Oct 09 2019 17:27:39. As a result, documentation below may be outdated.

## How to Implement the Solution


Let's understand this code block by block in the order of execution.

### Main Function
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
```
In the first three lines, we are including header files using [include directive][1] to utilise some functions defined in header files later in the program.
Here, Standard Input/Output header file (`<stdio.h>`) is called to use `printf()` function, C Standard Library (`<string.h>`) to use `strlen()` function and `<ctype.h>` to use `toupper()` function.

Before we move onto the next part, let's look on the functions which we called from header files.
**[strlen()][2]** gives the length of the string as an integer. **[toupper()][3]** converts lowercase alphabet to uppercase and **[printf()][4]** prints formatted string as output.  

For the next block,
```c
int main(int argc, char *argv[]) {
    if(argc == 2 && strlen(argv[1]) != 0) {
        printf("%s\n", captialize(argv[1]));
    } else if(argc > 2) {
        printf("Use quotes around multiple strings.\n");
    } else {
        printf("Usage: please provide a string\n");
    }

    return 0;
}
```

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
./capitalize string
```
Here, ```./capitalize``` represents **argv[0]** and `2` represents **argv[1]**.

Now the if statement check the input given by the user.If the **argc** is equal to 2 and **argv** is not an empty string, **capitalize()** gets called. Otherwise if the user has provided more than 1 string or not provided any input at all, then the program will print correct usage pattern.

```c
cchar *captialize(char str[]) {
    for(int i = 0; i < strlen(str); i++) {
        if(i == 0) {
            str[i] = toupper(str[i]);
        } else {
            continue;
        }
    }
    return str;
}
```
In this function, a for loop with a variable **i** is started. It runs till the length of string. If **i** = first letter of the string, **str[0]** get capitalized by **toupper()**. Otherwise rest of the string remains the same.

[1]: https://en.wikipedia.org/wiki/Include_directive
[2]: https://man7.org/linux/man-pages/man3/strlen.3.html
[3]: https://man7.org/linux/man-pages/man3/toupper.3.html
[4]: https://man7.org/linux/man-pages/man3/printf.3.html


## How to Run the Solution

```console
gcc -o capitalize capitalize.c
./capitalize
```
Another handy option is to compile and run using online C Compiler such as [OnlineGDB][5] or [Repl][6]

[5]: https://www.onlinegdb.com/
[6]: https://replit.com/languages/c
