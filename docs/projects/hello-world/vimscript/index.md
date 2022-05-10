---

title: Hello World in Vimscript
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the Hello World in Vimscript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```vimscript
func! Hello()
    call append(0, "Hello, World!")
endfunc

au BufEnter,BufReadPost * call Hello()
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).