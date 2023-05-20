---
title: Fizz Buzz in Kotlin
layout: default
last-modified: 2020-05-02
featured-imaged: fizz-buzz-in-every-language.png
tags: [kotlin, fizz-buzz]
authors:
  - stuin

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
fun main(args: Array<String>){
    for (i in 1..100){
        when {
            (i % 3 == 0 && i % 5 == 0) -> println("FizzBuzz")
            i % 3 == 0 -> println("Fizz")
            i % 5 == 0 -> println("Buzz")
            else -> println("$i")
        }
    }
}
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- ali-abdullah

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Kotlin is structured very similarly to Java, but there are a lot of nice features in the syntax.

The rules of the problem are quite straightforward:

    If a number is divisible by 3, print the word 'Fizz' instead of the number.
    If the number is divisible by 5, print the word 'Buzz' instead of the number.
    Finally, if the number is divisible by both 3 and 5, print 'FizzBuzz' instead
    of the number. Otherwise, just print the number.

### The Function

The main function of the program is the same as always, just a single line to start.

```kotlin
fun main(args: Array<String>){
```

This creates a simple function to contain all the other code.

### The Loop

Next we will set up the required loop, going from 1 to 100. Kotlin makes this very easy.

```kotlin
for (i in 1..100){
```

Now we get into less familiar territory, with a `when` statement. This is similar to a `switch` statement in other languages, but it is much more flexible.

```kotlin
when {
    (i % 3 == 0 && i % 5 == 0) -> println("FizzBuzz")
    i % 3 == 0 -> println("Fizz")
    i % 5 == 0 -> println("Buzz")
    else -> println("$i")
}
```

For each line, the condition to the left of the arrow will be checked, and when a line returns `true`, the code on the right of the arrow will be executed.
It is worth mentioning that Kotlin has optional semicolons, but a newline works fine in most cases.

The first three lines are then pretty standard
1. if i is divisible by 3 and 5, print `"FizzBuzz"`
2. if i is only divisible by 3, print `"Fizz"`
3. if i is only divisible by 5, print `"Buzz"`

The only thing left to mention is the last line,

```kotlin
else -> println("$i")
```

If none of the other conditions are `true`, this default statement is run which prints out the value of `i`.
The fact that `i` is contained inside a string is completely unnesesary, but does demonstrate one of the nice features of Kotlin.

Variables can be inserted into a string at any point, and code can be executed if neccesary.
For example, `"2 + 2 = ${2 + 2}"` would in fact calculate the simple string `"2 + 2 = 4"`.


## How to Run the Solution

Online compilers such as [Kotlin Playground][2] or this [Online Kotlin Compiler][3] are a good way to get started.

To run on a personal computer, the ideal environment is [IntelliJ IDEA][4], as it and kotlin were both created by JetBrains.
If you have installed the command line version however, save the program to FizzBuzz.kt and run with these commands.
```bash
kotlinc FizzBuzz.kt -include-runtime -d FizzBuzz.jar
java -jar FizzBuzz.jar
```

[2]: https://play.kotlinlang.org/
[3]: https://www.tutorialspoint.com/compile_kotlin_online.php
[4]: https://www.jetbrains.com/idea/
