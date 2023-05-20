---
title: Bubble Sort in Ruby
layout: default
date: 2019-03-20
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2019-03-20

---

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
def bubble_sort(numbers)
  n = numbers.length
  for i in 0...n-1
    for j in 0...n-i-1
      if numbers[j] > numbers[j + 1]
        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
      end
    end
  end
  return numbers
end

def err()
  puts('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"')
end

begin
  unsorted = ARGV[0].split(", ").map{|i| Integer(i)}
  if unsorted.length > 1
    sorted = bubble_sort(unsorted)
    print(sorted)
  else
    err()
  end
rescue
  err()
end
```

{% endraw %}

[Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Jeremy Grifski
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 20 2019 19:51:53. The solution was first committed on Mar 20 2019 15:25:56. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).