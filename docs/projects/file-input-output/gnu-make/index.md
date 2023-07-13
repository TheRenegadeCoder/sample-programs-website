---
authors:
- rzuckerm
date: 2023-07-13
featured-image: file-input-output-in-every-language.jpg
last-modified: 2023-07-13
layout: default
tags:
- file-input-output
- gnu-make
title: File Input Output in Gnu Make
---

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Gnu Make](https://sampleprograms.io/languages/gnu-make) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```gnu_make
define TEXT
Hello from GNU Make
Here are some lines:
This is line 1
This is line 2
Goodbye!
endef

$(file >output.txt,$(TEXT))
$(info $(file <output.txt))

.PHONY: all
all: ;@:

```

{% endraw %}

File Input Output in [Gnu Make](https://sampleprograms.io/languages/gnu-make) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).