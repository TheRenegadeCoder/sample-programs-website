### Introduction

GNU Make is not a language that has much support for numerical operations.
Instead, numbers have to be represented as a space-separated list of `x`'s.
For example, 0 is an empty string and 6 is `x x x x x x`. I can't claim to
have thought of this on my own. The idea is based on the
[GNU Make Standard Library][1].

Before looking at the code, there's a few concepts that need to be explained
first.

### Immediate vs. Deferred Assignment

Throughout the code, there are [two types of assignment][2]:

* `:=` means immediate assignment.
* `=` means deferred assignment.

As the name implies, immediate assignment assigns the value to the variable
right away. This is typically used for constants. Deferred assignment is only
evaluated when it is needed. Until then, the variable just equals the
expression. This can be used to create user-defined functions.

### User-Defined Functions

User-defined functions are done using deferred assignment. The arguments of
a user-defined function are one-based argument numbers enclosed in `$()`. For
example, `$(3)` is the third argument.

These functions are invoked using the [call][3] function. The first argument
of the `call` function is the variable name that contains the function. The
remaining arguments are the arguments to pass to the user-defined function.

### Built-In Numeric Functions

GNU has a few functions that deal with numbers:

* [words][4]
* [wordlist][5]

#### words Function

The `words` function accepts a single argument which is a space-separated list.
It just returns the number of elements in that list.

#### wordlist Function

The `wordlist` function accepts three arguments:

1. One-based starting index. Let's call this `s`.
2. One-based ending index. Let's call this `e`.
3. A space-separated list

The function returns element `s` through element `e` of the list. The `s` and
`e` arguments are constrained by the size of the list. In other words, the
`wordlist` function will not go past the end of the list. If `e` is less than
`s`, an empty string is returned.

### Built-In Conditional Function

The [if][6] function is a conditional function that returns one of two values:
one for the "true" case, and one for the "false" case. This function takes
three arguments:

1. The value to compare
2. The value to return if "true"
3. The value to return if "false"

A value is considered "true" if it is not empty, "false" otherwise.

### Constants

The Baklava algorithm requires displaying spaces and asterisks (stars).
Therefore, these constants are defined:

```make
EMPTY :=
SPACE := $(EMPTY) $(EMPTY)
STAR := *
```

Since GNU Make ignores leading and trailing spaces in variable assignments, in
order to get a variable to assigned to a space (`SPACE`), the space needs to
be sandwiched between an empty variable (`EMPTY`). The `STAR` variable just
contains a single star.

### Numbers

This code sets the numbers that are needed to implement the Baklava algorithm:

```make
ONE := x
TWO := x x
TEN := $(TWO) $(TWO) $(TWO) $(TWO) $(TWO)
```

`TEN` is just five copies `TWO` (effectively 2 times 5).

### Math Functions

A number of math functions are needed to implement the Baklava algorithm:

* Increment (`INC`)
* Decrement (`DEC`)
* Add (`ADD`)
* Subtract (`SUB`)

#### INC Function

The `INC` function takes a single value and returns that value plus one. The
values are represents as space-separated `x`'s, so all that needs to be done
is to append a single `x`:

```make
INC = $(strip $(1) $(ONE))
```

The [strip][7] function just removes leading and trailing spaces. It is needed
for the case where the argument is an empty string (0). If this function were
not added, ` x` would be returned instead of `x`.

#### DEC Function

