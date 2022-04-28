---

title: Hello World in Kotlin
layout: default
last-modified: 2020-05-02
featured-image: hello-world-in-kotlin-featured-image.JPEG
tags: [kotlin, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the Hello World in Kotlin page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Kotlin
fun main(args: Array<String>) {
  println("Hello, World!")
}

```

## How to Implement the Solution

Anyway, let�s get down to business�Hello World in Kotlin:

```kotlin
package hello
fun main(args: Array<String>) {
  println("Hello, World!")
}
```
  
Now, time to dig in!

On the first line, we have the package declaration. Like most 
languages, this basically declares the package or module name 
of this file. If anyone needed to use a function in this file, 
they could access it via the package name.

Next, we have the function definition. In this first line, we 
can see we define the main function which receives an array of 
Strings as input. In a lot of languages, types are declared in 
type-var order, not in Kotlin. In Kotlin, we declare the variable 
name before giving it a type.

Finally, we print Hello World in Kotlin. Like many languages, 
we use a simple call to the println function, so no surprises there.


## How to Run the Solution

At this point, we probably want to actually run the Hello World in 
Kotlin code snippet. Perhaps the easiest way to do so is to leverage 
the online Kotlin editor.

Alternatively, we can use the latest standalone compiler. Of course, 
we�ll want to get a copy of Hello World in Kotlin while we�re at it. 
With both in hand, all we need to do is navigate to the folder containing 
our files and run the following:

```shell
kotlinc hello-world.kt -include-runtime -d hello-world.jar
java -jar hello-world.jar
```

Apparently, the standalone Kotlin compiler compiles Kotlin down to a 
runnable jar which we can then execute using the Java Runtime 
Environment. Of course, I haven�t tried it. After all, I pulled these 
directions from Kotlin documentation. Let me know if this works in the 
comments.
