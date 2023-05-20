---
title: Fibonacci in Ruby
layout: default
date: 2018-10-14
featured-image: fibonacci-in-every-language.jpg
last-modified: 2018-10-14

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
def fibonacci(number)
    a = 0
    b = 1
    c = 0

    i = 0
    while i < number
        c = a + b
        b = a
        a = c

        print("#{i+1}: #{c}\n")
        i += 1
    end
end

num = Integer(ARGV[0]) rescue -1
if num >= 0
    fibonacci(num)
else
    print("Usage: please input the count of fibonacci numbers to output")
end
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Noah Nichols
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 07 2019 00:40:32. The solution was first committed on Oct 14 2018 13:08:19. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).