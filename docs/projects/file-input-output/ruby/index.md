---
authors:
- Jeremy Grifski
- Noah
- rzuckerm
date: 2018-09-13
featured-image: file-input-output-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- file-input-output
- ruby
title: File Input Output in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/ruby/how-to-implement-the-solution.md
- sources/programs/file-input-output/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

File Input Output in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Noah

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Before reading on, why not try to figure out how it works?

### Writing

For modularity and readability, we have extracted the file writing code into
its own function:

```ruby
def write_file
  out = File.new("output.txt", "w")

  out << "This is a line written by a Ruby program\n"
  out << "This line also"

  out.flush()
  out.close()
end
```

On the first line we call the function File.new():

```ruby
out = File.new("output.txt", "w")
```

It takes an argument to the path of the file and a mode. A mode is how we want
the file to be opened. By default, it opens for reading. We want to write
abilities so we specify `"w"` for writing.

For the next two lines we write arbitrary text to the file:

```ruby
out << "This is a line written by a Ruby program\n"
out << "This line also"
```

In this sample code we used the bitshift left operators to write the text. We
could have used the `write()` method to write text instead of using the operators.

Next, we flush the file:

```ruby
out.flush()
```

Sometimes when we make calls to write not everything may get written down to
disk. Only a fraction could be in the file and the rest is in memory waiting
to get written to the file. To ensure everything is written, we call the method
`flush()`.

Lastly, we close the file to free up its resources:

```ruby
out.close()
```

This is something you should always do with resources when you're done with them.

### Reading

Like with the `write_file()` function, we put the code for reading the file in
its own function:

```ruby
def read_file
  in_file = File.open("output.txt", "r")

  in_file.each_line do |line|
    puts line
  end

  in_file.close()
end
```

To begin, we open a file on the first line:

```ruby
in_file = File.open("output.txt", "r")
```

`File.open()` takes an argument to the path of the file and a mode. By default,
it opens the file for reading purposes, but for the sake of being explicit, I
passed `"r"` for the mode.

The next three lines loop through the file and print out each line:

```ruby
in_file.each_line do |line|
  puts line
end
```

Finally, we close the file:

```ruby
in_file.close()
```

And, that's it for reading.

### Scripting

Since Ruby is a scripting language, we can call the two functions we've just
defined back-to-back at the end of our file:

```ruby
write_file()
read_file()
```

And, that'll do it!


## How to Run the Solution

Websites like Repl allow you to write and run code of different programming
languages in the browser. Feel free to drop our solution into one of your
favorite online editors.

If you have Ruby installed on your computer/mac, you can run the following command:

```console
ruby file-io.rb
```

To verify everything has worked correctly, you should see the contents of the
file printed to the screen. In addition, the dummy file should be located
alongside your script now. Feel free to check that out and let us know.
