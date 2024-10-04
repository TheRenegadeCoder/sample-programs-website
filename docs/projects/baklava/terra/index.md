---
authors:
- rzuckerm
date: 2024-10-03
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-03
layout: default
tags:
- baklava
- terra
title: Baklava in Terra
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/terra/how-to-implement-the-solution.md
- sources/programs/baklava/terra/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Terra](https://sampleprograms.io/languages/terra) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```terra
local function strRepeat(n, s)
    local r = ""
    for i = 1, n do
        r = r .. s
    end

    return r
end

local function baklava()
    for i = -10, 10 do
        local numSpaces = i
        if i < 0 then
            numSpaces = -numSpaces
        end

        print(strRepeat(numSpaces, " ") .. strRepeat(21 - 2 * numSpaces, "*"))
    end
end

baklava()

```

{% endraw %}

Baklava in [Terra](https://sampleprograms.io/languages/terra) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).