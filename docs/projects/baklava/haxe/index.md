---
authors:
- rzuckerm
date: 2025-01-01
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-01
layout: default
tags:
- baklava
- haxe
title: Baklava in Haxe
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/haxe/how-to-implement-the-solution.md
- sources/programs/baklava/haxe/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Haxe](https://sampleprograms.io/languages/haxe) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```haxe
import StringTools;

class Baklava {
    static private function repeatString(s:String, n:Int): String {
        return StringTools.rpad("", s, n);
    }

    static public function main() {
        for (n in -10...11) {
            var numSpaces = Std.int(Math.abs(n));
            var numStars = 21 - 2 * numSpaces;
            trace(repeatString(" ", numSpaces) + repeatString("*", numStars));
        }
    }
}

```

{% endraw %}

Baklava in [Haxe](https://sampleprograms.io/languages/haxe) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).