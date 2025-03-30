---
authors:
- Zia
date: 2025-03-29
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2025-03-29
layout: default
tags:
- base64-encode-decode
- go
title: Base64 Encode Decode in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/go/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"encoding/base64"
	"fmt"
	"os"
)

func die() {
	fmt.Println("Usage: please provide a mode and a string to encode/decode")
	os.Exit(1)
}

func main() {
	if len(os.Args) < 3 {
		die()
	}

	enc := base64.StdEncoding

	if len(os.Args[2]) == 0 {
		die()
	}

	switch os.Args[1] {
	case "encode":
		fmt.Println(enc.EncodeToString([]byte(os.Args[2])))
		return
	case "decode":
		s, err := enc.DecodeString(os.Args[2])
		if err != nil {
			die()
		}

		fmt.Println(string(s))
	default:
		die()
	}
}

```

{% endraw %}

Base64 Encode Decode in [Go](https://sampleprograms.io/languages/go) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).