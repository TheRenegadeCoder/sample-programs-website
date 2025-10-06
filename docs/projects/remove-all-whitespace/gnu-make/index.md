---
authors:
- rzuckerm
date: 2025-10-05
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2025-10-05
layout: default
tags:
- gnu-make
- remove-all-whitespace
title: Remove All Whitespace in Gnu Make
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/gnu-make/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/gnu-make/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Gnu Make](https://sampleprograms.io/languages/gnu-make) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```gnu_make
USAGE := Usage: please provide a string

# Constants
EMPTY :=
SPACE := $(EMPTY) $(EMPTY)

# Note that this is non-portable, but it's the only way I could get a carriage return
# assigned to a variable
CR := $(shell printf '\r')

# Remove all whitespace
#
# Note that GNU Make automatically converts tab and newline ('\n') to a space and
# that leading and trailing whitespace are ignore, so all that needs to be done
# is to remove carriage return (`\r') and space.
#
# Arg 1: The string
# Return: The string without whitespace
REMOVE_ALL_WHITESPACE = $(subst $(CR),,$(subst $(SPACE),,$(1)))

# If string not provided, display usage statement
# Else display string without whitespace
ifeq (,$(ARGV1))
$(info $(USAGE))
else
NUMBER := $(call CONVERT_NUMBER,$(strip $(ARGV1)))
$(info $(call REMOVE_ALL_WHITESPACE,$(ARGV1)))
endif

.PHONY:
all: ;@:

```

{% endraw %}

Remove All Whitespace in [Gnu Make](https://sampleprograms.io/languages/gnu-make) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).