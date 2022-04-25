# File Io in Every Language

## Description

Most languages have built-in utilities or functions for reading and writing files.
Many of these input/output functions follow a similar pattern across programming languages:
a string to the path of the file and a "mode". A mode is how the files is opened.
Will the file be opened for reading, writing, or even both?
Will the file be appending new content? Truncated?


## Requirements

In general, a File IO solution should perform the following:

1. Write some arbitrary content to a file (use `output.txt`)
2. Read back that content and print it to the user

More specifically, begin with writing a file to disk. In the write function, you should show how
to open a file with write abilities and write some contents to the file. Before closing the file,
you should ensure everything is written to disk. Then, close the file. There should be basic error
checking to confirm file opening was successful.

With the read file function, open the file with read abilities. Most higher level languages
offer a way to read line by line or even transfer the whole contents into a string. One way
to read the file is to loop line by line and do some processing. Printing each line to the
screen is enough. Like in the write function, make sure there is some basic error checking.


## Testing

Verify that the actual output matches the expected output. See the
[requirements][1] section for an example of the expected output.


## Articles

- [File Io in Bash](https://sampleprograms.io/projects/file-io/bash)
- [File Io in C](https://sampleprograms.io/projects/file-io/c)
- [File Io in C#](https://sampleprograms.io/projects/file-io/c-sharp)
- [File Io in C++](https://sampleprograms.io/projects/file-io/c-plus-plus)
- [File Io in Dg](https://sampleprograms.io/projects/file-io/dg)
- [File Io in Go](https://sampleprograms.io/projects/file-io/go)
- [File Io in Haskell](https://sampleprograms.io/projects/file-io/haskell)
- [File Io in Java](https://sampleprograms.io/projects/file-io/java)
- [File Io in Javascript](https://sampleprograms.io/projects/file-io/javascript)
- [File Io in Kotlin](https://sampleprograms.io/projects/file-io/kotlin)
- [File Io in Lua](https://sampleprograms.io/projects/file-io/lua)
- [File Io in Matlab](https://sampleprograms.io/projects/file-io/matlab)
- [File Io in Objective C](https://sampleprograms.io/projects/file-io/objective-c)
- [File Io in Perl](https://sampleprograms.io/projects/file-io/perl)
- [File Io in Php](https://sampleprograms.io/projects/file-io/php)
- [File Io in Python](https://sampleprograms.io/projects/file-io/python)
- [File Io in R](https://sampleprograms.io/projects/file-io/r)
- [File Io in Ruby](https://sampleprograms.io/projects/file-io/ruby)
- [File Io in Rust](https://sampleprograms.io/projects/file-io/rust)
- [File Io in Scala](https://sampleprograms.io/projects/file-io/scala)

## Further Reading