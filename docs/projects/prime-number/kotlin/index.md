---

---

Welcome to the Prime Number in Kotlin page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Kotlin
fun main(args: Array<String>) 
{
    if (args.isNullOrEmpty() || args[0].isBlank() || args[0].toIntOrNull()?.takeIf { it >= 0 } == null) {
        println("Usage: please input a non-negative integer")
        return
    }

    val num = args[0].toInt()
    if(num>1)
    {
        for(i in 2 until num)
        {
            if(num%i == 0)
            {
                println("Composite")
                return
            }
        }
        println("Prime")
    }
    else
    {
        println("Composite")
    }
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.