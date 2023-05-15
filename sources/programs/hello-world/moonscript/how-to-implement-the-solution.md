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
