---

---

# Hello World in Never

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.