---
title: File Input Output in Kotlin
layout: default
date: 2019-10-16
featured-image: file-input-output-in-every-language.jpg
last-modified: 2019-10-16

---

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
import java.io.File
import java.nio.charset.Charset

fun main(args: Array<String>) {

    val fileName = "output.txt"

    val file = File(fileName)

    if(file.exists()){
        val output = file.readText(Charset.defaultCharset())
        println(output)
    } else{
        try {
            file.createNewFile()
            file.writeText("Hello, World!")
            val output = file.readText(Charset.defaultCharset())
            println(output)
        }catch (e :Exception){
            println("File could not be created!")
        }
    }
}
```

{% endraw %}

[File Input Output](https://sampleprograms.io/projects/file-input-output) in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Tim Lange

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).