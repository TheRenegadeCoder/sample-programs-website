---

title: Bubble Sort in Kotlin
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Bubble Sort in Kotlin page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Kotlin
fun main(args: Array<String>) 
{
    var nums: IntArray
    try
    {
        nums = args[0].split(", ").map{ it.toInt() }.toIntArray()
        if (nums.size < 2) {
            throw Exception()
        }
    }
    catch(e: Exception)
    {
        println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"")
        return
    }
    var swapped:Boolean = false
    for(i in 0 until nums.count()-1)
    {
        swapped = false
        for(j in 0 until nums.count()-i-1)
        {
            if(nums[j]>nums[j+1])
            {
                //swap
                nums[j] = nums[j+1].also {nums[j+1] =  nums[j]}
                swapped = true
            }
        }
        if (swapped==false)
        {
            break
        }
    }
    for(i in 0 until nums.count())
    {
        if (i==nums.count()-1)
        {
            println("${nums[i]}")
            return
        }
        print("${nums[i]}, ")
    }
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.