The `DEC` function takes a single value (let's call this `n`) represented as
`x`'s. It returns that value minus 1, limited to be no less than zero since
negative numbers cannot be represented. All that needs to be done is to remove
a single `x`:

```make
DEC = $(wordlist 2,$(words $(1)),$1)
```

The above returns element 2 through `n` (using the `wordlist` function), where
The value of `n` is returned using the `words` function. For example, if the
value is 3 (`x x x`), then 2 (`x x`) is returned.

#### ADD Function

The `ADD` function takes two values and returns the sum of them. All that
needs to be done is to concatenate the two values:

```make
ADD = $(strip $(1) $(2))
```

The `strip` function removes leading or trailing spaces for the case where
either argument is an empty string (0). If this were not done then 0 plus
2 would be ` x x` instead of `x x`, and 2 plus 0 would be `x x ` instead
of `x x`.

#### SUB Function

The `SUB` function takes two values (let's call these `a` and `b`) and returns
the first value minus the second value, limited to be no less than zero since
negative numbers cannot be represented. All that needs to be done is the
remove the second value from the first:

```make
$(wordlist $(words $(call INC,$(2))),$(words $(1)),$(1))
```

This is similar to what the `DEC` function does, but instead of starting 2, it
starts at `a + 1`. Note that the second argument is incremented due to the
fact that one-base indexes are used. For example, let say that `a` is 5
(`x x x x x`), and `b` is 3 (`x x x`), then element 4 (`3 + 1`) through 5 is
returned, which are the 2 (`x x`) right-most elements:

```
1 2 3 | 4 5
x x x | x x
```

### REPEAT Function

The `REPEAT` function takes two argument:

1. The character to repeat
2. The number of times to repeat the character (`n`) represented as `x`'s

The function returns the character repeated the specified number of times:

```make
REPEAT = $(subst $(1)$(SPACE),$(1),$(foreach _,$(2),$(1)))
```

Let's break this down starting with the [foreach][8] function. This function
takes three arguments:

1. A variable name
2. A space-separated list
3. A text value

It returns a space-separated list that contains the text value for each item
in the list. In this case, the variable `_` is unused. The list is `n`
represented as `x`'s. The text is the character to repeat. What this will do
is repeat the character `n` times separated by spaces. For example, if `n` is
7 (`x x x x x x x`) and the character is `*`, then `* * * * * * *` would be
returned.

Since we don't want those extra spaces, we need to remove them. However, we
have to be smart about it. We can't just remove all spaces. If the character
is ` `, then `foreach` will return `2*n - 1` spaces, and removing all the
spaces would return in a empty string instead of `n` spaces. Therefore,
the [subst][9] function is used. This function takes three arguments:

1. The search string
2. The replace string
3. The string to modify

This is used to change the character plus a space to just the character.

### The Baklava Algorithm

All the above is used to display the Baklava pattern, which is a diamond shape
composed of lines of spaces and stars.

#### BAKLAVA_LINE Function

This function takes two arguments:

1. The number of spaces represented as `x`'s
2. The number of stars represented as `x`'s

This function returns the requested number of spaces concatenated with the
requested number of stars:

```make
BAKLAVA_LINE = $(call REPEAT,$(SPACE),$(1))$(call REPEAT,$(STAR),$(2))
```

This is done with the `REPEAT` function.

#### UPPER_BAKLAVA_LOOP Function

This function displays the upper triangle of the Baklava. It takes two
arguments:

1. The starting number of spaces represented as `x`'s. Let's call this `num_spaces`.
2. The starting number of stars represented as `x`'s. Let's call this `num_stars`.

Here is the function:

```make
define UPPER_BAKLAVA_LOOP
$(info $(call BAKLAVA_LINE,$(1),$(2)))
$(if $(1),$(call UPPER_BAKLAVA_LOOP,$(call DEC,$(1)),$(call ADD,$(2),$(TWO))))
endef
```

The [define][10] keyword assigns a multi-line value to a variable. The value
is terminated with an `endef` keyword. The [info][11] function takes a single
value: the value to be displayed.

Here's what the function looks like in pseudo-code:

```
function UPPER_BAKLAVA_LOOP(num_spaces, num_stars)
    display BAKLAVA_LINE(num_spaces, num_starts)
    if num_spaces is not 0:
        call UPPER_BAKLAVA_LOOP(num_spaces - 1, num_stars + 2)
```

You'll notice that this is using recursion. That is the only way to implement
loops in GNU Make. Here, each successive loop decreases the number of spaces
displayed by one and increases the number of stars displayed by two until the
number of spaces is zero.

#### LOWER_BAKLAVA_LOOP Function

This function displays the lower triangle of the Baklava. It takes two
arguments:

1. The starting number of spaces represented as `x`'s. Let's call this
  `num_spaces`.
2. The starting number of stars represented as `x`'s. Let's call this
   `num_stars`.

Here is the function:

```make
define LOWER_BAKLAVA_LOOP
$(if $(2),\
    $(info $(call BAKLAVA_LINE,$(1),$(2)))\
    $(call LOWER_BAKLAVA_LOOP,$(call INC,$(1)),$(call SUB,$(2),$(TWO)))\
)
endef
```

Here's what the function looks like in pseudo-code:

```
function LOWER_BAKLAVA_LOOP(num_spaces, num_stars)
    if num_stars is not zero:
        display BAKLAVA_LINE(num_spaces, num_stars)
        call LOWER_BAKLAVA_LOOP(num_spaces + 1, num_stars - 2)
```

Once again, recursion. Here, while the number of stars is non-zero, each
successive loop increases the number of spaces displayed by one, and decreases
the number of stars displayed by two. This is exactly the opposite of what
`LOWER_BAKLAVA_LOOP` does.

#### The Final Step

In order to run the Baklava algorithm and display the results, the two Baklava
loops must be invoked with the correct starting number of spaces and stars.
Since there are 10 (`$(TEN)`) spaces and 1 (`$(ONE)`) star on the first row of
the upper triangle, `UPPER_BAKLAVA_LOOP` is called like this:

```make
$(call UPPER_BAKLAVA_LOOP,$(TEN),$(ONE))
```

Since there is 1 (`$(ONE)`) space and 19 (`10*2 - 1`) stars on the first row
of the lower triangle, `LOWER_BAKLAVA_LOOP` is called list this:

```make
$(call LOWER_BAKLAVA_LOOP,$(ONE),$(call DEC,$(call ADD,$(TEN),$(TEN))))
```

That's all there is to it!

[1]: https://github.com/jgrahamc/gmsl
[2]: https://www.gnu.org/software/make/manual/html_node/Reading-Makefiles.html
[3]: https://www.gnu.org/software/make/manual/html_node/Call-Function.html
[4]: https://www.gnu.org/software/make/manual/html_node/Text-Functions.html#index-words
[5]: https://www.gnu.org/software/make/manual/html_node/Text-Functions.html#index-wordlist
[6]: https://www.gnu.org/software/make/manual/html_node/Conditional-Functions.html#index-if-1
[7]: https://www.gnu.org/software/make/manual/html_node/Text-Functions.html#index-stripping-whitespace
[8]: https://www.gnu.org/software/make/manual/html_node/Foreach-Function.html
[9]: https://www.gnu.org/software/make/manual/html_node/Text-Functions.html#index-subst-1
[10]: https://www.gnu.org/software/make/manual/html_node/Multi_002dLine.html
[11]: https://www.gnu.org/software/make/manual/html_node/Make-Control-Functions.html#index-info
