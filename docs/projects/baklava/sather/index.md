---
authors:
- rzuckerm
date: 2024-10-02
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-02
layout: default
tags:
- baklava
- sather
title: Baklava in Sather
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/sather/how-to-implement-the-solution.md
- sources/programs/baklava/sather/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Sather](https://sampleprograms.io/languages/sather) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```sather
class BAKLAVA is
  main is
    i:INT := -10;
    loop while!(i <= 10);
      numSpaces:INT := i;
      if (numSpaces < 0) then
        numSpaces := -numSpaces;
      end;

      #OUT + strRepeat(numSpaces, " ") + strRepeat(21 - 2 * numSpaces, "*") +"\n";
      i := i + 1;
    end;
  end;

  strRepeat(n:INT, s:STR):STR is
    r:STR := "";
    loop n.times!;
        r := r + s;
    end;

    return r;
  end;
end;

```

{% endraw %}

Baklava in [Sather](https://sampleprograms.io/languages/sather) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).