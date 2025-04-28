---
authors:
- rzuckerm
date: 2025-04-27
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2025-04-27
layout: default
tags:
- awk
- base64-encode-decode
title: Base64 Encode Decode in Awk
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/awk/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/awk/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Awk](https://sampleprograms.io/languages/awk) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```awk
function usage() {
    print "Usage: please provide a mode and a string to encode/decode"
    exit(1)
}

# Awk doesn't have an ord() function, so create a global table from
# character to ASCII value
function init_ord_table(  i) {
    for (i = 0; i <= 255; i++) {
        ord_table[sprintf("%c", i)] = i
    }
}

function ord(s) {
    return (length(s) > 0) ? ord_table[s] : 0
}

function chr(i) {
    return sprintf("%c", i)
}

function init_base64_chars() {
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
}

function base64_encode(s,  i, result, len, n, u) {
    result = ""
    len = length(s)
    for (i = 1; i <= len; i += 3) {
        n[1] = ord(substr(s, i, 1))
        n[2] = ord(substr(s, i + 1, 1))
        n[3] = ord(substr(s, i + 2, 1))
        u = or(lshift(n[1], 16), lshift(n[2], 8), n[3])
        result = result base64_encode_char(u, i, len, 18)
        result = result base64_encode_char(u, i, len, 12)
        result = result base64_encode_char(u, i + 1, len, 6)
        result = result base64_encode_char(u, i + 2, len, 0)
    }

    return result
}

function base64_encode_char(u, idx, len, shifts) {
    return (idx <= len) ? substr(base64_chars, 1 + and(rshift(u, shifts), 0x3f), 1) : "="
}

# Return Base64 decoded string or 0 if invalid input
function base64_decode(s,  len, result, num_pads, c, i, k) {
    len = length(s)
    if ((len % 4) != 0) {
        return 0
    }

    num_pads = 0
    while (len > 0 && substr(s, len, 1) == "=") {
        num_pads++
        len--
    }

    if (num_pads > 2) {
        return 0
    }

    result = ""
    for (i = 1; i <= len; i += 4) {
        for (k = 1; k <= 4; k++) {
            c[k] = base64_decode_index(s, i + k - 1, len)
            if (c[k] < 0) {
                return 0
            }
        }

        u = or(lshift(c[1], 18), lshift(c[2], 12), lshift(c[3], 6), c[4])
        result = result base64_decode_char(u, i, len, 16)
        result = result base64_decode_char(u, i + 2, len, 8)
        result = result base64_decode_char(u, i + 3, len, 0)
    }

    return result
}

# Return Base64 index if valid character, -1 otherwise
function base64_decode_index(s, idx, len) {
    return (idx <= len) ? index(base64_chars, substr(s, idx, 1)) - 1 : 0
}

function base64_decode_char(u, idx, len, shifts) {
    return (idx <= len) ? chr(and(rshift(u, shifts), 0xff)) : ""
}

BEGIN {
    if (ARGC < 3 || !ARGV[2]) {
        usage()
    }

    init_ord_table()
    init_base64_chars()

    mode = ARGV[1]
    s = ARGV[2]
    switch (mode) {
        case "encode":
            result = base64_encode(s)
            break
        case "decode":
            result = base64_decode(s)
            if (result == 0) {
                usage()
            }
            break
        default:
            usage()
    }

    print result
}

```

{% endraw %}

Base64 Encode Decode in [Awk](https://sampleprograms.io/languages/awk) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).