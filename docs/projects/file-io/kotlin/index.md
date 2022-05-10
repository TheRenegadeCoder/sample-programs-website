---

title: File Io in Kotlin
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the File Io in Kotlin page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).