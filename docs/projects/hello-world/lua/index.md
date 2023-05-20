---
title: Hello World in Lua
layout: default
last-modified: 2020-10-15
featured-image: hello-world-in-lua.jpg
tags: [lua, hello-world]
authors:
  - the_renegade_coder

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua
print("Hello, World!")
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Lua](https://sampleprograms.io/languages/lua) was written by:

- Jeremy Griffith

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's get down to business.

As we'll quickly notice, Hello World in Lua is not that exciting. In fact, there
are only a handful of languages with this boring of an implementation. For
instance, both Ruby and Python can perform Hello World in a similar fashion.
As a result, there's not a ton of explaining that needs to be done.

Essentially, Lua has a native printing function which can be used to write a
string to stdout. In this case, it's called `print`, but the developers could
have just as easily called it `put`, `write`, `println`, or `puts`.

As usual, we pass a string to the `print` function, and the function handles the
rest.


## How to Run the Solution

Well, perhaps running the script will be more interesting. Fortunately for us,
there's [an online REPL for Lua][2], so we don't have to worry about downloading
anything. Once inside, drop the [code snippet][4] from above into the editor and hit
run. That's it!

Alternatively, we could [download a copy of Lua][3], and run the solution locally.
Even better, we could build a Docker image, so we don't clutter our machine with
dependencies. If you want to help with the Docker initiative, head on over to
the Sample Programs repository and fork it. We appreciate the help!

[2]: https://www.lua.org/cgi-bin/demo
[3]: https://www.lua.org/download.html
[4]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/l/lua/hello-world.lua
