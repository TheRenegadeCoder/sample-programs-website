---
title: Baklava in C
layout: default
date: 2020-10-05
featured-image: baklava-in-c.jpg
tags: [c, baklava]
authors:
  - stuin

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include "stdio.h"

int main (void)
{

  for (int i = 0; i < 10; i++)
  {
    printf ("%.*s", (10 - i), "                                 ");
    printf ("%.*s", (i * 2 + 1), "******************************");
    printf ("\n");
  }

  for (int i = 10; -1 < i; i--)
  {
    printf ("%.*s", (10 - i), "                                 ");
    printf ("%.*s", (i * 2 + 1), "******************************");
    printf ("\n");
  }

  return 0;

}
```

{% endraw %}

[Baklava](https://sampleprograms.io/projects/baklava) in [C](https://sampleprograms.io/languages/c) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

```
               *
              ***
             *****
            *******
           *********
          ***********
         *************
        ***************
       *****************
      *******************
     *********************
      *******************
       *****************
        ***************
         *************
          ***********
           *********
            *******
             *****
              ***
               *
```

1.  The shape should be symmetrical both horizontally and vertically
2.  Each subsequent line should either add or remove padding by one character on both sides
3.  Whitespace should be adjusted accordingly in order to properly output the shape

### Setup

The first few lines are normal requirements for a simple text program like this.

`#include "stdio.h"` is used to include the standard input/output library, allowing us to use some built in output commands like `printf`.

After that, `int main(void)` creates the main function, meaning that the code inside the curly braces will be run when the program starts.

### First loop

The expanding top part of the diamond is drawn by the first for loop, starting here:

```c
for (int i = 0; i < 10; i++)
```

This contains 3 separate code statements, and makes up the most basic kind of loop in c.

1. `int i = 0;` Creates a numerical variable `i`, and gives it a value of 0.
2. `i < 10;` Repeatably checks if `i` is less than 10, and continues the loop if it is.
3. `i++` Adds 1 to the value of `i` whenever the loop ends.

Every time the loop runs, all the code inside the curly braces is activated.
Each line is a call to `printf()`, a function used to show text to the user.

1. `printf ("%.*s", (10 - i), "                                 ");`
  This line of code prints out a list of `10 - i` spaces. Here `"%.*s"` is a special sequence used to determine the format. If it was just `%s`, `printf` would output normal text, but putting `.*` in the middle means that its length can be changed.
2. `printf ("%.*s", (i * 2 + 1), "******************************");`
  This is a similar piece of code, printing `2i + 1` stars to the screen. `i` starts at 0, so the first line will just be one star, but as `i` increases, 2 more stars will be added to each line.
3. `printf("\n");`
	This line is much more simple, and is used like an enter key, moving the text to a new line at the end of each loop.

In the end, this loop of code will produce a large pyramid like this:

```
               *
              ***
             *****
            *******
           *********
          ***********
         *************
        ***************
       *****************
      *******************
```

### Second loop

The second for loop is almost identical, and creates the same pyramid as before, but upside down.
```c
for (int i = 10; -1 < i; i--)
```
1. `int i = 10;` Sets `i` to 10 at the start instead of 0.
2. `-1 < i;` The loop runs until `i` is equal to 0.
3. `i--` Here `i` is getting smaller each loop, rather than getting bigger.

Nothing else is changed in the loop, so the final output of the program becomes the full diamond like above.

The line `return 0;` at the end just announces that the program has finished successfully.


## How to Run the Solution

If we want to run it on a specific computer, we need to install a compiler such as GCC, and type the following commands in a terminal.

```console
c -o baklava baklava.c
./baklava
```
