---

title: Fizz Buzz in Euphoria
layout: default
date: 2022-04-28
last-modified: 2023-02-20

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/math.e

for n = 1 to 100
do
    sequence s = ""
    if mod(n, 3) = 0
    then
        s &= "Fizz"
    end if

    if mod(n, 5) = 0
    then
        s &= "Buzz"
    end if

    if length(s) = 0
    then
        s &= sprintf("%d", n)
    end if

    printf(STDOUT, "%s\n", {s})
end for
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).