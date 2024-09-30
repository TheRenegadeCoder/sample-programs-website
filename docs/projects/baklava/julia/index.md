---
authors:
- germmand
- Jeremy Grifski
date: 2018-10-04
featured-image: baklava-in-every-language.jpg
last-modified: 2019-03-27
layout: default
tags:
- baklava
- julia
title: Baklava in Julia
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/julia/how-to-implement-the-solution.md
- sources/programs/baklava/julia/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Julia](https://sampleprograms.io/languages/julia) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```julia
#!/usr/bin/julia

function main()
    for i = 0:10
        print(" "^(10 - i))
        println("*"^(i * 2 + 1))
    end 

    for i = 9:-1:0
        print(" "^(10 - i))
        println("*"^(i * 2 + 1))
    end
end

main()

```

{% endraw %}

Baklava in [Julia](https://sampleprograms.io/languages/julia) was written by:

- germmand
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).