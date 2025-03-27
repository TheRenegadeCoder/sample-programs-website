---
authors:
- rzuckerm
date: 2023-07-17
featured-image: fizz-buzz-in-every-language.png
last-modified: 2023-08-12
layout: default
tags:
- fizz-buzz
- gnu-make
title: Fizz Buzz in Gnu Make
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/gnu-make/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/gnu-make/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Gnu Make](https://sampleprograms.io/languages/gnu-make) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```gnu_make
# Numbers are represented as x's so that they can be manipulated with text functions.
# This idea is based on how the GNU Make Standard Library (https://github.com/jgrahamc/gmsl)
# handles numbers.
ZERO :=
ONE := x
TWO := x x
THREE := x x x
FIVE := $(THREE) $(TWO)
TEN := $(FIVE) $(FIVE)
FIFTEEN := $(TEN) $(FIVE)
HUNDRED := $(TEN) $(TEN) $(TEN) $(TEN) $(TEN) $(TEN) $(TEN) $(TEN) $(TEN) $(TEN)

# Is divisible function
# Arg 1: Number encoded as x's
# Arg 2: Divisor encoded as x's
# Return: $(ONE) if divisible, $(ZERO) otherwise
IS_DIVISIBLE = $(if $(strip $(subst $(2),,$(1))),$(ZERO),$(ONE))

# Is less than function
# Arg 1: Number 1 encoded as x's
# Arg 2: Number 2 encoded as x's
# Return: $(ONE) if Number 1 < Number 2, $(ZERO) otherwise
IS_LESS_THAN = $(if $(wordlist $(words $(call INC,$(1))),$(words $(2)),$(2)),$(ONE),$(ZERO))

# Increment function
# Arg 1: Number encoded as x's
# Return: Number + 1 encoded as x's
INC = $(strip $(1) $(ONE))

# Fizz Buzz function
# Arg 1: Number encoded as x's
# Return: One of the following:
# - FizzBuzz if Number is divisible by 15
# - Fizz if Number is divisible by 3
# - Buzz if Number if divisible 5
# - Otherwise, Number converted to decimal representation
FIZZ_BUZZ = $(strip \
    $(if $(call IS_DIVISIBLE,$(1),$(FIFTEEN)),FizzBuzz,\
        $(if $(call IS_DIVISIBLE,$(1),$(THREE)),Fizz,\
            $(if $(call IS_DIVISIBLE,$(1),$(FIVE)),Buzz,$(words $(1)))\
        ) \
    ) \
)

# Fizz Buzz loop
#
# Outputs result of Fizz Buzz function starting at starting number and ending
# at the ending number
#
# Arg 1: Starting number encoded as x's
# Arg 2: Ending number encoded as x's
define FIZZ_BUZZ_LOOP
$(info $(call FIZZ_BUZZ,$(1)))
$(if $(call IS_LESS_THAN,$(1),$(2)),$(call FIZZ_BUZZ_LOOP,$(call INC,$(1)),$(2)))
endef

# Run Fizz Buzz loop from 1 to 100
$(call FIZZ_BUZZ_LOOP,$(ONE),$(HUNDRED))

.PHONY: all
all: ;@:

```

{% endraw %}

Fizz Buzz in [Gnu Make](https://sampleprograms.io/languages/gnu-make) was written by:

- rzuckerm

This article was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

### Introduction

GNU Make has very few functions that accept or return numbers, so doing
anything that requires math is challenging. After doing some Google searches,
I discovered the [GNU Make Standard Library][1]. This library does some
amazing things with the functions available in GNU Make. I studied the code,
and the way they handle numbers is to convert them with a sequence of `x`'s
separated by spaces. In other words, the number `n` is represented as
`n` `x`'s separated by spaces. For `0`, an empty string is used. For example,
`5` would be represented like this:

```
x x x x x
```

Before we start digging into the code, let's explain some concepts and
built-in functions that will be used in this code sample.

### Immediate vs. Deferred Assignment

Throughout the code, there are [two types of assignment][2]:

* `:=` means immediate assignment.
* `=` means deferred assignment.

As the name implies, immediate assignment means the value of the variable
is assigned immediately, and any variables referenced are immediately
expanded. For example:

```make
HELLO := hello
WORLD := world
HELLO_WORLD := $(HELLO) $(WORLD)
```

For the above, the value of `HELLO` is the string `hello`, the value of
`WORLD` is the string `world`. The variable `HELLO_WORLD` is the value
of `HELLO`, a space, and then the value of `WORLD` -- i.e., the string
`hello world`.

### User-Defined Functions

A user-defined function is set up as a variable with a deferred assignment.
Function arguments are represented as the one-based argument number enclosed
in `$()` -- e.g., `$(2)` is the second argument. The [call][3] function is
used to invoked these functions. For example. let's set up this function:

```make
GREET = $(1), $(2). How are you?
```

This function takes two argument: a greeting and a name. It returns a value
that is equal to the first argument, a comma, a space, the second argument,
and `. How are you?`.

We would call this function like this:

```make
GREETING := $(call GREET,Hello,Joe Smith)
```

The first argument is `Hello`, and the second argument is `Joe Smith`. This
would set the variable `GREETING` to the value of
`Hello, Joe Smith. How are you?`.

### Built-In Numeric Functions

There are a few functions in GNU Make that handle numbers. Of those, only
the following are used:

* [wordlist][5]
* [words][6]

### wordlist Function

First, let's take a look at the [wordlist][5] function. This function takes
three arguments:

1. The one-based starting index. Let's call this `s`.
2. The one-based ending index. Let's call this `e`.
3. A space-separated list.

It returns a space-separated list that contains elements `s` through `e`
(inclusive) of the original list. These values are constrained to the length
of the list. For the case where `s` is greater than `e`, an empty string is
returned.

For example, let's create a variable called `SOME_LIST` with 5 elements:

```make
SOME_LIST := first second third fourth fifth
```

If you did this:

```make
ANSWER1 := $(wordlist 2,4,$(SOME_LIST))
```

Then, `ANSWER1` would equal `two three four`, which is the 2nd through 4th
element.

If you did this:

```make
ANSWER2 := $(wordlist 4,1000,$(SOME_LIST))
```

Then, `ANSWER2` would equal `four five`, which is the 4th and 5th element
since the value returned by `wordlist` stops at the last element.

If you did any of these:

```make
ANSWER3A := $(wordlist 6,7,$(SOME_LIST))
ANSWER3B := $(wordlist 5,4,$(SOME_LIST))
```

Then, you would get an empty string because:

* For `ANSWER3A`, there is no 6th element.
* For `ANSWER3B`, `5` is greater than `4`.

#### words Function

The [words][6] function accepts a single argument: a space-separated list. The
function returns the number of elements in that list. For example:

* `$(words a b c)` returns `3`
* `$(words)` returns `0`

### Built-In Conditional Function

The [if][7] function is a conditional function that returns one of two
values: one for the "true" case, one for the "false" case. It take three
arguments:

1. The value to compare
2. The value to return if "true"
3. The value to return if "false"

A value is considered "true" if it is non-empty. For example:

```make
$(if $(SOME_VALUE),It's True,It's False)
```

If that value of the variable `SOME_VALUE` is non-empty, then `It's True` is
returned. Otherwise, `It's False` is returned.

### Numbers

This code sets up the numbers that are used in the Fizz Buzz algorithm:

```make
ZERO :=
ONE := x
TWO := x x
THREE := x x x
FIVE := $(THREE) $(TWO)
TEN := $(FIVE) $(FIVE)
FIFTEEN := $(TEN) $(FIVE)
HUNDRED := $(TEN) $(TEN) $(TEN) $(TEN) $(TEN) $(TEN) $(TEN) $(TEN) $(TEN) $(TEN)
```

From the names, it's obvious as to which number each variable represents --
e.g., `FIVE` (which is effectively `THREE` plus `TWO`) is 5 `x`'s separated by
spaces.

### Math Functions

A number of math functions are needed in order to support the Fizz Buzz
algorithm:

* Increment (`INC`)
* Is less than (`IS_LESS_THAN`)
* Is divisible by (`IS_DIVISIBLE_BY`)

#### INC Function

Let's look at the `INC` function first since it is the simplest, and it is
used elsewhere. It takes a single argument which is a number represented as
`x`'s and returns the number plus one represented as `x`'s. Here the function:

```make
INC = $(strip $(1) $(ONE))
```

Incrementing just involves append a space and a single `x` (the value of
`ONE`) to the passed in argument. The [strip][4] function removes leading
and trailing whitespace. This is needed for the case whether the argument has
the value of zero, which is an empty string. Without this, ` x` would be
returned instead of just `x`.

#### IS_LESS_THAN Function

The `IS_LESS_THAN` function takes a two arguments which are numbers
represented as `x`'s and returns a `$(ONE)` (which is `x`) as a true value,
and `$(ZERO)` (which is empty) as a false value. Here is the function:

```make
IS_LESS_THAN = $(if $(wordlist $(words $(call INC,$(1))),$(words $(2)),$(2)),$(ONE),$(ZERO))
```

Whoa! That's a lot to digest here! Let's break it down. Effectively, the way
this works if to remove each item in the first argument from the second until
the first or second argument is exhausted, whichever comes first. When the
first argument is less than the second, a non-empty list will remain, and
`$(ONE)` is returned. Otherwise, it will be an empty list, and `$(ZERO)` is
returned.

Let's work through a couple of examples. Let `ARG1` be `3` and `ARG2` be `5`,
each represented as `x`'s:

```make
ARG1 := x x x
ARG2 := x x x x x
RESULT := $(call IS_LESS_THAN,$(ARG1),$(ARG2))
```

For this case `$(words $(call INC,$(ARG1)))` is `4` (`3 + 1`), and
`$(words $(ARG2))` is `5`, so `$(wordlist 4,5,$(ARG2))` can be visualized as
the right-hand side of this:

```
1 2 3 | 4 5
x x x | x x
```

Since the result is non-empty, `$(ONE)` is returned.

Let's work through the reverse of the previous example:

```make
ARG1 := x x x x x
ARG2 := x x x
RESULT := $(call IS_LESS_THAN,$(ARG1),$(ARG2))
```

For this case `$(words $(call INC,$(ARG1)))` is `6`, and `$(words $(ARG2))` is
`3`, so `$(wordlist 6,3,$(ARG2))` can be visualized as the right-hand side of
this:

```
1 2 3 | 4 5 6
x x x |
```

Since the result is empty, `$(ZERO)` is returned.

#### IS_DIVISIBLE_BY Function

The `IS_DIVISIBLE_BY` function take two arguments:

* Dividend represented as `x`'s
* Divisor represented as `x`'s

If the dividend is divisible by the divisor, `$(ONE)` is returned. Otherwise,
`$(ZERO)` is returned. Here is the function:

```make
IS_DIVISIBLE_BY = $(if $(strip $(subst $(2),,$(1))),$(ZERO),$(ONE))
```

While this isn't as scary as the `IS_LESS_THAN` function, there is an
interesting trick at work here. The [subst][8] take three arguments:

1. The search string
2. The replace string
3. The string to modify

This is used to remove all instances of the divisor from the dividend. If the
result is non-empty, then the dividend is not divisible by the divisor.
Otherwise, it is divisible.

Let's work through a couple of examples. Let `ARG1` be `8` and `ARG2` be `3`,
each represented as `x`'s:

```
ARG1 := x x x x x x x x
ARG2 := x x x
RESULT := $(call IS_DIVISIBLE_BY,$(ARG1),$(ARG2))
```

The `subst` function would look like this:

```make
$(subst x x x,,x x x x x x x x)
```

In other words, substitute 3 `x`'s with nothing. The return value of `subst`
would be the right-most side of this:

```
1 2 3 | 4 5 6 | 7 8
x x x | x x x | x x
```

Since this is non-empty (`x x`), the return value of `IS_DIVISIBLE_BY` is
`$(ZERO)`.

Let's change `ARG1` to `9` represented as `x`'s:

```make
ARG1 := x x x x x x x x x
ARG2 := x x x
RESULT := $(call IS_DIVISIBLE_BY,$(ARG1),$(ARG2))
```

For this case, the right-most side of `subst` would be this:

```
1 2 3 | 4 5 6 | 7 8 9 |
x x x | x x x | x x x |
```

Since this is empty, the return value of `IS_DIVISIBLE_BY` is `$(ONE)`.

### The Fizz Buzz Algorithm

Finally, we're at the meat of the matter! Thanks for sticking with me so far.

#### FIZZ_BUZZ Function

The `FIZZ_BUZZ` function takes a single argument that is a number represented
as `x`'s. Let's call this argument `n`. This function returns on of the following:

* If `n` is divisible by 3 and 5 (i.e., 15), return `FizzBuzz`.
* Else if `n` is divisible by 3, return `Fizz`.
* Else if `n` is divisible by 5, return `Buzz`.
* Else return `n` represented as a regular number.

Here is the implementation:

```make
FIZZ_BUZZ = $(strip \
    $(if $(call IS_DIVISIBLE,$(1),$(FIFTEEN)),FizzBuzz,\
        $(if $(call IS_DIVISIBLE,$(1),$(THREE)),Fizz,\
            $(if $(call IS_DIVISIBLE,$(1),$(FIVE)),Buzz,$(words $(1)))\
        ) \
    ) \
)
```

The `strip` function is needed to remove any extraneous spaces that are added
by the formatting of the code, which is done for readability. The `words`
function is needed to convert the argument into a regular number.

#### FIZZ_BUZZ_LOOP Function

The `FIZZ_BUZZ_LOOP` function has two arguments: the starting and end numbers
represented as `x`'s. Here is the function:

```make
define FIZZ_BUZZ_LOOP
$(info $(call FIZZ_BUZZ,$(1)))
$(if $(call IS_LESS_THAN,$(1),$(2)),$(call FIZZ_BUZZ_LOOP,$(call INC,$(1)),$(2)))
endef
```

The [define][10] keyword assigns a multi-line value to a variable. The value
is terminated with an `endef` keyword. The [info][9] function takes a single
value: the value to be displayed.

Here is what this function would look like in pseudocode:

```
function FIZZ_BUZZ_LOOP(start, end)
    display FIZZ_BUZZ(start)
    if start < end:
        call FIZZ_BUZZ_LOOP(start + 1, end)
```

You'll notice that this is using recursion. That is the only way to implement
loops in GNU Make.

#### The Final Step

In order to make all this run the Fizz Buzz algorithm and display results, one
final piece is needed, and that is to call `FIZZ_BUZZ_LOOP` with a starting
value of 1 (`$(ONE)`) and ending value of 100 (`$(HUNDRED)`):

```make
$(call FIZZ_BUZZ_LOOP,$(ONE),$(HUNDRED))
```

And that's it! Wow, that was exhausting! I think I'll take a nap now.

[1]: https://github.com/jgrahamc/gmsl
[2]: https://www.gnu.org/software/make/manual/html_node/Reading-Makefiles.html
[3]: https://www.gnu.org/software/make/manual/html_node/Call-Function.html
[4]: https://www.gnu.org/software/make/manual/html_node/Text-Functions.html#index-stripping-whitespace
[5]: https://www.gnu.org/software/make/manual/html_node/Text-Functions.html#index-wordlist
[6]: https://www.gnu.org/software/make/manual/html_node/Text-Functions.html#index-words
[7]: https://www.gnu.org/software/make/manual/html_node/Conditional-Functions.html#index-if-1
[8]: https://www.gnu.org/software/make/manual/html_node/Text-Functions.html#index-subst-1
[9]: https://www.gnu.org/software/make/manual/html_node/Make-Control-Functions.html#index-info
[10]: https://www.gnu.org/software/make/manual/html_node/Multi_002dLine.html


## How to Run the Solution

To run this program, download and install the latest GNU Make using these
instructions:

* [Windows][11]
* For [Linux][12], see "How to Download" section
* [Mac][13]

Download a copy of [Fizz Buzz in GNU Make][14], and run this command:

```
make -sf fizz-buzz.mk
```

[11]: https://leangaurav.medium.com/how-to-setup-install-gnu-make-on-windows-324480f1da69
[12]: https://www.incredibuild.com/integrations/gnu-make
[13]: https://formulae.brew.sh/formula/make
[14]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/g/gnu-make/fizz-buzz.mk
