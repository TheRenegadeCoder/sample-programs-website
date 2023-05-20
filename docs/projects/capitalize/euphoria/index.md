---
title: Capitalize in Euphoria
layout: default
date: 2023-02-17
featured-image: capitalize-in-every-language.jpg
last-modified: 2023-02-17

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/text.e

procedure usage()
    puts(STDOUT, "Usage: please provide a string\n")
    abort(0)
end procedure

function capitalize(sequence s)
    return upper(s[1]) & s[2..$]
end function

-- Parse 1st command-line argument
sequence argv = command_line()
if length(argv) < 4 or length(argv[4]) = 0
then
    usage()
end if

-- Capitalize string and show it
sequence s = argv[4]
s = capitalize(s)
printf(STDOUT, "%s\n", {s})
```

{% endraw %}

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).