First, like always, here's the complete solution:

```ruby
if ARGV.length < 1
    puts "Usage: ruby reverse-string.rb [string]"
else
    string = ARGV[0]
    puts string.reverse
end
```

Right away, we begin by checking to see if the user gave us a string in the
form of a command line argument:

```ruby
if ARGV.length < 1
    puts "Usage: ruby reverse-string.rb [string]"
```

If not, we print a usage message which tells the user how to use the program.

Otherwise, we store the command line argument that the user passed into a string:

```ruby
else
    string = ARGV[0]
    puts string.reverse
end
```

Then, we reverse the string using the built-in method of the string class and
print the result onto the screen.

As we can see, our solution is very brief. That's because we're using a
high-level language that offers many different tools, so we can concentrate on
building our application instead of worrying about implementation details.
