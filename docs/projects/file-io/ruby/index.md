---

title: File Io in Ruby
layout: default
date: 2022-04-28
last-modified: 2022-05-16

---

Welcome to the [File Io](https://sampleprograms.io/projects/file-io) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
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

{% endraw %}

[File Io](https://sampleprograms.io/projects/file-io) in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Noah

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).