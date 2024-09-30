---
authors:
- Blake.Ke
- Jeremy Grifski
- mikenmo
date: 2020-10-01
featured-image: quick-sort-in-every-language.jpg
last-modified: 2020-10-09
layout: default
tags:
- kotlin
- quick-sort
title: Quick Sort in Kotlin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quick-sort/kotlin/how-to-implement-the-solution.md
- sources/programs/quick-sort/kotlin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Kotlin](https://sampleprograms.io/languages/kotlin) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

    var ans:IntArray = quickSort(arr)
    for(i in 0 until ans.count())
    {
        if (i==ans.count() - 1)
        {
            println("${ans[i]}")
            return
        }
        print("${ans[i]}, ")
    }
}

fun quickSort(arr: IntArray):IntArray
{
    if (arr.count() == 1)
    {
        return(arr.sliceArray(0..0))
    }
    var pivot:Int = (arr.count() - 1) / 2 
    arr[pivot] = arr[arr.count() - 1].also {arr[arr.count() - 1] =  arr[pivot]}
    pivot = arr.count()-1

    var ans = intArrayOf()
    var left = intArrayOf()
    for(i in 0 until arr.count())
    {
        if(arr[i] > arr[pivot] || i == pivot)
        {
            for(j in arr.count() - 2 downTo 0)
            {
                if(i>j || j == 0)
                {
                    arr[pivot] = arr[i].also {arr[i] =  arr[pivot]}
                    pivot = i
                    
                    if(pivot!=0){
                        left = arr.sliceArray(0..pivot-1)
                        ans = quickSort(arr.sliceArray(0..pivot - 1))
                        ans = ans + arr.sliceArray(pivot..pivot)
                    }
                    else
                    {
                        ans = arr.sliceArray(pivot..pivot)
                    }
                    if(pivot!=arr.count()-1){
                        ans = ans + quickSort(arr.sliceArray(pivot + 1..arr.count() - 1))
                    }
                    
                    return (ans)
                }
                if(arr[j]<arr[pivot])
                {
                    arr[i] = arr[j].also {arr[j] = arr[i]}
                    break
                }
            }
        }
    }
    return (intArrayOf())
}

```

{% endraw %}

Quick Sort in [Kotlin](https://sampleprograms.io/languages/kotlin) was written by:

- Blake.Ke
- Jeremy Grifski
- mikenmo

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).