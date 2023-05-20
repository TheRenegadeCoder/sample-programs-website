---
title: Hello World in MoonScript
layout: default
last-modified: 2020-10-15
featured-image: hello-world-in-moonscript.jpg
tags: [moonscript, hello-world]
authors:
  - bassem_mohamed

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Moonscript](https://sampleprograms.io/languages/moonscript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```moonscript
print "Hello, World!"
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Moonscript](https://sampleprograms.io/languages/moonscript) was written by:

- bassemmohamed1994

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Hello World in MoonScript has a relatively simple implementation.

All we have to do is call the built-in Moonscript function `print`, and that's it.
Behind the scenes, the code is compiled into Lua which is, in this case,
exactly the same.

In other cases, it could be different. For instance, we could have an
implementation of some arithmetic which we print to the user:

```moonscript
x = 10
y = 15
z = x + y
print y
```

The code is then compiled into Lua like this:

```lua
local x = 10
local y = 15
local z = x + y
return print(y)
```

How cool is that?


## How to Run the Solution

If your feeling adventurous today, You can quickly install MoonScript using one
of the following methods:

**For Windows users**, you can [try installing the windows binaries][4].

**For Linux users**, install [LuaRocks][5] which is a package manager for Lua modules.
Then run the following command:

```console
luarocks install moonscript
```

With the moon executable and Lua modules on your device, run your .moon file
with this command:

```console
moon ./YOURFILE.moon
```

Also, you can compile your .moon file into Lua by using this command:

```console
moonc ./YOURFILE.moon
```

Alternatively, you can always [run MoonScript using an online compiler][6].

[4]: https://moonscript.org/#windows_binaries
[5]: http://www.luarocks.org/
[6]: https://moonscript.org/compiler/
