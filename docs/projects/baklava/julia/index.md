---
title: Baklava in Julia
layout: default
date: 2018-10-04
featured-image: baklava-in-every-language.jpg
last-modified: 2018-10-04

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Julia](https://sampleprograms.io/languages/julia) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```julia
#!/usr/bin/julia

function main()
    for i = 0:10
        print(" "^(10 - i))
        println("*"^(i * 2 + 1))
    end 

    for i = 9:-1:0
        print(" "^(10 - i))
        println("*"^(i * 2 + 1))
    end
end

main()
```

{% endraw %}

[Baklava](https://sampleprograms.io/projects/baklava) in [Julia](https://sampleprograms.io/languages/julia) was written by:

- germmand
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 27 2019 14:00:36. The solution was first committed on Oct 04 2018 17:07:58. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).