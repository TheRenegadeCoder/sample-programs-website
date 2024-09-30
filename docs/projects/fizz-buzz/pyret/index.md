---
authors:
- Jeremy Grifski
date: 2023-10-15
featured-image: fizz-buzz-in-every-language.png
last-modified: 2023-10-15
layout: default
tags:
- fizz-buzz
- pyret
title: Fizz Buzz in Pyret
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/pyret/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/pyret/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Pyret](https://sampleprograms.io/languages/pyret) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```pyret
fun fizzbuzz(n :: Number):
  when n > 0 block:
    fizzbuzz(n - 1)
    var result = ""
    when num-modulo(n, 3) == 0:
      result := string-append(result, "Fizz")
    end
    when num-modulo(n, 5) == 0:
      result := string-append(result, "Buzz")
    end
    when string-equal(result, ""):
      result := tostring(n)
    end
    print(string-append(result, "\n"))
  end
end

fizzbuzz(100)

```

{% endraw %}

Fizz Buzz in [Pyret](https://sampleprograms.io/languages/pyret) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).