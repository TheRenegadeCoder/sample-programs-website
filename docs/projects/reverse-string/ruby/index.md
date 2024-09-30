---
authors:
- Jeremy Grifski
- Noah Nichols
- rzuckerm
date: 2018-09-24
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- reverse-string
- ruby
title: Reverse String in Ruby
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/ruby/how-to-implement-the-solution.md
- sources/programs/reverse-string/ruby/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Ruby](https://sampleprograms.io/languages/ruby) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ruby
if ARGV.length >= 1
    string = ARGV[0]

    puts string.reverse
end
```

{% endraw %}

Reverse String in [Ruby](https://sampleprograms.io/languages/ruby) was written by:

- Noah Nichols
- rzuckerm

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Right away, we begin by checking to see if the user gave us a string in the
form of a command line argument:

```ruby
if ARGV.length >= 1
```

If not, we exit the program

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

Alternatively, websites like [REPL][1] allow you to run code from several programming
languages in your browser. Feel free to leverage one of those!

[1]: https://replit.com/languages/ruby
