---

---

# Reverse String in Dg

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Dg
import "/sys/argv"

snd_if_exists = xs -> if
    (len xs) > 1 => snd xs
    otherwise    => ""

reverse = s -> if
    len s     => last s + (init s |> reverse)
    otherwise => ""

print $ reverse <| snd_if_exists argv

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.