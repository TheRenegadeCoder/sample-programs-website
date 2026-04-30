---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2026-05-01
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2026-05-01
layout: default
tags:
- base64-encode-decode
- cobol
title: Base64 Encode Decode in COBOL
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/cobol/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/cobol/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [COBOL](https://sampleprograms.io/languages/cobol) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cobol
identification division.
program-id. base64-util.

data division.
working-storage section.

01  cmd-args.
    05  arg-count        pic 9(4) comp.
    05  execution-mode   pic x(10).
    05  input-text       pic x(4096).

01  text-work-area.
    05  output-text      pic x(8192).
    05  input-len        pic 9(5) comp.
    05  str-idx          pic 9(5) comp.
    05  out-pos          pic 9(5) comp value 0.
    05  char-val         pic 9(4) comp.
    05  out-char         pic x.

01  raw-bytes.
    05  byte-1           pic 9(4) comp.
    05  byte-2           pic 9(4) comp.
    05  byte-3           pic 9(4) comp.

01  b64-indices.
    05  idx-1            pic 9(4) comp.
    05  idx-2            pic 9(4) comp.
    05  idx-3            pic 9(4) comp.
    05  idx-4            pic 9(4) comp.
    05  table-idx        pic 9(4) comp.

01  base64-table         pic x(64) value
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".

01  decode-map.
    05  decode-val       occurs 256 times pic s9(4) comp.

procedure division.

main.
    accept arg-count from argument-number

    if arg-count < 2
        perform show-usage
    end-if

    accept execution-mode from argument-value
    accept input-text from argument-value

    move function length(function trim(input-text)) to input-len

    if input-len = 0
        perform show-usage
    end-if

    perform build-decode-table

    evaluate function lower-case(execution-mode)
        when "encode"
            perform do-encode
        when "decode"
            perform do-decode
        when other
            perform show-usage
    end-evaluate

    if out-pos > 0
        display output-text(1:out-pos)
    end-if
    
    move 0 to return-code
    goback.

build-decode-table.
    perform varying table-idx from 1 by 1 until table-idx > 256
        move -1 to decode-val(table-idx)
    end-perform

    perform varying table-idx from 1 by 1 until table-idx > 64
        move function ord(base64-table(table-idx:1)) to char-val
        compute decode-val(char-val) = table-idx - 1
    end-perform.

do-encode.
    move 1 to str-idx
    move 0 to out-pos
    
    perform until str-idx > input-len
        move 0 to byte-1 byte-2 byte-3
        
        compute byte-1 = function ord(input-text(str-idx:1)) - 1
        
        if str-idx + 1 <= input-len
            compute byte-2 = function ord(input-text(str-idx + 1:1)) - 1
        end-if
        
        if str-idx + 2 <= input-len
            compute byte-3 = function ord(input-text(str-idx + 2:1)) - 1
        end-if

        compute idx-1 = byte-1 / 4
        compute idx-2 = function mod(byte-1, 4) * 16 + byte-2 / 16
        compute idx-3 = function mod(byte-2, 16) * 4 + byte-3 / 64
        compute idx-4 = function mod(byte-3, 64)

        move base64-table(idx-1 + 1:1) to out-char
        perform append-char
        move base64-table(idx-2 + 1:1) to out-char
        perform append-char

        if str-idx + 1 <= input-len
            move base64-table(idx-3 + 1:1) to out-char
        else
            move "=" to out-char
        end-if
        perform append-char

        if str-idx + 2 <= input-len
            move base64-table(idx-4 + 1:1) to out-char
        else
            move "=" to out-char
        end-if
        perform append-char

        add 3 to str-idx
    end-perform.

do-decode.
    if function mod(input-len, 4) not = 0
        perform show-usage
    end-if

    move 1 to str-idx
    move 0 to out-pos

    perform until str-idx > input-len
        perform validate-block

        move function ord(input-text(str-idx:1)) to char-val
        move decode-val(char-val) to idx-1
        
        move function ord(input-text(str-idx + 1:1)) to char-val
        move decode-val(char-val) to idx-2

        compute byte-1 = idx-1 * 4 + idx-2 / 16
        move function char(byte-1 + 1) to out-char
        perform append-char

        if input-text(str-idx + 2:1) not = "="
            move function ord(input-text(str-idx + 2:1)) to char-val
            move decode-val(char-val) to idx-3
            compute byte-2 = function mod(idx-2, 16) * 16 + idx-3 / 4
            move function char(byte-2 + 1) to out-char
            perform append-char
        end-if

        if input-text(str-idx + 3:1) not = "="
            move function ord(input-text(str-idx + 3:1)) to char-val
            move decode-val(char-val) to idx-4
            compute byte-3 = function mod(idx-3, 4) * 64 + idx-4
            move function char(byte-3 + 1) to out-char
            perform append-char
        end-if

        add 4 to str-idx
    end-perform.

validate-block.
    if input-text(str-idx:1) = "=" or input-text(str-idx + 1:1) = "="
        perform show-usage
    end-if

    perform varying char-val from 0 by 1 until char-val > 3
        move function ord(input-text(str-idx + char-val:1)) to byte-1
        if decode-val(byte-1) = -1 and input-text(str-idx + char-val:1) not = "="
            perform show-usage
        end-if
    end-perform

    if input-text(str-idx + 2:1) = "="
        if input-text(str-idx + 3:1) not = "=" or str-idx + 4 <= input-len
            perform show-usage
        end-if
    end-if

    if input-text(str-idx + 3:1) = "="
        if str-idx + 4 <= input-len
            perform show-usage
        end-if
    end-if.

append-char.
    add 1 to out-pos
    move out-char to output-text(out-pos:1).

show-usage.
    display "Usage: please provide a mode and a string to encode/decode"
    move 1 to return-code
    stop run.
```

{% endraw %}

Base64 Encode Decode in [COBOL](https://sampleprograms.io/languages/cobol) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).