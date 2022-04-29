---

title: Capitalize in Ruby

---

Welcome to the Capitalize in Ruby page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Ruby
def capitalize_str(str)
    s = str.split(' ')
    s[0][0] = s[0][0].upcase
    s.join(' ')
end

if ARGV.length == 0 || ARGV[0] == ''
    puts 'Usage: please provide a string'
else
    puts capitalize_str(ARGV[0])
end

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.