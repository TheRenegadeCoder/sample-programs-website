With the background out of the way, let’s implement Hello World in Crystal:

```crystal
puts "Hello, World!"
```

If we think back, we might remember that this syntax is exactly the same in Ruby. 
Of course, this should come as no surprise as Ruby’s syntax was a major influence 
on Crystal.

[Digging through the API][1] reveals that there are four definitions of puts:

```crystal
def puts(*objects : _) : Nil
def puts : Nil
def puts(obj) : Nil
def puts(string : String) : Nil
```

In our case, we’re using option four which simply writes a string to standard output.

Now, puts is pretty interesting because it automatically appends a new line unless 
a new line already exists. Personally, that’s the first time I’ve heard of a library 
call doing that kind of string formatting for the user. So, my question becomes: what 
happens if the string ends with multiple new lines?

Based on the source code:

```crystal
def puts(string : String) : Nil
self << string
puts unless string.ends_with?('\n')
nil
end
```

The puts library appears to only remove the last new line. After running it, I can 
confirm that’s all this function does. Now, that’s some bizarre behavior:

```crystal
puts 'Hello, World!' # Writes 'Hello, World!\n'
puts 'Hello, World!\n' # Writes 'Hello, World!\n'
puts 'Hello, World!\n\n' # Writes 'Hello, World!\n\n'
```

Honestly, I find this a little buggy. If, by default, this function adds a new 
line, then I would instinctively add a new line to the string (see line 2 above) to 
create extra space.

Of course, that doesn’t work. I suspect that Crystal style would prefer the following:

```crystal
puts 'Hello, World!'
puts
```

Or, something along those lines. At any rate, I’ve gone a bit too far down a rabbit hole. 
Let’s learn how to run our solution.
