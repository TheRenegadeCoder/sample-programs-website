---
authors:
- Jeremy Grifski
- Matt Wiley
- rzuckerm
date: 2018-09-19
featured-image: reverse-string-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- lua
- reverse-string
title: Reverse String in Lua
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/lua/how-to-implement-the-solution.md
- sources/programs/reverse-string/lua/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua
if #arg > 0 then
    print(string.reverse(arg[1]))
end

```

{% endraw %}

Reverse String in [Lua](https://sampleprograms.io/languages/lua) was written by:

- Jeremy Grifski
- Matt Wiley

This article was written by:

- Jeremy Grifski
- Matt Wiley
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's look at the code in detail.

It's pretty simple, right? (It is for sure, but this snippet hides some Lua quirkiness which I've taken some time to call out in the caveats section at the end of the article.)

Let's quickly step through the logic and see what's going on.

### The Basics

Lua is a scripting language, and like almost all scripting languages it is interpreted rather than compiled. The full explanation of what that means is out of scope here, but suffice it to say that Lua has much less rigor in how it is executed than a compiled language might. That's evident from the get go.

The code block above is not a snippet (well it is, but bear with us here), it is the complete script file. We can save this file as `reverse-string.lua` as is and run it with the Lua interpreter. Dead simple.

### The Code Itself

Let's roll through the code in line-by-line fashion. 

Ready? Ok.

#### Line #1

```lua
if #arg > 0 then
```

The first thing we see looks pretty obvious. We have an `if` which we see as a control flow concept in most languages. It is followed by some comparison logic which should resolve to a value of either true or false, and the comparison logic is closed by the keyword `then`. The comparison logic is using a special operator -- the `#`. This `#` operator is the length operator and it is attempting\* to give us the number of arguments that the user has passed to the script. In this case we're checking that the caller has provided at least 1 string input to the script at the command line. If we were to read this in English it would read:

```
If the number of args is greater than 0, then ...
```

#### Line #2

```lua
    print(string.reverse(arg[1]))
```

This is what we're here for! As with most languages, especially scripting languages, these sorts of common operations are baked in. Since we have a built-in utility that let's us do exactly what we're looking to do we can get right to it without having to mess around with special data structures or manual string manipulation. Instead, we get straight to the point. So much so that we can read the code as though it were practically English text.

```
Print the string held in the variable 'arg[1]' in reverse to standard output.
```

At this point you should see your input displayed back to you, but, ya know, in reverse.

**Note:** There's a lot hiding the `string.reverse(...)` syntax where Lua's object-oriented programming is concerned, and unfortunately it is out of scope for this article. If you're interested you should read more about it [here](https://www.lua.org/pil/16.html).

#### Line #3

```lua
end
```

The `end` keyword in Lua closes blocks of code. In this case it closes the `if` (or `if/then`) block. 

After this the interpreter reads the last new line character and an EOF (end-of-file) character, and execution of our script is complete.

### Conclusion

It's hard for string reversal to get much simpler than this. Lua as a language has some strange boundaries but it can be really powerful. 

If you're on a Mac and you're looking for something to play around with that can give you concrete experience with Lua scripting checkout [Hammerspoon](https://www.hammerspoon.org/). It's a Lua-based automation tool for OSX and macOS with some fun integrations for common apps. Check it out!

## Caveats, Notes and Trivia

### \* So about that `#` ...

Right out of the gate we're running into some Lua quirkiness. It's hiding in the `#` unary operator that's hanging out in front of that `arg` variable. So, before we get into the quirk you should know something about Lua: just about everything that's not a number or text is held in a data structure called a table - `arg` is no different. It is a table that holds all of the arguments passed along to the currently running script.

The `#` operator is called the 'length operator', but it's a bit of misnomer. Here's why (and you can read about it in the docs [here](http://www.lua.org/manual/5.2/manual.html#3.4.6)), the operator is ONLY strictly defined for strings, and in the case of strings it actually only counts bytes - not characters. So it would seem that counts on Unicode strings would be, uh, let's say inaccurate. All other values can be overridden to use any length calculation the author of the script provides, and on the face of it this is a pretty interesting feature. That is unless the author doesn't provide a function for calculating length and let's Lua just do Lua things.

Lua, when left to its default behavior for table length calculation, doesn't calculate anything at all. Before I explain, let's get on the same page about tables.

In Lua, tables are alike to dictionaries in Python or objects in Javascript. The syntax is a little different, but the concept is very similar in that you get a set of key-value pairs.

We can define a table in few different ways (and you can read more about this [here](https://www.lua.org/pil/3.6.html)):

```lua
myTable = {a=1, b=2, c=3}
```

This is the same as:

```lua
myTable={}
myTable.a=1 
myTable.b=2
myTable.c=3
```

And if we were define a simple list of strings:

```lua
myThings = {'dog', 'cat', 'bird'}
```

what we're actually getting is 

```lua
myThings[1]='dog'
myThings[2]='cat'
myThings[3]='bird'
```

We're getting an implicit table with numbers for keys. And, this is special when it comes to the default behavior of the `#` operator. It is a table where the keys are a valid sequence, and when Lua sees a sequence in the keys it will report the highest value in the sequence as the length. In this case, 3. So for this EXACT version of a table the default length calculation is correct.

It gets weirder. Hang on.

Lua is (very atypically) a 1-indexed language. Meaning it starts counting at 1, where most other programming languages start counting at 0. So a "valid" sequence only includes the counting numbers {1...n}. **Zero is not included in the sequence.** This means that when we have our script or command-line arguments table:

```lua
arg[0]='my-script.lua' -- the filename of the script being run currently
arg[1]='fibonacci' -- the user input
```

The `#` operator reports a table length of 1 when there are actually two pairs in the table.

How about another (even weirder) example...

If we were to stuff a table like so:

```lua
a={'one', 'two', 'three'}
a['matt']='wiley'
a[5]='five'
```

We're actually getting something like this:

```lua
a[1]='one'
a[2]='two'
a[3]='three'
a['matt']='wiley'
a[5]='five'
```

And when we call `#a` we would get back 3. The docs I've read aren't very clear on why this is the case in Lua. I would expect that the length operator returned some indicator that it just couldn't do its job, but instead it appears to find the first contiguous sequence (in this case {1,2,3}) and report the last key in the sequence as the length.

I know. I don't get it either. That's just Lua.

So, for reading simple lists (or rather even explicitly validly-sequenced tables), the `#` operator works well. For all other use cases: Double check that return value. Weird bugs abound. Better yet, read more about how to leverage other mechanisms of the Lua language to better manage your tables.

For command-line argument, though, this works just fine.


## How to Run the Solution

First, make sure you have Lua installed on your local machine. You can read about how to do that here: [Getting started with Lua](https://www.lua.org/start.html).

Once you have Lua installed, you can download the `reverse-string.lua` file from this repo ([here](https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/l/lua/reverse-string.lua)).

Save that file wherever you like, then open a terminal or command prompt to that directory.

There you should be able to run the following:

```sh
lua reverse-string.lua fibonacci
```

And see the following output:

```sh
iccanobif
```
