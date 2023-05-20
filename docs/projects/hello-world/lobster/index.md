---
title: Hello World in Lobster
layout: default
date: 2019-09-14
featured-image: hello-world-in-every-language.jpg
last-modified: 2019-09-14

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Lobster](https://sampleprograms.io/languages/lobster) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lobster
import std
import vec
import color

fatal(gl_window("Hello World", 640, 480))

while gl_frame() and gl_button("escape") != 1:
    gl_clear(color_black)
    check(gl_set_font_name("data/fonts/US101/US101.TTF") and gl_set_font_size(32), "can\'t load font!")
    gl_text("Hello World!")
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Lobster](https://sampleprograms.io/languages/lobster) was written by:

- Abel D

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Sep 16 2019 13:20:15. The solution was first committed on Sep 14 2019 12:53:02. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).