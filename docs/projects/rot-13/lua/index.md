---

---

Welcome to the Rot 13 in Lua page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Lua
local function ascii_base(s)
  return s:lower() == s and ('a'):byte() or ('A'):byte()
end

function caesar_cipher(str, key)
  return (str:gsub('%a', function(s)
    local base = ascii_base(s)
    return string.char(((s:byte() - base + key) % 26) + base)
  end))
end

if (#arg < 1 or arg[1] == "")
then
    print('Usage: please provide a string to encrypt')
else
    io.write(caesar_cipher(arg[1], 13))
end

io.write("\n")

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.