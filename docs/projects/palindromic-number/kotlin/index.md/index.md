# Palindromic Number in Kotlin

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Kotlin
fun main(args: Array<String>) {
    var n: Int
    var num: Int
    var digit: Int
    var rev: Int = 0

    try {
        num = args[0].toInt()

        if (num.toString().length > 1){
            n = num

            do {
                digit = num % 10
                rev = (rev * 10) + digit
                num = num / 10
            }while (num != 0)

            if (n == rev){
                println(true)
            }else{
                println(false)
            }
        }else{
            println("Usage: please input a number with at least two digits")
        }


    }catch(e: Exception){
        println("Usage: please input a number with at least two digits")
    }
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.