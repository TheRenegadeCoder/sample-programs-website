---
title: Hello World in Vimscript
layout: default
date: 2018-08-27
featured-image: hello-world-in-every-language.jpg
last-modified: 2018-08-27

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Vimscript](https://sampleprograms.io/languages/vimscript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```vimscript
func! Hello()
    call append(0, "Hello, World!")
endfunc

au BufEnter,BufReadPost * call Hello()
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Vimscript](https://sampleprograms.io/languages/vimscript) was written by:

- Christoph Böhmwalder

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).