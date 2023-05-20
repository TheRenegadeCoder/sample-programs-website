---
title: Bubble Sort in Go
layout: default
last-modified: 2020-09-30
featured-imaged: bubble-sort-in-every-language.jpg
tags: [go, bubble-sort]
authors:
  - bracciata

---

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
    "encoding/json"
    "fmt"
    "os"
    "regexp"
    "strconv"
    "strings"
)

func bubbleSort(list []int) []int {
    swapped := true
    for swapped {
        swapped = false
        for i := 0; i < len(list)-1; i++ {
            if list[i] > list[i+1] {
                n := list[i]
                list[i] = list[i+1]
                list[i+1] = n
                swapped = true
            }
        }
    }
    return list
}

func strToSliceInt(strList string) []int {
    list := regexp.MustCompile(", ?").Split(strList, -1)
    if len(list) < 2 {
        exitWithError()
    }
    var nums []int
    for _, num := range list {
        n, err := strconv.Atoi(num)
        if err != nil {
            exitWithError()
        }
        nums = append(nums, n)
    }
    return nums
}

func sliceIntToString(list []int) (out string) {
    bytes, _ := json.Marshal(list)
    out = strings.Replace(string(bytes), ",", ", ", -1)
    out = strings.Trim(out, "[]")
    return
}

func exitWithError() {
    fmt.Println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"")
    os.Exit(1)
}

func main() {
    if len(os.Args) != 2 {
        exitWithError()
    }

    nums := strToSliceInt(os.Args[1])
    nums = bubbleSort(nums)
    fmt.Println(sliceIntToString(nums))
}
```

{% endraw %}

[Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Go](https://sampleprograms.io/languages/go) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 25 2019 19:45:18. The solution was first committed on Mar 05 2019 12:01:36. As a result, documentation below may be outdated.

## How to Implement the Solution

At this point, let's dig into the code a bit. The following sections break
down the Bubble Sort in Go functionality.

### The Main Function

Breaking down this solution bottom up,

```go
func main() {
    if len(os.Args) != 2 {
        exitWithError()
    }

    nums := strToSliceInt(os.Args[1])
    nums = bubbleSort(nums)
    fmt.Println(sliceIntToString(nums))
}
```
This is the `main` function of this file. It parses the form `Args`, assures that there is enough elements for it to be sorted, the converts the string to integers, then calls our bubble sort function, and finally prints the results.
It also deals with any errors raised.

### Transform Input Parameters

```go
func strToSliceInt(strList string) []int {
    list := regexp.MustCompile(", ?").Split(strList, -1)
    if len(list) < 2 {
        exitWithError()
    }
    var nums []int
    for _, num := range list {
        n, err := strconv.Atoi(num)
        if err != nil {
            exitWithError()
        }
        nums = append(nums, n)
    }
    return nums
}
```

This function takes a string like `"2, 1, 10, 5, 3"`, and turns into a list of numbers.
First we need to convert our string into a
list `Split(strList, -1)` which is a list of strings split by comma (,). So our
original input string becomes `["2", " 1", " 10", " 5", " 3"]`.
Then for each element in the list `for _, num := ...` ,  we do something to it.

In this example we convert it into a decimal integer, `strconv.Atoi(num)`. After that each of the newly converted integers are converted added to the new list `nums`.

### Transform Output Result

```go
func sliceIntToString(list []int) (out string) {
    bytes, _ := json.Marshal(list)
    out = strings.Replace(string(bytes), ",", ", ", -1)
    out = strings.Trim(out, "[]")
    return
}
```

This function takes a list of integers like `[2, 1, 10,  5, 3]`, and turns into a string.
First we need to convert our list of integers into a
string `bytes, _ := json.Marshal(list)`. So our
original input string becomes `"[2,1,10,5,3]"`.
Then we replace the commas with commas and a space `"[2, 1, 10, 5, 3]"`. Finally, we remove the square brackets before returning the string `out = strings.Trim(out, "[]")`.


### Throw Errors

```go
func exitWithError() {
    fmt.Println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"")
    os.Exit(1)
}
```

This function prints a message and then exits the script with an error, `os.Exit(1)`.
If any non-zero value is returned then the program didn't complete properly.
This function is called if the user input isn't correct.

### Bubble Sort

```go
func bubbleSort(list []int) []int {
    swapped := true
    for swapped {
        swapped = false
        for i := 0; i < len(list)-1; i++ {
            if list[i] > list[i+1] {
                n := list[i]
                list[i] = list[i+1]
                list[i+1] = n
                swapped = true
            }
        }
    }
    return list
}
```

Finally we're at the real meat and potatoes of the script. This function takes an unsorted integer
list and returns a sorted list, using the bubble sort algorithm. This function `bubbleSort` has two nested for loops inside of it. The `for swapped` loop will run as long as the variable gets swapped in each run of the loop. The `for` loop nested inside will run from the first element in the list (`i=0`) to the last minus one (`len(list)-1`). As it runs through it compares every element to the one after it and if it is larger it swaps them

```go
n := list[i]
list[i] = list[i+1]
list[i+1] = n
```

After that it marks `swapped` as true to notify the outer loop it should keep running. If `swapped` was not changed to `true` the list would stop there because it checked every element and determined none of them needed to be moved.

For example, if `[3, 2, 5, 1]` is the input:

* First we compare 3 and 2
* 3 is greater than 2
* Store 3 to a temporary variable: `n := list[i]`
* Places 2 where 3 was: `list[i] = list[i+1]`
* Places 3 where 2 was: `list[i+1] = n`

* Next we compare 3 and 5
* Nothing happens because 5 is greater than 3.

* First we compare 5, 1
* 5 is greater than 1
* Store 5 to a temporary variable: `n := list[i]`
* Places 1 where 5 was: `list[i] = list[i+1]`
* Places 5 where 1 was: `list[i+1] = n`

At this point, `list` is `[2, 3, 1, 5]`. The process repeats starting at the beginning of the list until there are no more items to swap:

* `[2, 3, 1, 5]` becomes `[2, 1, 3, 5]`
* `[2, 1, 3, 5]` becomes `[1, 2, 3, 5]`, and we're done


## How to Run the Solution

If we want to run this program, we should probably download a copy of [Bubble Sort in Go](https://github.com/TheRenegadeCoder/sample-programs/blob/master/archive/g/go/bubble-sort.go).
After that, we should make sure we have the latest Go interpreter.
From there, we can run the following command in the terminal:

`go run bubble-sort.go "3, 2, 10, 6, 1, 7"`

Alternatively, we can copy the solution into an online Go interpreter and hit run.
