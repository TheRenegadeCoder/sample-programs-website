---
authors:
- f00d
date: 2025-10-30
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-10-30
layout: default
tags:
- fizz-buzz
- goby
title: Fizz Buzz in Goby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/goby/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/goby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Goby](https://sampleprograms.io/languages/goby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```goby
i = 1
while i do
    if i > 100
    break
    end
    result = ""
    if i % 3 == 0 
        result += "Fizz"
    end
    if i % 5 == 0
        result += "Buzz"
    end
    if result == ""
        result = i.to_s + ""
    end
    puts(result)
    i += 1
end

```

{% endraw %}

Fizz Buzz in [Goby](https://sampleprograms.io/languages/goby) was written by:

- f00d

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).