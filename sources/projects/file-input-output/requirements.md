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
