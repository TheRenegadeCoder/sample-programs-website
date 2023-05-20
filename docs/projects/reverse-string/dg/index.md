---
title: Reverse String in Dg
layout: default
date: 2018-10-03
featured-image: reverse-string-in-every-language.jpg
last-modified: 2018-10-03

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Dg](https://sampleprograms.io/languages/dg) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dg
import "/sys/argv"

snd_if_exists = xs -> if
    (len xs) > 1 => snd xs
    otherwise    => ""

reverse = s -> if
    len s     => last s + (init s |> reverse)
    otherwise => ""

print $ reverse <| snd_if_exists argv
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Dg](https://sampleprograms.io/languages/dg) was written by:

- Riley Martine

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).