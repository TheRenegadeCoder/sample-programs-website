---
authors:
- rzuckerm
date: 2023-02-26
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2023-02-26
layout: default
tags:
- euphoria
- longest-palindromic-substring
title: Longest Palindromic Substring in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/euphoria/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/types.e
include std/text.e

-- Find longest palindromic string using matching array
-- Source: https://www.geeksforgeeks.org/longest-palindromic-substring-using-dynamic-programming/
function longest_palindromic_substring(sequence s)
    -- Initialize array indicating whether there is a character match
    -- between two characters to indicate that nothing matches
    integer n = length(s)
    sequence matches = repeat(repeat(FALSE, n), n)

    -- Indicate all length 1 strings match
    for i = 1 to n
    do
        matches[i][i] = TRUE
    end for

    -- Convert string to lowercase
    sequence t = lower(s)

    -- Find all length 2 matches
    integer start = 1
    integer max_len = 1
    for i = 1 to n - 1
    do
        if t[i] = t[i + 1]
        then
            matches[i][i+1] = TRUE
            if max_len < 2
            then
                start = i
                max_len = 2
            end if
        end if
    end for

    -- Find all length 3 or higher matches
    integer j
    for len = 3 to n
    do
        -- Loop through each starting character
        for i = 1 to n - len + 1
        do
            -- If match for one character in from start and end characters
            -- and start and end characters match, set match for start and
            -- end characters, and update max length
            j = i + len - 1
            if matches[i + 1][j - 1] and t[i] = t[j]
            then
                matches[i][j] = TRUE
                if len > max_len
                then
                    start = i
                    max_len = len
                end if
            end if
        end for
    end for

    return s[start..start + max_len - 1]
end function

procedure usage()
    puts(STDOUT, "Usage: please provide a string that contains at least one palindrome\n")
    abort(0)
end procedure

-- Error if 1st command-line argument is missing is empty
sequence argv = command_line()
if length(argv) < 4 or length(argv[4]) = 0
then
    usage()
end if

-- Get longest palindromic substring. Error if none found
sequence s = argv[4]
sequence longest = longest_palindromic_substring(s)
if length(longest) < 2
then
    usage()
end if

-- Show longest palindromic substring
printf(STDOUT, "%s\n", {longest})

```

{% endraw %}

Longest Palindromic Substring in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).