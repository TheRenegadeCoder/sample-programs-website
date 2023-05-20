---
title: File Input Output in Lua
layout: default
date: 2019-10-31
featured-image: file-input-output-in-every-language.jpg
last-modified: 2019-10-31

---

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Lua](https://sampleprograms.io/languages/lua) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lua
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

[File Input Output](https://sampleprograms.io/projects/file-input-output) in [Lua](https://sampleprograms.io/languages/lua) was written by:

- bhaskar_datta
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 15 2020 19:22:39. The solution was first committed on Oct 31 2019 19:53:27. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).