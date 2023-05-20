---
title: Fizz Buzz in Euphoria
layout: default
date: 2023-02-19
featured-image: fizz-buzz-in-every-language.png
last-modified: 2023-02-19

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/math.e
include std/utils.e

for n = 1 to 100
do
    sequence s = ""
    s &= iif(mod(n, 3) = 0, "Fizz", "")
    s &= iif(mod(n, 5) = 0, "Buzz", "")
    s &= iif(length(s) = 0, sprintf("%d", n), "")
    printf(STDOUT, "%s\n", {s})
end for
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).