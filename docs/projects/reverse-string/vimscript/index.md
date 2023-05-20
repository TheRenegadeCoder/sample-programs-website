---
title: Reverse String in Vimscript
layout: default
date: 2018-08-27
featured-image: reverse-string-in-every-language.jpg
last-modified: 2018-08-27

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Vimscript](https://sampleprograms.io/languages/vimscript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```vimscript
func! Reverse(str)
    let l:r = join(reverse(split(a:str, '\zs')), '')
    call append(0, l:r)
endfunc
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Vimscript](https://sampleprograms.io/languages/vimscript) was written by:

- Christoph Böhmwalder

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).