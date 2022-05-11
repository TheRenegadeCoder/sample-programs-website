---

title: File Io in Go
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the File Io in Go page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```go
package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

func read() (string, error) {
	contents, err := ioutil.ReadFile("output.txt")
	return string(contents), err
}

func write(contents string) error {
	return ioutil.WriteFile("output.txt", []byte(contents), 0644)
}

func main() {
	err := write("file contents")
	if err != nil {
		log.Fatal(err)
	}
	contents, err := read()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(contents)
}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).