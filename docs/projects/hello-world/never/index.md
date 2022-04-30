---

title: Hello World in Never
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Hello World in Never page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Never
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).