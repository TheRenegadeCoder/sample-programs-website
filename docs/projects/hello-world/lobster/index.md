---

title: Hello World in Lobster
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Hello World in Lobster page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).