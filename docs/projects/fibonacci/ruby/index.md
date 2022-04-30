---

title: Fibonacci in Ruby
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Fibonacci in Ruby page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Ruby
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).