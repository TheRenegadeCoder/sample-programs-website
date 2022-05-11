---

title: Reverse String in Dg
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Reverse String in Dg page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dg
import "/sys/argv"

snd_if_exists = xs -> if
    (len xs) > 1 => snd xs
    otherwise    => ""

reverse = s -> if
    len s     => last s + (init s |> reverse)
    otherwise => ""

print $ reverse <| snd_if_exists argv
```

{% endraw %}

Reverse String in Dg was written by:

- Riley Martine

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).