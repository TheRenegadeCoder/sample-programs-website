---

title: Baklava in Julia
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Baklava in Julia page! Here, you'll find the source code for this program as well as a description of how the program works.

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

Baklava in Julia was written by:

- Jeremy Grifski
- germmand

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 27 2019 14:00:36. The solution was first committed on Oct 04 2018 17:07:58. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).