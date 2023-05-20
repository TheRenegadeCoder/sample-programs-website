---
title: Remove All Whitespace in Julia
layout: default
date: 2022-10-05
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2022-10-05

---

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Julia](https://sampleprograms.io/languages/julia) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```julia
using Core: print
function err()
  println("Usage: please provide a string")
end

function remove_all_whitespaces(n)
  if (length(n) in [0,1])
    err()
  else
    n_nospace = (filter(x -> !isspace(x), n))
    n_notab = replace(n_nospace,  "\t" => "")
    n_nonewline = replace(n_notab,  "\n" => "")
    n_nonewline = replace(n_notab,  "\r" => "")
    println(n_nonewline)
  end
end

try
  # remove_all_whitespaces(parse(ARGS[1]))
  remove_all_whitespaces(ARGS[1])
catch e
  err()
end
```

{% endraw %}

[Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Julia](https://sampleprograms.io/languages/julia) was written by:

- smjalageri

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).