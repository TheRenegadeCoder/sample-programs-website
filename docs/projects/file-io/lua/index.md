---

title: File Io in Lua

---

Welcome to the File Io in Lua page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Lua
function writer()
	file_to_be_written = io.open("output.txt","w+")
	io.output(file_to_be_written)
	io.write("text to be written into output.txt")
	io.close(file_to_be_written)
end


function reader()
	file_to_be_read = io.open("output.txt","r")
	io.input(file_to_be_read)
	print(io.read())
	io.close(file_to_be_read)
end

writer()
reader()

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.