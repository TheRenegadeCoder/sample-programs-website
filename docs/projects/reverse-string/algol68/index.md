---
title: Reverse String in Algol68
layout: default
date: 2023-01-24
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-01-24

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Algol68](https://sampleprograms.io/languages/algol68) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```algol68
PROC reverse string = (STRING s) STRING:
(
    STRING t;
    FOR n FROM UPB s DOWNTO 1
    DO
        t +:= s[n]
    OD;

    t
);

# Get 1st command-line argument #
STRING s := argv(4);

# Reverse string and show result #
s := reverse string(s);
printf(($gl$, s))
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Algol68](https://sampleprograms.io/languages/algol68) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 19 2023 22:24:49. The solution was first committed on Jan 24 2023 20:34:53. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).