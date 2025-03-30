---
authors:
- rzuckerm
date: 2025-03-30
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2025-03-30
layout: default
tags:
- base64-encode-decode
- euphoria
title: Base64 Encode Decode in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/euphoria/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/base64.e
include std/text.e
include std/regex.e as re

procedure usage()
    puts(
        STDOUT, 
        "Usage: please provide a mode and a string to encode/decode\n"
    )
    abort(0)
end procedure

constant re_not_base64_chars = re:new("[^A-Za-z0-9+/]")

-- Base64 decode
--
-- Although the built-in Base64 decode is available, it does not do a very good
-- job of error checking the input other that making sure that the input length
-- is a multiple of 4. The output of this function is -1 if the input string
-- is invalid, the Base64 decoded string otherwise.
function base64_decode(sequence str)
    -- Error if more than 2 pad trailing characters
    atom str_length = length(str)
    atom pad_length = str_length - length(trim_tail(str, "="))
    if pad_length > 2
    then
        return -1
    end if

    -- Remove trailing pad characters
    str_length -= pad_length

    -- Error if invalid Base64 characters
    if re:has_match(re_not_base64_chars, str[1..str_length])
    then
        return -1
    end if

    -- Use Base64 decode library function
    return base64:decode(str)
end function

-- Check command-line arguments
sequence argv = command_line()
if length(argv) < 5 or length(argv[5]) = 0
then
    usage()
end if

sequence mode = argv[4]
sequence str = argv[5]
object result
switch mode
do
    case "encode"
    then
        result = base64:encode(str)
    case "decode"
    then
        result = base64_decode(str)
        if atom(result)
        then
            usage()
        end if
    case else
        usage()
end switch

printf(STDOUT, "%s\n", {result})

```

{% endraw %}

Base64 Encode Decode in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).