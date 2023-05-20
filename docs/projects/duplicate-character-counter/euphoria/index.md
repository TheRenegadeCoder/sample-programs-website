---
title: Duplicate Character Counter in Euphoria
layout: default
date: 2023-02-19
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2023-02-19

---

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e

function duplicate_character_counter(sequence s)
    -- Initialize character counter
    sequence char_counter = repeat(0, 256)

    -- Count number of occurances of each character
    for n = 1 to length(s)
    do
        char_counter[s[n] + 1] += 1
    end for

    return char_counter
end function

procedure show_duplicate_character_counts(sequence s, sequence char_counter)
    boolean has_dupes = FALSE

    for n = 1 to length(s)
    do
        integer index = s[n] + 1
        if char_counter[index] > 1
        then
            printf(STDOUT, "%s: %d\n", {s[n], char_counter[index]})
            char_counter[index] = 0
            has_dupes = TRUE
        end if
    end for

    if not has_dupes
    then
        puts(STDOUT, "No duplicate characters\n")
    end if
end procedure

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

-- Count duplicate characters
sequence s = argv[4]
sequence char_counter = duplicate_character_counter(s)

-- Show all duplicate character counts in order in which they occurred in string (if any)
show_duplicate_character_counts(s, char_counter)
```

{% endraw %}

[Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).