---
title: Merge Sort in Kotlin
layout: default
date: 2020-10-02
featured-image: merge-sort-in-every-language.jpg
last-modified: 2020-10-02

---

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```kotlin
fun main(args: Array<String>) 
{
    var arr: IntArray
    try
    {
        arr = args[0].split(", ").map{ it.toInt() }.toIntArray()
        if (arr.size < 2) {
            throw Exception()
        }
    }
    catch(e: Exception)
    {
        println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"")
        return
    }

    var ans:IntArray = mergeSort(arr)
    for(i in 0 until ans.count())
    {
        if (i==ans.count()-1)
        {
            println("${ans[i]}")
            return
        }
        print("${ans[i]}, ")
    }
}

fun mergeSort(arr1: IntArray):IntArray
{
    var arr:IntArray = arr1
    if (arr.count() > 1)
    {
        var mid:Int = (arr.count() - 1) / 2
        var left = arr.sliceArray(0..mid)
        var right = arr.sliceArray(mid + 1..arr.count() - 1)
        
        left = mergeSort(left)
        right = mergeSort(right)

        arr = intArrayOf()
        while (left.count() > 0 && right.count() > 0)
        {
            if (left[0] < right[0])
            {
                arr = arr + left.sliceArray(0..0)
                left = left.sliceArray(1..left.count() - 1) 
            }
            else
            { 
                arr = arr + right.sliceArray(0..0)
                right = right.sliceArray(1..right.count() - 1)
            } 
        }
        arr = arr + left + right
    }
    return(arr)
}
```

{% endraw %}

[Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Blake.Ke
- Jeremy Grifski
- mikenmo

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 09 2020 22:39:08. The solution was first committed on Oct 02 2020 04:45:02. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).