---
title: Hello World in Kotlin
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-kotlin.jpg
tags: [kotlin, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
fun main(args: Array<String>) {
  println("Hello, World!")
}
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Jeremy Griffith

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's get down to business, Hello World in Kotlin.

On the first line, we have the `package` declaration. Like most
languages, this basically declares the package or module name
of this file. If anyone needed to use a function in this file,
they could access it via the package name.

Next, we have the function definition. In this first line, we
can see we define the `main` function which receives an array of
`String`s as input. In a lot of languages, types are declared in
type-var order, not in Kotlin. In Kotlin, we declare the variable
name before giving it a type.

Finally, we print Hello World in Kotlin. Like many languages, 
we use a simple call to the `println` function, so no surprises there.


## How to Run the Solution

At this point, we probably want to actually run the Hello World in
Kotlin code snippet. Perhaps the easiest way to do so is to leverage
the online Kotlin editor.

Alternatively, we can use the latest [standalone compiler][1]. Of course,
we'll want to get a copy of [Hello World in Kotlin][2] while we're at it.
With both in hand, all we need to do is navigate to the folder containing
our files and run the following:

```shell
kotlinc HelloWorld.kt -include-runtime -d HelloWorld.jar
java -jar HelloWorld.jar
```

The standalone Kotlin compiler compiles Kotlin down to a
runnable Java Archive (`jar`) which we can then execute using the Java Runtime
Environment.

[1]: https://kotlinlang.org/docs/command-line.html#manual-install
[2]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/k/kotlin/HelloWorld.kt
