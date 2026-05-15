
### Header files

```c
#include <ctype.h>
#include <stdio.h>
#include <string.h>
```

These lines import standard libraries so we can use built-in functions. 

- `<ctype.h>` provides character functions like [`toupper()`][2].
- `<stdio.h>` provides input/output functions like [`printf()`][3].
- `<string.h>` provides string utilities like [`strlen()`][1].

### Main function

```c
int main(int argc, char *argv[])
```

This is where every C program starts. Here, `argc` represents the number of
command-line arguments, and `argv` represents an array of strings containing
those arguments. So, if we run:

```console
./capitalize "hello"
```
then:
- `argc = 2`
- `argv[0] = "./capitalize"`
- `argv[1] = "hello"`

### Input validation

```c
if (argc == 2 && strlen(argv[1]) != 0)
```

This ensures:

- exactly one argument is provided
- it is not an empty string

If the user provides no input, the program prints usage message. If there are
too many arguments, the program warns about quotes, because the user most
likely called the program using `./capitalize hello world` instead of
`./capitalize "hello world"`.

### Capitalization step

```c
printf("%s\n", capitalize(argv[1]));
```

If input is valid, we call `capitalize()` with the first argument, then print
the result. In the function:

```c
char *captialize(char str[])
{
    for (int i = 0; i < strlen(str); i++)
        if (i == 0)
            str[i] = toupper(str[i]);
        else
            continue;
    return str;
}
```
we traverse each letter in the string. If `i = 0`, then we capitalize the first
letter of the string using [`toupper`][2], otherwise the string remains the same.

[1]: https://man7.org/linux/man-pages/man3/strlen.3.html
[2]: https://man7.org/linux/man-pages/man3/toupper.3.html
[3]: https://man7.org/linux/man-pages/man3/printf.3.html