---
title: Hello World in Never
layout: default
date: 2018-09-20
featured-image: hello-world-in-every-language.jpg
last-modified: 2018-09-20

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Never](https://sampleprograms.io/languages/never) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```never

func print_str(hw[L] -> int) -> int
{
    func __print(hw[L] -> int, i -> int) -> int
    {
        i < L ? { print(hw[i]); __print(hw, i + 1) } : 0
    }
    __print(hw, 0)
}

func main() -> int
{
    let hw = [ 72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33 ] -> int;
    
    print_str(hw)
}
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Never](https://sampleprograms.io/languages/never) was written by:

- smaludzi

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).