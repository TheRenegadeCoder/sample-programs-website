---
title: Reverse String in Euphoria
layout: default
date: 2023-02-19
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-02-19

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/sequence.e

-- Parse 1st command-line argument
sequence argv = command_line()
sequence s = ""
if length(argv) >= 4
then
  s = argv[4]
end if

-- Show reversed string
sequence t = reverse(s)
printf(STDOUT, "%s\n", {t})
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).