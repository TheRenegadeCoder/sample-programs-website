As usual, we present the whole solution before we delve deeper into the code:

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
abilities so we specify "w" for writing.

For the next two lines we write arbitrary text to the file:

```ruby
out << "This is a line written by a Ruby program\n"
out << "This line also"
```

In this sample code we used the bitshift left operators to write the text. We
could have used the write() method to write text instead of using the operators.

Next, we flush the file:

```ruby
out.flush()
```

Sometimes when we make calls to write not everything may get written down to
disk. Only a fraction could be in the file and the rest is in memory waiting
to get written to the file. To ensure everything is written, we call the method
flush().

Lastly, we close the file to free up its resources:

```ruby
out.close()
```

This is something you should always do with resources when you're done with them.

### Reading

Like with the `write_file()` function, we put the code for reading the file in
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
it opens the file for reading purposes, but for the sake of being explicit I
passed "r" for the mode.

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
