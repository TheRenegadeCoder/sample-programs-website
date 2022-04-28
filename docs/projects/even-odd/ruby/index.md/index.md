# Even Odd in Ruby

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Ruby
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.