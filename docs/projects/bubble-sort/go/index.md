---

title: Bubble Sort in Go
layout: default
last-modified: 2020-09-30
featured-image: bubble-sort-in-every-language.jpg
tags: [go, bubble-sort]
authors:
  - bracciata

---

Welcome to the Bubble Sort in Go page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Go
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

## How to Implement the Solution

At this point, let's dig into the code a bit. The following sections break
down the Bubble Sort in Go functionality.

### Solution

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

func swap(list []int, firstIndex int, secondIndex int) bool {
	if list[firstIndex] > list[secondIndex] {
		x := list[firstIndex]
		list[firstIndex] = list[secondIndex]
		list[secondIndex] = x
		return true
	}
	return false
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
This is the main function of this file. It parses the  form Args, assures that there is enough elements for it to be sorted, the converts the string to integers, then calls our bubble sort function, and finally prints the results.
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
It does this using a list comprehension, first we need to convert our string into a
list `Split(strList, -1)` which is a list of strings split by comma (,). So our
original input string becomes `["2", " 1", " 10", " 5", " 3"]`.
Then for each element in the list `for _, num := ...` ,  we do something to it.

In this example we convert it into a decimal integer, `strconv.Atoi(num)`. After that each of the newly converted integers are converted added to the new list `nums`.

```go
func sliceIntToString(list []int) (out string) {
	bytes, _ := json.Marshal(list)
	out = strings.Replace(string(bytes), ",", ", ", -1)
	out = strings.Trim(out, "[]")
	return
}
```

This function takes a list of integers like `[2, 1, 10,  5, 3]`, and turns into a string.
It does this using a list comprehension, first we need to convert our list of integers into a
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

This function prints a message and then exits the script with an error, `os.exit(1)`.
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
list and returns a sorted list, using the bubble sort algorithm. This function `bubbleSort` has two nested for loops inside pof it. For swapped will run as long as the variable gets swapped in each run of the loop. The for loop nested inside will  run from the first element in the list(`i=0`) to the last minus one(`len(list)-1`). As it runs through it compares every element to the one after it and if it is larger it swaps them `n := list[i]
				list[i] = list[i+1]
				list[i+1] = n` and after that it marks swapped true to notify the outer loop it should keep running. If stopped were not changed to true the list would stop there because it checked every element and determined none of them needed to be moved.

For example, if `[3, 2, 5, 1]` is the input:

* First we compare 2, 3
* 2 < 3
* Store 2 to a temporary variable `n:=list[i]`
* Places two where three was `list[i] = list[i+1]`
* Places three where two was `list[i+1] = n`


* Next we compare 3 and 5
* Nothing happens because 5 is greater than 3.

* This repeats for the rest of the list and then restarts back to two at the start because one element was swapped this time through.

* Compare 3, 5
* 3 < 5
* This time we don't delete 3, we then pass every element of the list except the first one (3) `xs[1:]`
* Call `pass_list` `[3] + pass_list(5,1)`.



* For input `[10, 3, 2, 5, 7]` output is `[3, 2, 5, 7, 10]`
* Then input `[3, 2, 5, 7, 10]` output is `[2, 3, 5, 7, 10]`
* Then input is `[2, 3, 5, 7, 10]` output is `[2, 3, 5, 7, 10]`
* ...


## How to Run the Solution

If we want to run this program, we should probably download a copy of [Bubble Sort in Go](https://github.com/TheRenegadeCoder/sample-programs/blob/master/archive/g/go/bubble-sort.go).
After that, we should make sure we have the latest Go interpreter.
From there, we can run the following command in the terminal:

`go run bubble-sort.go "3, 2, 10, 6, 1, 7"`

Alternatively, we can copy the solution into an online Go interpreter and hit run.
