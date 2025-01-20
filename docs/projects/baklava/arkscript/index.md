---
authors:
- rzuckerm
date: 2025-01-20
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-20
layout: default
tags:
- arkscript
- baklava
title: Baklava in Arkscript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/arkscript/how-to-implement-the-solution.md
- sources/programs/baklava/arkscript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Arkscript](https://sampleprograms.io/languages/arkscript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```arkscript
(import std.List)
(import std.Math)
(import std.Range)
(import std.String)

(let repeat_string
    (fun (n s)
        (string:join (list:fill n s) "")
    )
)

(let baklava_line
    (fun (n) {
        (let num_spaces (math:abs n))
        (let num_stars (- 21 (* 2 num_spaces)))
        (string:join [(repeat_string num_spaces " ") (repeat_string num_stars "*")] "")
    })
)

(let ctr (range:range -10 11))
(range:forEach
    ctr 
    (fun (n) 
        (print (baklava_line n))
    )
)

```

{% endraw %}

Baklava in [Arkscript](https://sampleprograms.io/languages/arkscript) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).