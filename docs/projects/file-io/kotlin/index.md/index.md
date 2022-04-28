# File Io in Kotlin

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.