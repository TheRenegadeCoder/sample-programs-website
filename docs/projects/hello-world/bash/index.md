---
authors:
- Abdus
- Jeremy Grifski
- rzuckerm
date: 2018-05-09
featured-image: hello-world-in-bash.jpg
last-modified: 2023-05-15
layout: default
tags:
- bash
- hello-world
title: Hello World in Bash
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/bash/how-to-implement-the-solution.md
- sources/programs/hello-world/bash/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Bash](https://sampleprograms.io/languages/bash) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```bash
#!/bin/bash

echo Hello, World!

```

{% endraw %}

Hello World in [Bash](https://sampleprograms.io/languages/bash) was written by:

- Abdus
- Jeremy Grifski

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

As we can see, printing "Hello, World!" in Bash is quite simple. All we do is call the 
`echo` command to print the string.

As an added note, the shebang (`#!`) tells the environment how to run the script. 
In this case, we want to run the script using Bash. But, we can use this same 
notation for other languages as well:

```python
#!/usr/bin/env python
print("Hello, World!")
```

```ruby
#!/usr/bin/env ruby
puts "Hello, World!"
```

```node
#!/usr/bin/env node
console.log("Hello, World!")
```

Here, we have Hello World in Python, Ruby, and Node.js, respectively. Each of these 
scripting languages can leverage the shebang syntax for easy execution in Unix, Linux, 
and Mac environments.


## How to Run the Solution

If we want to run the solution, we can easily leverage an online Bash shell. To use 
the tool, we just have to drop our solution into the editor and hit run.

Alternatively, if we have a bash shell available, we can easily download the script, 
navigate to its folder from the command line, and run it:

```console
./hello-world.sh
```

In fact, even Windows 10 users can leverage Bash. How-To Geek has a nice tutorial 
on how to use Bash on Windows 10. If that sounds interesting, check it out!
