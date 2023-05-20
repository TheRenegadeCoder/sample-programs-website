---
title: Longest Word in Euphoria
layout: default
date: 2023-02-17
featured-image: longest-word-in-every-language.jpg
last-modified: 2023-02-17

---

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/regex.e as re
include std/text.e
include std/math.e

function longest_word(sequence s)
    -- Trim off leading and trailing whitespace, then split into words
    sequence words = split(re:new(`\s+`), trim(s))

    -- Find longest word
    integer longest = 0
    for n = 1 to length(words)
    do
        longest = max({longest, length(words[n])})
    end for

    return longest
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

-- Get longest word length and display it
sequence s = argv[4]
printf(STDOUT, "%d\n", longest_word(s))
```

{% endraw %}

[Longest Word](https://sampleprograms.io/projects/longest-word) in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).