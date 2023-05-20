---
title: Reverse String in Never
layout: default
date: 2018-09-20
featured-image: reverse-string-in-every-language.jpg
last-modified: 2018-09-20

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Never](https://sampleprograms.io/languages/never) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

func reverse(hw[L] -> int) -> [_] -> int
{
    let rev = {[ L ]} -> int;
    
    func __reverse(hw[L1] -> int, rev[L2] -> int, i -> int) -> int
    {
        i < L1 ? { rev[L2 - i - 1] = hw[i]; __reverse(hw, rev, i + 1) } : 0 
    }
    __reverse(hw, rev, 0);

    rev
}

func main() -> int
{
    let hw = [ 72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33 ] -> int;
    
    print_str(reverse(hw))
}
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Never](https://sampleprograms.io/languages/never) was written by:

- smaludzi

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).