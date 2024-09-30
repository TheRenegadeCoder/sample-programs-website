---
authors:
- Alex Gustafsson
- Jeremy Grifski
date: 2019-10-18
featured-image: rot13-in-every-language.jpg
last-modified: 2020-10-15
layout: default
tags:
- lua
- rot13
title: Rot13 in Lua
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/lua/how-to-implement-the-solution.md
- sources/programs/rot13/lua/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua
local function ascii_base(s)
  return s:lower() == s and ('a'):byte() or ('A'):byte()
end

function caesar_cipher(str, key)
  return (str:gsub('%a', function(s)
    local base = ascii_base(s)
    return string.char(((s:byte() - base + key) % 26) + base)
  end))
end

if (#arg < 1 or arg[1] == "")
then
    print('Usage: please provide a string to encrypt')
else
    io.write(caesar_cipher(arg[1], 13))
end

io.write("\n")

```

{% endraw %}

Rot13 in [Lua](https://sampleprograms.io/languages/lua) was written by:

- Alex Gustafsson
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).