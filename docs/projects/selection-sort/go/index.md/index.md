---

---

Welcome to the Selection Sort in Go page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Go
package main

import (
	"encoding/json"
	"fmt"
	"math"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func selectionSort(unsorted []int, sorted ...int) []int {
	if len(unsorted) <= 0 {
		return sorted
	}
	if len(unsorted) == 1 {
		return append(sorted, unsorted...)
	}

	min := math.MaxInt32
	minI := -1
	for i, n := range unsorted {
		if n < min {
			min = n
			minI = i
		}
	}
	sorted = append(sorted, min)
	unsorted = append(unsorted[:minI], unsorted[minI+1:]...)
	return selectionSort(unsorted, sorted...)
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
	nums = selectionSort(nums)
	fmt.Println(sliceIntToString(nums))
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.