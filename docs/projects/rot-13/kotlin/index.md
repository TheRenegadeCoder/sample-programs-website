---

---

Welcome to the Rot 13 in Kotlin page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Kotlin
data class EncodingBounds(val lowerBound: Int, val upperBound: Int)

fun encodingBoundsForCharValue(c: Char): EncodingBounds? {
    val lowerCaseBounds = EncodingBounds('a'.toInt(), 'z'.toInt())
    val upperCaseBounds = EncodingBounds('A'.toInt(), 'Z'.toInt())
    return when (c) {
        in 'a'..'z' -> lowerCaseBounds
        in 'A'..'Z' -> upperCaseBounds
        else -> null
    }
}

fun calculateRotatedChar(char: Char, rotation: Int, bounds: EncodingBounds): Char {
    val rotatedCharVal = char.toInt() + rotation
    val remainder = rotatedCharVal - (bounds.upperBound + 1)
    return (if (rotatedCharVal > bounds.upperBound) bounds.lowerBound + remainder else rotatedCharVal).toChar()
}

fun parseInput(args: Array<String>): String? {
    if (args.isEmpty()) {
        return null
    }
    val text = args[0]
    if (text.isEmpty()) {
        return null
    }
    return text
}

fun rot13Encode(text: String): String {
    val rotation = 13

    return text.map { c ->
        val bounds = encodingBoundsForCharValue(c)
        if (bounds == null) {
            c.toString()
        } else {
            calculateRotatedChar(c, rotation, bounds).toString()
        }
    }.reduce { encodedText, encodedChar ->
        encodedText + encodedChar
    }

}

fun main(args: Array<String>) {
    val strToEncode = parseInput(args)
    if (strToEncode == null) {
        println("Usage: please provide a string to encrypt")
    } else {
        println(rot13Encode(strToEncode))
    }
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.