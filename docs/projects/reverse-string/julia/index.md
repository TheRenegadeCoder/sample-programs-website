---

title: Reverse String in Julia
layout: default
date: 2022-04-28
last-modified: 2022-12-25

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Julia](https://sampleprograms.io/languages/julia) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```julia
#!/usr/bin/julia
# Reverse the Input String
# Function to print Error Message
function err()
  println("Usage: please provide a string")
end
# Function to reverse the input string
function reverse_string(n)
  if (length(n) in [0,1])
    err()
  else
    println(reverse(n))
  end
end

try
  reverse_string(ARGS[1])
catch e
  err()
end
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Julia](https://sampleprograms.io/languages/julia) was written by:

- smjalageri

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).