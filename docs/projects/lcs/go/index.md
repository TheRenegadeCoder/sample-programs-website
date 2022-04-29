---

title: LCS in Go
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the LCS in Go page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

func lcs(list1 []int, list2 []int) (lcsList []int) {
	if len(list1) <= 0 || len(list2) <= 0 {
		return
	}
	if list1[0] == list2[0] {
		return append(lcs(list1[1:], list2[1:]), list1[0])
	}
	return longest(lcs(list1, list2[1:]), lcs(list1[1:], list2))
}

func longest(list1 []int, list2 []int) []int {
	if len(list1) > len(list2) {
		return list1
	}
	return list2
}

func reverse(list []int) (reversed []int) {
	for i := len(list) - 1; i >= 0; i-- {
		reversed = append(reversed, list[i])
	}
	return
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

func exitWithError() {
	fmt.Println("Usage: please provide two lists in the format \"1, 2, 3, 4, 5\"")
	os.Exit(1)
}

func sliceIntToString(list []int) (out string) {
	bytes, _ := json.Marshal(list)
	out = strings.Replace(string(bytes), ",", ", ", -1)
	out = strings.Trim(out, "[]")
	return
}

func main() {
	if len(os.Args) != 3 {
		exitWithError()
	}

	list1 := strToSliceInt(os.Args[1])
	list2 := strToSliceInt(os.Args[2])
	fmt.Println(sliceIntToString(reverse(lcs(list1, list2))))
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.