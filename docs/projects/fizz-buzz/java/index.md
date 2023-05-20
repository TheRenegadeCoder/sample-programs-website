---
title: Fizz Buzz in Java
layout: default
last-modified: 2020-05-02
featured-image: fizz-buzz-in-java.jpg
tags: [java, fizz-buzz]
authors:
  - stuin

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
public class FizzBuzz {
    public static void main(String[] args) {
        for (int i = 1; i < 101; i++) {
            String output = "";
            if (i % 3 == 0) {
                output += "Fizz";
            }
            if (i % 5 == 0) {
                output += "Buzz";
            }
            if (output.isEmpty()) {
                output += i;
            }
            System.out.println(output);
        }
    }
}
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Java](https://sampleprograms.io/languages/java) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 15:04:56. The solution was first committed on Sep 08 2018 22:49:52. As a result, documentation below may be outdated.

## How to Implement the Solution

Java is a very standard looking programming language, so this code may look quite familiar.

The rules of the problem are quite straightforward:

    If a number is divisible by 3, print the word 'Fizz' instead of the number.
    If the number is divisible by 5, print the word 'Buzz' instead of the number.
    Finally, if the number is divisible by both 3 and 5, print 'FizzBuzz' instead
    of the number. Otherwise, just print the number.

The modulo operator will let us easily check for divisibility, as it returns the remainder
from a division. When `i` is divisible by 3, `i % 3` will just be 0.

### The Function

As with any Java program, we start out with a `public class`, (named the same as the
FizzBuzz.java file). Then inside that we set up a `main` function, with a array of string arguments.

```java
public class FizzBuzz {
    public static void main(String[] args) {
        ...
    }
}
```

The program is within that one function, so we do not need to pay any more attention to that.

### The Loop

Next we will set up the required loop, going from 1 to 100. We can use a simple for
loop to achieve that.

```java
for (int i = 1; i < 101; i++) {
    ...
}
```

The first part of it is a variable, int `i` stores a number and is started at 1.
The loop is then set to run repeatedly until `i` is greater than 100. Finally `i++ `means
that every time the loop is run, `i` will increase by 1.

### Control Flow

Each time the loop runs, it will first create a blank String to hold the output
(This just stores a list of characters for later display).

```java
String output = "";
```

Each if statement will then check for divisibility and add to the output variable.

```java
if (i % 3 == 0) {
    output += "Fizz";
}
if (i % 5 == 0) {
    output += "Buzz";
}
if (output.isEmpty()) {
    output += i;
}
```

If `i` is divisible by 3, add `"Fizz"`, then if `i` is divisible by 5, add `"Buzz"`. Notice
that there is no else statement, so both of them can run consecutively. This
also uses Java's handy ability to just add two strings together and attach one
to the end of the other. If the output is still blank after the first if
statements, then put the number there instead.

### The Output

Finally we have a long statement to put that output onto the screen.

```java
System.out.println(output);
```

This references a standard library function, and can be used at any time to output
text. The `ln` at the end means that after the output variable is printed it will
be followed by a newline, allowing the next loop to follow.


## How to Run the Solution

First we will need to grab the latest version of Java, particularly the Java
Development Kit (JDK). Next we need to save the code into a file named
`FizzBuzz.java`. Finally, in the folder with the code, we shall run the commands:

```console
javac FizzBuzz.java
java FizzBuzz
```

There are plenty of online compilers available as well.
