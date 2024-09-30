---
authors:
- rzuckerm
date: 2023-08-28
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-08-28
layout: default
tags:
- reverse-string
- unicat
title: Reverse String in Unicat
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/unicat/how-to-implement-the-solution.md
- sources/programs/reverse-string/unicat/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Unicat](https://sampleprograms.io/languages/unicat) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```unicat
# Find end of input by finding null-termination
0o00 😺😼😹😺🙀🙀 Memory 10 (0o12) through N+11 = input (N characters), newline, null
0o01 😻😹😸🙀🙀😹😺🙀🙀 Memory 0 = 0o12 (10 = '\n')
0o02 😻😹😹🙀🙀😹😺🙀🙀 Memory 1 = 0o12 (10, input pointer)
0o03 😻😹😺🙀🙀😹🙀🙀 Memory 2 = 1
0o04 😻😹😻🙀🙀😸🙀🙀 Memory 3 = 0
0o05 😿🙀😸😻🙀🙀😹🙀🙀 Memory 3 += Memory 1 (input pointer)
0o06 😼😾😻🙀🙀 Memory 3 = pointer(Memory 3) (contents of input pointer)
0o07 😽😿😻🙀🙀😹😸🙀🙀 If Memory 3 > 0, jump to 0o11 (0o10 + 1)
0o10 😻😹😹🙀😿😹😺🙀🙀 Jump to 0o13 (0o12 + 1)
0o11 😿🙀😸😹🙀🙀😺🙀🙀 Memory 1 += Memory 2 (1) (increment input pointer)
0o12 😻😹😹🙀😿😻🙀🙀 Jump to 0o04 (0o03 + 1)

# Null-terminate before input
0o13 😻😹😹😹🙀🙀😸😸🙀🙀 Memory 9 (0o11) = 0

# Strip trailing newline (if present)
0o14 😻😹😻🙀🙀😹🙀😿 Memory 3 = -1
0o15 😿🙀😸😻🙀🙀😹🙀🙀 Memory 3 += Memory 1 (input pointer - 1, previous character)
0o16 😼😾😻🙀🙀 Memory 3 = pointer(Memory 3) (previous character)
0o17 😿🙀😺😻🙀🙀😸🙀🙀 Memory 3 -= Memory 0 (contents of input pointer - '\n')
0o20 😽😿😻🙀🙀😺😼🙀🙀 If Memory 3 > 0, jump to 0o25 (0o24 + 1) (if contents of input pointer > '\n')
0o21 😻😹😼🙀🙀😹🙀😿 Memory 4 = -1
0o22 😿🙀🙀😻🙀🙀😼🙀🙀 Memory 3 *= Memory 4
0o23 😽😿😻🙀🙀😺😼🙀🙀 If Memory 3 > 0, jump to 0o25 (0o24 + 1) (if '\n' > contents of input pointer)
0o24 😿🙀😺😹🙀🙀😺🙀🙀 Memory 1 -= Memory 2 (1) (decrement input pointer)

# Output reversed string starting before newline (if present) until beginning
# null-termination is found, then output a newline
0o25 😿🙀😺😹🙀🙀😺🙀🙀 Memory 1 -= Memory 2 (1) (decrement input pointer)
0o26 😻😹😻🙀🙀😸🙀🙀 Memory 3 = 0
0o27 😿🙀😸😻🙀🙀😹🙀🙀 Memory 3 += Memory 1 (input pointer)
0o30 😼😾😻🙀🙀 Memory 3 = pointer(Memory 3) (contents of input pointer)
0o31 😽😿😻🙀🙀😻😻🙀🙀 If Memory 3 > 0, jump to 0o34 (0o33 + 1)
0o32 😽😼😸🙀🙀 Output Memory 0 ('\n')
0o33 🙀🙀 Exit
0o34 😽😼😻🙀🙀 Output Memory 3 (contents of input pointer)
0o35 😻😹😹🙀😿😺😼🙀🙀 Jump to 0o25 (0o24 + 1)

```

{% endraw %}

Reverse String in [Unicat](https://sampleprograms.io/languages/unicat) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).