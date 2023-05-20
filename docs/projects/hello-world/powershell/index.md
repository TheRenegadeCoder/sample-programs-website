---
title: Hello World in PowerShell
layout: default
last-modified: 2020-10-15
featured-image: hello-world-in-powershell.jpg
tags: [powershell, hello-world]
authors:
  - alcha

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Powershell](https://sampleprograms.io/languages/powershell) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```powershell
Write-Host "Hello, World!"
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Powershell](https://sampleprograms.io/languages/powershell) was written by:

- Devin Leaman

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's get something working! 😊

To execute this code, open a [PowerShell][1] console on any Windows machine as it
comes installed by default. You'll see the reply output in the window like so:

```console
[20:35:40]:Alcha$ Write-Host 'Hello, World!'
Hello, World!
[20:35:56]:Alcha$
```

As is the case with most modern scripting languages, getting a Hello World
sample running is really easy.

[1]: https://learn.microsoft.com/en-us/powershell/


## How to Run the Solution

Instead of running the commands directly within the console though, write your
scripts in a file and call the file when necessary. Download a copy of the
[HelloWorld.ps1][2] file from the repository and open a console.

Now, navigate to wherever you downloaded the script and execute it by calling
it like so:

```console
.\HelloWorld.ps1
```

This calls the script and returns the output to the console:

```console
[20:35:40]:powershell$ .\HelloWorld.ps1
Hello, World!
[20:35:56]:powershell$
```

And, that's it!

[2]: https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/p/powershell/HelloWorld.ps1
