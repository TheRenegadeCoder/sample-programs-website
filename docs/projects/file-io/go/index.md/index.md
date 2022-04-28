# File Io in Go

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Go
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.