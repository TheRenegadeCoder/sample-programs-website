---
authors:
- rzuckerm
date: 2025-03-30
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2025-03-30
layout: default
tags:
- base64-encode-decode
- php
title: Base64 Encode Decode in Php
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/php/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/php/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Php](https://sampleprograms.io/languages/php) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```php
<?php
function usage()
{
    exit("Usage: please provide a mode and a string to encode/decode");
}

// Cannot use the library function directly because it doesn't check if the
// length of the input string is a multiple of 4. The value of false is
// returned if the input string is invalid. Otherwise, the Base64 decoded
// string is returned
function base64_validate_and_decode($str)
{
    // Use the library function if length of input string is a multiple of 4.
    // Otherwise, just return false
    $result = false;
    if (strlen($str) % 4 == 0) {
        $result = base64_decode($str, true);
    }

    return $result;
}

// Exit if arguments are invalid
if (count($argv) < 3 || strlen($argv[2]) < 1)
{
    usage();
}

$mode = $argv[1];
$str = $argv[2];
switch ($mode) {
    case "encode":
        $result = base64_encode($str);
        break;

    case "decode":
        $result = base64_validate_and_decode($str);
        if ($result === false) {
            usage();
        }
        break;

    default:
        usage();
}

echo $result;

```

{% endraw %}

Base64 Encode Decode in [Php](https://sampleprograms.io/languages/php) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).