---
authors:
- Ștefan-Iulian Alecu
date: 2025-07-29
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2026-05-13
layout: default
tags:
- base64-encode-decode
- c-sharp
title: Base64 Encode Decode in C#
title1: Base64 Encode
title2: Decode in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/c-sharp/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
﻿using System.Text;

return args switch
{
    ["encode", var value] when !string.IsNullOrWhiteSpace(value)
        => Encode(value),

    ["decode", var value] when !string.IsNullOrWhiteSpace(value)
        => Decode(value),

    _ => Usage()
};

static int Encode(string value)
{
    Console.WriteLine(Convert.ToBase64String(Encoding.ASCII.GetBytes(value)));
    return 0;
}

static int Decode(string value)
{
    byte[] buffer = new byte[value.Length];
    if (!Convert.TryFromBase64String(value, buffer, out int written))
        return Usage();

    Console.WriteLine(Encoding.ASCII.GetString(buffer, 0, written));
    return 0;
}

static int Usage()
{
    Console.Error.WriteLine("Usage: please provide a mode and a string to encode/decode");
    return 1;
}
```

{% endraw %}

Base64 Encode Decode in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).