
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

1.  The shape should be symmetrical both horizontally and vertically
2.  Each subsequent line should either add or remove padding by one character on both sides
3.  Whitespace should be adjusted accordingly in order to properly output the shape

The code in kotlin can be written as follows:
```kotlin
fun main (args: Array<String>)
{
    for (i in 0..9)
        println (" ".repeat (10 - i) + "*".repeat (i * 2 + 1));

    for (i in 10 downTo 0)
        println (" ".repeat (10 - i) + "*".repeat (i * 2 + 1));
}
```

### First loop
Kotlin is structured similarly to Java, but the syntax is designed to be helpful and easy, so the first line is all that is needed to get the program started.

The top half of the diamond is created here, and is comparitively easy to read:
```kotlin
for (i in 0..9)
    println (" ".repeat (10 - i) + "*".repeat (i * 2 + 1));
```
The first line sets up a basic loop, iterating the variable i from 0 to 9

The next line of code is then run 10 times, each time outputing a new line to the screen.
Each line contains (10 - i) spaces, followed by (2i + 1) stars. As i rises from 0 to 9, the number of spaces shrinks and the number of stars increases.

In the end, this loop of code will produce a large pyramid like this:

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

### Second loop
The second for loop is almost identical, and creates the same pyramid as before, but upside down.
```kotlin
for (i in 10 downTo 0)
    println (" ".repeat (10 - i) + "*".repeat (i * 2 + 1));
```
Instead of starting at 0 and ending at 9, this loop starts at 10 and ends when i is 0.

Nothing else is changed in the loop, so it adds the bottom half of the diamond and finishes the program.
