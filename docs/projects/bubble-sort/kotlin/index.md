---
title: Bubble Sort in Kotlin
layout: default
date: 2020-10-01
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2020-10-01

---

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
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

[Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Blake.Ke
- Jeremy Grifski
- mikenmo

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 09 2020 23:34:00. The solution was first committed on Oct 01 2020 16:33:59. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).