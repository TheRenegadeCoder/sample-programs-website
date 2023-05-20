---
title: Remove All Whitespace in Euphoria
layout: default
date: 2023-02-19
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2023-02-19

---

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/regex.e as re
include std/sequence.e
include std/text.e

function remove_all_whitespace(sequence s)
    -- Trim off leading and trailing whitespace, then split into words
    sequence words = re:split(re:new(`\s+`), trim(s))

    -- Join words together without spaces
    return join(words, "")
end function

procedure usage()
    printf(STDOUT, "Usage: please provide a string")
    abort(0)
end procedure

-- Parse 1st command-line argument
sequence argv = command_line()
if length(argv) < 4 or length(argv[4]) = 0
then
    usage()
end if

-- Remove all whitespace and show result
sequence s = argv[4]
sequence t = remove_all_whitespace(s)
printf(STDOUT, "%s\n", {t})
```

{% endraw %}

[Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).