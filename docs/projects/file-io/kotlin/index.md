---

title: File Io in Kotlin

---

Welcome to the File Io in Kotlin page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Kotlin
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

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.