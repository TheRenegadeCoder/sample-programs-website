---

title: Hello World in MoonScript
layout: default
last-modified: 2020-10-15
featured-image: hello-world-in-moonscript.jpg
tags: [moonscript, hello-world]
authors:
  - bassem_mohamed

---

Welcome to the Hello World in Moonscript page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Moonscript
print "Hello, World!"
```

{% endraw %}

## How to Implement the Solution

As you can see here, Hello World in MoonScript has a relatively simple
implementation:

```moonscript
print "Hello, World!"
```

All we have to do is call the built-in Lua function print, and that's it.
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
