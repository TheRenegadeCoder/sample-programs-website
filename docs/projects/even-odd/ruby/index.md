---

title: Even Odd in Ruby
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Even Odd in Ruby page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```ruby
# Requirement https://sample-programs.therenegadecoder.com/projects/even-odd/
# Issue 1839

if ARGV.empty?
# if ARGV.length < 1
    puts "Usage: please input a number"
    exit
else
    # if ARGV.empty?
    #     puts "Usage: please input a number"
    # end
    begin
    string1 = ARGV[0]
    num = Integer(string1)
    rescue ArgumentError
    puts "Usage: please input a number"
    exit
    end

    if num % 2 == 0
    	puts "Even"
    else
    	puts "Odd"
    end
end
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).