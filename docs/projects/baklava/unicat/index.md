---
authors:
- rzuckerm
date: 2023-08-28
featured-image: baklava-in-every-language.jpg
last-modified: 2023-08-28
layout: default
tags:
- baklava
- unicat
title: Baklava in Unicat
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/unicat/how-to-implement-the-solution.md
- sources/programs/baklava/unicat/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Unicat](https://sampleprograms.io/languages/unicat) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```unicat
# Set up characters
0o00 😻😹😸🙀🙀😼😸🙀🙀 Memory 0 = 0o40 (32 = ' ')
0o01 😻😹😹🙀🙀😽😺🙀🙀 Memory 1 = 0o52 (42 = '*')
0o02 😻😹😺🙀🙀😹😺🙀🙀 Memory 2 = 0o12 (10 = '\n')

# Set up constants
0o03 😻😹😻🙀🙀😹🙀🙀 Memory 3 = 1
0o04 😻😹😼🙀🙀😹🙀😿 Memory 4 = -1

# Set up varibles
0o05 😻😹😽🙀🙀😹😺🙀😿 Memory 5 = -0o12 (-10) (loop_counter)

# Loop start: num_spaces = absolute value of loop_counter
0o06 😻😹😾🙀🙀😸🙀🙀 Memory 6 = 0
0o07 😿🙀😸😾🙀🙀😽🙀🙀 Memory 6 += Memory 5 (num_spaces = loop_count)
0o10 😽😿😾🙀🙀😹😹🙀🙀 If Memory 6 > 0, jump to 0x12 (0o11 + 1) (if num_spaces > 0)
0o11 😿🙀🙀😾🙀🙀😼🙀🙀 Memory 6 *= Memory 4 (negate num_spaces)

# num_stars = 21 - 2*num_spaces
0o12 😻😹😿🙀🙀😺😽🙀🙀 Memory 7 = 0o25 (21)
0o13 😿🙀😺😿🙀🙀😾🙀🙀 Memory 7 -= Memory 6 (21 - num_spaces)
0o14 😿🙀😺😿🙀🙀😾🙀🙀 Memory 7 -= Memory 6 (num_stars = 21 - 2*num_spaces)

# Display spaces
0o15 😻😹😹🙀😿😹😿🙀🙀 Jump to 0o20 (0o17 + 1) (jump to check for num_spaces > 0)
0o16 😽😼😸🙀🙀 Output Memory 0 (' ')
0o17 😿🙀😺😾🙀🙀😻🙀🙀 Memory 6 -= Memory 3 (decrement num_spaces)
0o20 😽😿😾🙀🙀😹😽🙀🙀 If Memory 6 > 0, jump to 0o16 (0o15 + 1) (if num_spaces > 0)

# Display stars
0o21 😽😼😹🙀🙀 Output Memory 1 ('*')
0o22 😿🙀😺😿🙀🙀😻🙀🙀 Memory 7 -= Memory 3 (decrement num_stars)
0o23 😽😿😿🙀🙀😺😸🙀🙀 If Memory 7 > 0, jump to 0o21 (0o20 + 1)

# Output newline
0o24 😽😼😺🙀🙀 Output Memory 2 ('\n')

# If loop_counter > 10, jump to Loop start
0o25 😻😹😹😸🙀🙀😹😺🙀🙀 Memory 8 (0o10) = 10 (0o12)
0o26 😿🙀😺😹😸🙀🙀😽🙀🙀 Memory 8 (0o10) -= Memory 5 (10 - loop_counter)
0o27 😿🙀😸😽🙀🙀😻🙀🙀 Memory 5 += Memory 3 (increment loop_counter)
0o30 😽😿😹😸🙀🙀😽🙀🙀 If Memory 8 (0o10) > 0, jump to 0o06 (0o05 + 1) (if loop_counter > 10, jump to Loop start)

0o31 🙀🙀 Exit

```

{% endraw %}

Baklava in [Unicat](https://sampleprograms.io/languages/unicat) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).