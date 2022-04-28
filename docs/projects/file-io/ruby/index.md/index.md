# File Io in Ruby

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Ruby
def write_file
  out = File.new("output.txt", "w")

  out << "This is a line written by a Ruby program\n"
  out << "This line also"

  out.flush()
  out.close()
end


def read_file
  in_file = File.open("output.txt", "r")

  in_file.each_line do |line|
    puts line
  end

  in_file.close()
end

write_file()
read_file()
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.