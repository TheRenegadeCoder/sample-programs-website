### Approach

We get the length of the input string and iteration from the last character to the first, displaying each character.

[Time complexity][1]: O(n)

<br/>

### Breakdown

Now let us see step-by-step how the code works.

```c
#include <stdio.h> 
#include <string.h> 
```

Here we are including header files (`.h` files) to use functions like `printf()`. Header files provided us with tested ready to use functions to ease the software development work. 

By including `#include <stdio.h>` we can use `printf()` method without worrying about how it is implemented.

```c
int main(int argc, char **argv)
{
    char *text = "";
    size_t textlen;

    /* get text from command line and calculate length */
    if (argc >= 2) {
        text = argv[1];
    }

    textlen = strlen(text);
```

This get the first command-line argument if it is present. Otherwise, an empty string it assumed. The variable `text` contains
a pointer to the string to be reversed. Then, the length of the string is calculated using **strlen()** and stored in `textlen`.

Now we get to actual code that displays the string in reverse:

```c
/* print characters in reverse */
while (textlen-- > 0) {
    putchar(text[textlen]);
}
```

This goes through the string in reverse order and displays each character.

Then, a newline is displayed:

```c
/* put a newline at the end */
putchar('\n');
```

Finally the code exits:

```c
return 0;
```

[1]: https://en.wikipedia.org/wiki/Time_complexity
