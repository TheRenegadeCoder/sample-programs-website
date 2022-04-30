---

title: Reverse a String in Ruby
layout: default
last-modified: 2020-05-02
featured-image:
tags: [ruby, reverse-a-string]
authors:
  - noah11012

---

Welcome to the Reverse String in Ruby page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```ruby
if ARGV.length < 1
    puts "Usage: ruby reverse-string.rb [string]"
else
    string = ARGV[0]

    puts string.reverse
end
```

{% endraw %}

## How to Implement the Solution

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


## How to Run the Solution

If you have Ruby installed on your machine, you can run the following command:

```console
ruby reverse-string.rb SomeStringHere
```

Alternatively, websites like REPL allow you to run code from several programming
languages in your browser. Feel free to leverage one of those!
