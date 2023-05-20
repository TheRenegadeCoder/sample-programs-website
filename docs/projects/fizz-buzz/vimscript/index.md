---
title: Fizz Buzz in Vimscript
layout: default
date: 2018-08-28
featured-image: fizz-buzz-in-every-language.png
last-modified: 2018-08-28

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Vimscript](https://sampleprograms.io/languages/vimscript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```vimscript
func! FizzBuzz()
    for l:i in range(1, 100)
        if l:i % 15 == 0
            let l:str = 'FizzBuzz'
        elseif l:i % 5 == 0
            let l:str = 'Buzz'
        elseif l:i % 3 == 0
            let l:str = 'Fizz'
        else
            let l:str = l:i
        endif

        call append(l:i-1, l:str)
    endfor

    " go to top of buffer
    normal gg
endfunc

au BufEnter,BufReadPost * call FizzBuzz()
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Vimscript](https://sampleprograms.io/languages/vimscript) was written by:

- Christoph Böhmwalder

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).